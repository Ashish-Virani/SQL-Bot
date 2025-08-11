# utils/file_processor.py
import pandas as pd
import streamlit as st

def process_uploaded_file(uploaded_file):
    """Reads an uploaded CSV or XLSX file into a pandas DataFrame."""
    if uploaded_file is None:
        return None
    
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload a CSV or XLSX file.")
            return None
        return df
    except Exception as e:
        st.error(f"Error reading file: {e}")
        return None