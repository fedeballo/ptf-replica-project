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

# Funzione principale
def main():
    st.markdown(
        """
        <style>
        .title {
            font-size: 32px !important;
            text-align: center;
        }
        .logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-top: 20px;
            margin-bottom: 50px;
        }
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            width: 100%;
            padding-left: 50px;
            padding-right: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.title('ReplicaPro')  # Utilizzo di st.header() per un titolo più grande
    st.image("Logo.png", width=400, use_column_width=False)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Espandi l'introduzione
    with st.expander("Introduction"):
        st.write("""
            Welcome to our emerging financial consultancy firm! We specialize in replicating the returns of various indices using futures contracts:
            - MSCI World AC
            - BB Global Bond Agg
            - HFRX Index
            - Monster Index (a linear combination of the above)
        """)

    # Espandi i rendimenti degli indici
    with st.expander("Index Returns"):
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
