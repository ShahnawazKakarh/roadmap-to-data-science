import streamlit as st
from dotenv import load_dotenv
import io
import os
import google.generativeai as genai
import pandas as pd


load_dotenv()

st.title("AI Financial Analyzer")
st.divider()
st.badge("KAKS PVT LTD, COPYRIGHT 2025")
st.markdown("Make better decision with AI in Finance")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
st.write("✅ API key loaded:", bool(GEMINI_API_KEY))

uploaded_file = st.file_uploader("Upload your financial data (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    tab1, tab2, tab3 = st.tabs(["Data Summary", "Cleaned Data", "AI Insights"])
    with tab1:
        st.subheader("Data Summary")
        st.dataframe(df)

    with tab2:
        st.subheader("Cleaned Data")
        "Coercing 'Amount' column to numeric and dropping rows with NaN values"
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
        df.dropna(subset=['Amount'], inplace=True)
        st.dataframe(df)

    with tab3:
        st.subheader("AI Insights")
        prompt = f""" 

Analyze the following financial data provided in CSV format. The data includes columns for 'Date', 'Category', 'Description', 'Amount', and 'Payment Method'.

Provide insights based on this data, including:
1.  A summary of total income and total expenses.
2.  A breakdown of expenses by category.
3.  Identification of the most frequently used payment methods.
4.  Any other interesting observations or patterns you can find in the data.

Here is the data : {df.to_csv(index=False)}
 """

        try:
            model = genai.GenerativeModel("models/gemini-flash-lite-latest")
            response = model.generate_content(prompt)
            st.markdown("## AI Suggestions")
            st.write(response.text)
        except Exception as e:
            st.error("An error occurred while processing the data.".format(e))
            st.stop()