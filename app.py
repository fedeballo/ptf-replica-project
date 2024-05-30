import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Funzione per generare rendimenti casuali cumulati
def generate_cumulative_returns(length):
    return np.random.randn(length).cumsum()

# Funzione per visualizzare il grafico dei rendimenti degli indici
def plot_index_returns(index_name):
    fig, ax = plt.subplots(figsize=(10, 6))
    dates = np.arange('2020-01', '2025-01', dtype='datetime64[M]')
    index_returns = generate_cumulative_returns(len(dates))
    replicated_returns = generate_cumulative_returns(len(dates))

    ax.plot(dates, index_returns, label=f"{index_name} Actual Returns")
    ax.plot(dates, replicated_returns, label=f"{index_name} Replicated Returns", linestyle='--')
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Returns')
    ax.set_title(f'{index_name} Returns Over Time')
    ax.legend()
    
    # Calcolo di esempio per MAE e Tracking Error
    mae = np.mean(np.abs(index_returns - replicated_returns))
    tracking_error = np.std(index_returns - replicated_returns)

    st.pyplot(fig)
    st.write(f"Mean Absolute Error (MAE): {mae:.2f}")
    st.write(f"Tracking Error: {tracking_error:.2f}")

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
            - **MSCI World AC**: This index captures large and mid-cap representation across 23 developed markets and 27 emerging markets countries, reflecting the performance of the global equity market.
            - **BB Global Bond Agg**: The Bloomberg Global Aggregate Bond Index is a flagship measure of global investment-grade debt from 24 local currency markets, providing a broad-based exposure to the global bond market.
            - **HFRX Index**: This index is designed to be representative of the overall composition of the hedge fund universe, offering insight into the performance of various hedge fund strategies.
            - **Monster Index 1**: A custom index that is a linear combination of the above indices with weights [0.3, 0.2, 0.5], providing a diversified blend of equities, bonds, and alternative investments.
            - **Monster Index 2**: Another custom index that is a linear combination of the above indices with weights [0.4, 0.1, 0.5], offering a different diversified investment approach.
        """)
        st.write("Below is the plot showing the returns of the selected indices over time.")
        plot_index_returns("MSCI World AC")  # Display a sample plot initially

    # Espandi l'elenco dei futures
    with st.expander("List of Futures"):
        show_futures_list()

    # Espandi la scelta dell'indice da replicare
    with st.expander("Choose Index to Replicate"):
        selected_index = st.selectbox("Select an index to replicate", ["MSCI World AC", "BB Global Bond Agg", "HFRX Index", "Monster Index 1", "Monster Index 2"])

        st.write(f"## Replication of {selected_index}")
        
        # Input per l'ammontare dell'investimento
        investment_amount = st.number_input("Enter the amount you want to invest:", min_value=0.0, step=100.0)
        
        # Proporzioni di investimento nei futures (valori di esempio)
        futures_allocation = {
            "MSCI World AC": {'RX1': 0.10, 'CO1': 0.05, 'DU1': 0.10, 'ES1': 0.20, 'GC1': 0.05, 'NQ1': 0.15, 'TP1': 0.05, 'TU2': 0.10, 'TY1': 0.10, 'VG1': 0.10},
            "BB Global Bond Agg": {'RX1': 0.25, 'CO1': 0.05, 'DU1': 0.25, 'ES1': 0.05, 'GC1': 0.05, 'NQ1': 0.05, 'TP1': 0.05, 'TU2': 0.15, 'TY1': 0.10, 'VG1': 0.05},
            "HFRX Index": {'RX1': 0.10, 'CO1': 0.10, 'DU1': 0.10, 'ES1': 0.15, 'GC1': 0.10, 'NQ1': 0.10, 'TP1': 0.10, 'TU2': 0.10, 'TY1': 0.10, 'VG1': 0.05},
            "Monster Index 1": {'RX1': 0.15, 'CO1': 0.10, 'DU1': 0.10, 'ES1': 0.10, 'GC1': 0.10, 'NQ1': 0.10, 'TP1': 0.05, 'TU2': 0.10, 'TY1': 0.10, 'VG1': 0.10},
            "Monster Index 2": {'RX1': 0.20, 'CO1': 0.05, 'DU1': 0.15, 'ES1': 0.10, 'GC1': 0.05, 'NQ1': 0.10, 'TP1': 0.05, 'TU2': 0.10, 'TY1': 0.10, 'VG1': 0.10},
        }

        # Calcola l'investimento per ciascun future
        if investment_amount > 0:
            allocations = futures_allocation[selected_index]
            st.write("### Investment Allocation")
            for future_code, proportion in allocations.items():
                amount_invested = investment_amount * proportion
                st.write(f"**{future_code}:** {amount_invested:.2f}")

            # Mostra il grafico dei rendimenti dell'indice scelto e della replica
            plot_index_returns(selected_index)

if __name__ == "__main__":
    main()
