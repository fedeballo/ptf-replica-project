import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Funzione per visualizzare il grafico dei rendimenti degli indici
def plot_index_returns():
    fig, ax = plt.subplots(figsize=(10, 6))
    dates = np.arange('2020-01', '2025-01', dtype='datetime64[M]')
    for index_name in ["MSCI World AC", "BB Global Bond Agg", "HFRX Index", "Monster Index"]:
        index_returns = np.random.randn(len(dates)).cumsum()
        ax.plot(dates, index_returns, label=index_name)
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

# Imposta lo stile del sito con uno sfondo scuro
def set_custom_style():
    st.markdown(
        """
        <style>
        body {
            color: white;
            background-color: #1f1f1f; /* Colore sfondo scuro */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

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
        st.write("""The indices we have focused on for replication are as follows:
                    - **MSCI World AC**: This index captures large and mid-cap representation across 23 developed markets and 27 emerging markets countries, reflecting the performance of the global equity market.
                    - **BB Global Bond Agg**: The Bloomberg Global Aggregate Bond Index is a flagship measure of global investment-grade debt from 24 local currency markets, providing a broad-based exposure to the global bond market.
                    - **HFRX Index**: This index is designed to be representative of the overall composition of the hedge fund universe, offering insight into the performance of various hedge fund strategies.
                    - **Monster Index**: A custom index that is a linear combination of the above indices, providing a diversified blend of equities, bonds, and alternative investments for a balanced investment approach.
        """)
        st.write("Below is the plot showing the returns of the selected indices over time.")
        plot_index_returns()

    # Espandi l'elenco dei futures
    with st.expander("List of Futures"):
        show_futures_list()

    # Espandi la scelta dell'indice da replicare
    with st.expander("Choose Index to Replicate"):
        selected_index = st.selectbox("Select an index to replicate", ["MSCI World AC", "BB Global Bond Agg", "HFRX Index", "Monster Index"])

        # Dizionario che mappa ogni indice a un testo specifico e ad altri dettagli
        index_details = {
            "MSCI World AC": {
                "description": "In order to replicate the MSCI World AC, we utilize a diversified portfolio of futures contracts across various asset classes.",
                "error": "1.23",
                "trading_costs": "0.45",
                # "image": "msci_world_ac.png" # Assicurati che l'immagine esista nel repository
            },
            "BB Global Bond Agg": {
                "description": "To replicate the BB Global Bond Agg index, we focus on fixed-income futures, ensuring a stable and low-risk investment.",
                "error": "0.89",
                "trading_costs": "0.32",
                # "image": "bb_global_bond_agg.png"
            },
            "HFRX Index": {
                "description": "Replicating the HFRX Index involves a sophisticated strategy using long and short positions in a variety of futures contracts.",
                "error": "1.78",
                "trading_costs": "0.67",
                # "image": "hfrx_index.png"
            },
            "Monster Index": {
                "description": "The Monster Index is a comprehensive blend of equities, bonds, and alternative investments, replicated using a mix of futures contracts.",
                "error": "2.34",
                "trading_costs": "0.89",
                # "image": "monster_index.png"
            }
        }

        st.write(f"## Regression Model for Replication of {selected_index}")
        st.write(index_details[selected_index]["description"])
        st.write("Below is the plot of replicated returns along with error and trading costs.")
        # st.image(index_details[selected_index]["image"], caption="Replication Results")
        st.write(f"Error: {index_details[selected_index]['error']}, Trading Costs: {index_details[selected_index]['trading_costs']}")

if __name__ == "__main__":
    main()
