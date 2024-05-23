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
    st.title('IndexReplicator')
    
    st.write("## Introduction")
    st.write("""
        Welcome to our emerging financial consultancy firm! We specialize in replicating the returns of various indices using futures contracts:
        - MSCI World AC
        - BB Global Bond Agg
        - HFRX Index
        - Monster Index (a linear combination of the above)
    """)

    st.write("### Index Returns")
    st.write("Below is the plot showing the returns of the selected indices over time.")
    plot_index_returns()

    st.write("## List of Futures")
    show_futures_list()

    st.write("## Choose Index to Replicate")
    selected_index = st.selectbox("Select an index to replicate", ["MSCI World AC", "BB Global Bond Agg", "HFRX Index", "Monster Index"])

    st.write(f"## Regression Model for Replication of {selected_index}")
    st.write("In order to replicate the selected index, we utilize a regression model that provides the best fit.")
    st.write("Below is the plot of replicated returns along with error and trading costs.")
    #st.image("replication_results.png", caption="Replication Results")
    st.write(f"Error: X.XX, Trading Costs: Y.YY")

if __name__ == "__main__":
    main()
