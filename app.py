import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    # Carica i dati dal file CSV
    data = pd.read_csv(file_path)
    return data

def plot_index_returns(data):
    # Crea il grafico dei rendimenti degli indici sovrapposti
    plt.figure(figsize=(10, 6))
    for index_name, index_returns in data.items():
        plt.plot(index_returns, label=index_name)
    plt.xlabel('Date')
    plt.ylabel('Returns')
    plt.title('Index Returns Over Time')
    plt.legend()
    st.pyplot()

def show_futures_list():
    # Visualizza l'elenco dei futures utilizzati nel portafoglio di replica
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

def main():
    st.title('Financial Replication App')

    st.write("## Introduction")
    st.write("Welcome to our emerging financial consultancy firm! We specialize in replicating the returns of various indices using futures contracts.")

    st.write("### Index Returns")
    st.write("Below is the plot showing the returns of the selected indices over time.")
    indices_data = load_data("indices_returns.csv")
    plot_index_returns(indices_data)

    st.write("## List of Futures")
    show_futures_list()

    st.write("## Choose Index to Replicate")
    selected_index = st.selectbox("Select an index to replicate", ["MSCI World AC", "BB Global Bond Agg", "HFRX Index", "Monster Index"])

    st.write(f"## Regression Model for Replication of {selected_index}")
    st.write("In order to replicate the selected index, we utilize a regression model that provides the best fit.")
    st.write("Below is the plot of replicated returns along with error and trading costs.")

    # Carica i dati dei rendimenti replicati e dei costi di trading
    #plot_replicated_returns(replicated_returns)
    #plot_error_and_trading_costs(error, trading_costs)

if __name__ == "__main__":
    main()
