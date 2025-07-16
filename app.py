import streamlit as st
import pandas as pd

# Load the CSV
df = pd.read_csv('wireshark2.csv')

# App Title
st.title("Wireshark2 Network Traffic Dashboard")

# Preview the Data
st.subheader("Dataset Preview")
st.write(df.head())

# Protocol Counts Bar Chart
st.subheader("Protocol Distribution")
protocol_counts = df['Protocol'].value_counts()
st.bar_chart(protocol_counts)
