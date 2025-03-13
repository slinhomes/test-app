
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

# Set page title
st.title("Hello World")

# Fetch database connection string from environment variable
DATABASE_URL = os.getenv("AZURE_SQL_CONNECTION")

# Connect to Azure SQL using SQLAlchemy
@st.cache_data(show_spinner=True)
def fetch_data():
    try:
        engine = create_engine(DATABASE_URL)
        query = """
        SELECT TOP 5 * FROM SHMDwellingInfo;
        """
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

# Display the data
df = fetch_data()
st.write("Here are 5 rows of data from your Azure SQL Database:")
st.dataframe(df)