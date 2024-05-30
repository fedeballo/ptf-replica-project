import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Funzione per visualizzare il grafico dei rendimenti degli indici
def plot_index_returns():
    fig, ax = plt.subplots(figsize=(10, 6))
    dates = np.arange('2020-01', '2025-01', dtype='datetime64[M]')
    index_returns = np.linspace(1, 1.5, len(dates))  # Rendimenti di esempio

    ax.plot(dates, index_returns, label="Index Returns")
    ax.set_xlabel('Date')
    ax.set_ylabel('Returns')
    ax.set_title('Index Returns Over Time')
    ax.legend()
    st.pyplot(fig)

# Funzione per visualizzare l'elenco dei futures
def show_futures_list():
    futures_list = {
        'RX1': 'Fixed-income security issued by the Federal Republic of Germany.',
        'CO1': 'Price of Brent crude oil in the financial markets.',
        'DU1': 'The German 2-year government bond, known as the "Schatz."',
        'ES1': 'It represents a broad-based stock market index of 500 large companies listed on U.S. stock exchanges.',
        'GC1': 'Price of gold.',
        'NQ1': 'The Nasdaq 100 index.',
        'TP1': 'It\'s associated with the Topix index.',
        'TU2': 'It refers to the 2-year US Treasury bond.',
        'TY1': '10-years US Treasury bond.',
        'VG1': 'Euro Stoxx 50 index.'
    }

    st.write("### List of Futures Used in the Replication Portfolio")
    for future_code, description in futures_list.items():
        st.write(f"**{future_code}:** {description}")

# Funzione principale
def main():
    st.image('Logo.png')  # TITLE and Creator information
    st.write('\n')  # add spacing
    st.markdown('Welcome to ReplicaPro! Our platform offers a unique way to invest in futures contracts that replicate the performance of key indices. Explore the potential of diversifying your portfolio with ease and precision.')
    st.write('\n')  # add spacing
    
    # Espandi l'introduzione
    with st.expander("About us"):
        st.write("""
            Welcome to our emerging financial consultancy firm! We specialize in replicating the returns of various indices using futures contracts. We are a group of students from Politecnico di Milano who have developed this project with a passion for finance and technology. Our replicated portfolios are derived through the application of various models and advanced machine learning techniques, ensuring precision and effectiveness in our investment strategies.
        """)

    # Espandi i rendimenti degli indici
    with st.expander("Introduction to the Indices"):
        st.markdown("""
            ### The indices we have focused on for replication are as follows:
            - **MSCI World All Country**: This index captures large and mid-cap representation across 23 developed markets and 27 emerging markets countries, reflecting the performance of the global equity market.
            - **MSCI World**: This index captures large and mid-cap representation across 23 developed markets countries, reflecting the performance of the global developed equity market.
            - **BB Global Bond Agg**: The Bloomberg Global Aggregate Bond Index is a flagship measure of global investment-grade debt from 24 local currency markets, providing a broad-based exposure to the global bond market.
            - **HFRX Index**: This index is designed to be representative of the overall composition of the hedge fund universe, offering insight into the performance of various hedge fund strategies.
            - **Monster Index 1**: A custom index that is a linear combination of the above indices with weights [0.25, 0, 0.25, 0.5], providing a diversified blend of equities, bonds, and alternative investments.
            - **Monster Index 2**: Another custom index that is a linear combination of the above indices with weights [0.05, 0.4, 0.3, 0.25], offering a different diversified investment approach.
        """)
        st.write("Below is the plot showing the returns of the selected indices over time.")
        plot_index_returns()

    # Espandi l'elenco dei futures
    with st.expander("List of Futures"):
        show_futures_list()

    # Espandi la scelta dell'indice da replicare
    with st.expander("Choose Index to Replicate"):
        selected_index = st.selectbox("Select an index to replicate", ["MSCI World AC", "MSCI World", "BB Global Bond Agg", "HFRX Index", "Monster Index 1", "Monster Index 2"])

        st.write(f"## Replication of {selected_index}")
        
        # Input for the investment amount
        investment_amount = st.number_input("Enter the amount you want to invest in the selected index: \n<br><small><i>Note that the replication portfolio might employ leverage or have a lower overall value.</i></small>", min_value=0.0, step=100.0, format="%.2f")

        # Proporzioni di investimento nei futures (valori di esempio)
        futures_allocation = {
            "MSCI World AC": {'CO1': 0.0658, 'DU1': 0, 'ES1': 0.4981, 'GC1': 0, 'NQ1': 0.0082, 'RX1': 0.2052, 'TP1': 0, 'TU2': 0, 'TY1': 0, 'VG1': 0},
            "MSCI World": {'CO1': 0.0931, 'DU1': 0, 'ES1': 0.4558, 'GC1': 0, 'NQ1': 0.0078, 'RX1': 0.2031, 'TP1': 0, 'TU2': 0, 'TY1': 0, 'VG1': 0},
            "BB Global Bond Agg": {'CO1': 0.0168, 'DU1': 0, 'ES1': 0, 'GC1': 0.2097, 'NQ1': 0.0059, 'RX1': 0.6707, 'TP1': 0, 'TU2': 0, 'TY1': 0, 'VG1': 0},
            "HFRX Index": {'CO1': 0.0782, 'DU1': 0.0790, 'ES1': 0.0513, 'GC1': 0.0467, 'NQ1': 0, 'RX1': 0.2697, 'TP1': 0.0673, 'TU2': 0.0660, 'TY1': 0.0713, 'VG1': 0},
            "Monster Index 1": {'CO1': 0.1044, 'DU1': 0, 'ES1': 0, 'GC1': 0, 'NQ1': 0.0508, 'RX1': 0.5973, 'TP1': 0, 'TU2': 0, 'TY1': 0, 'VG1': 0},
            "Monster Index 2": {'CO1': 0.1060, 'DU1': 0, 'ES1': 0.0867, 'GC1': 0, 'NQ1': 0.0518, 'RX1': 0.5355, 'TP1': 0, 'TU2': 0, 'TY1': 0, 'VG1': 0},
        }

        # Calcola l'investimento per ciascun future
        if investment_amount > 0:
            allocations = futures_allocation[selected_index]
            st.write("### Investment Allocation")
            for future_code, proportion in allocations.items():
                amount_invested = investment_amount * proportion
                st.write(f"**{future_code}:** {amount_invested:.2f}")

            # Mostra il grafico dei rendimenti dell'indice scelto e della replica
            if selected_index == "MSCI World AC":
                st.image("MXWO_LASSO_COMPARISON.png")
                st.write("Mean Tracking Error: 0.0224")
                st.write("Information Ratio: -0.8347")
                st.write("Mean Turnover: 0.006")
            elif selected_index == "MSCI World":
                st.image("MXWD_LASSO_PREDICTION.png")
                st.write("Mean Tracking Error: 0.0352")
                st.write("Information Ratio: -0.3977")
                st.write("Mean Turnover: 0.0077")    
            elif selected_index == "BB Global Bond Agg":
                st.image("LEGATRUU_LASSO_PREDICTION.png")
                st.write("Mean Tracking Error: 0.0366")
                st.write("Information Ratio: 0.0964")
                st.write("Mean Turnover: 0.0022")
            elif selected_index == "HFRX Index":
                st.image("HFRLX_ELASTIC_COMPARISON.png")
                st.write("Mean Tracking Error: 0.0158")
                st.write("Information Ratio: -0.3074")
                st.write("Mean Turnover: 0.0036")
            elif selected_index == "Monster Index 1":
                st.image("MONSTER1_LASSO_PREDICTION.png")
                st.write("Mean Tracking Error: 0.0243")
                st.write("Information Ratio: -0.6899")
                st.write("Mean Turnover: 0.0049")
            elif selected_index == "Monster Index 2":
                st.image("MONSTER2_LASSO_COMPARISON.png")
                st.write("Mean Tracking Error: 0.030")
                st.write("Information Ratio: -0.485")
                st.write("Mean Turnover: 0.0056")

if __name__ == "__main__":
    main()
