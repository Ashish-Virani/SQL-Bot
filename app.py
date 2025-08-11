# app.py
import streamlit as st
from utils.database import get_mysql_db_connection, create_db_from_dataframe
from utils.file_processor import process_uploaded_file
from utils.llm_handler import get_llm_response, extract_sql_query

# --- Page Configuration ---
st.set_page_config(page_title="SQL Bot 🤖", layout="wide")
st.title("SQL Bot: Your AI Database Assistant")
st.markdown("Powered by `llama3.1:8b`.")

# --- Session State Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "db_schema" not in st.session_state:
    st.session_state.db_schema = None
if "db_connection" not in st.session_state:
    st.session_state.db_connection = None
# CRITICAL: Add db_engine to the session state to persist it
if "db_engine" not in st.session_state:
    st.session_state.db_engine = None

# --- Sidebar for Configuration ---
with st.sidebar:
    st.header("⚙️ Configuration")
    use_case = st.selectbox(
        "Choose your data source:",
        ["Connect to MySQL", "Upload a File", "Provide Schema Text"]
    )

    # --- MySQL Connection UI ---
    if use_case == "Connect to MySQL":
        st.subheader("MySQL Connection")
        db_user = st.text_input("Username", "root")
        db_password = st.text_input("Password", type="password")
        db_host = st.text_input("Host", "localhost")
        db_port = st.text_input("Port", "3306")
        db_name = st.text_input("Database Name")
        if st.button("🔌 Connect"):
            with st.spinner("Connecting to database..."):
                try:
                    db_conn = get_mysql_db_connection(db_user, db_password, db_host, db_port, db_name)
                    st.session_state.db_connection = db_conn
                    st.session_state.db_schema = db_conn.table_info
                    st.session_state.db_engine = None # Clear file DB engine if it exists
                    st.success("✅ Connected successfully!")
                    st.toast("Schema loaded!")
                except Exception as e:
                    st.error(f"❌ {e}")
    
    # --- File Upload UI (CORRECTED LOGIC) ---
    elif use_case == "Upload a File":
        st.subheader("File Upload")
        uploaded_file = st.file_uploader("Upload CSV or XLSX file", type=['csv', 'xlsx'])
        if uploaded_file:
            table_name = st.text_input("Enter a name for your data table:", "uploaded_data")
            if st.button("💾 Load Data"):
                with st.spinner("Processing file..."):
                    df = process_uploaded_file(uploaded_file)
                    if df is not None:
                        # Capture both the db object and the engine from the utility function
                        db_conn, db_engine = create_db_from_dataframe(df, table_name)
                        
                        # CRITICAL: Store BOTH the connection and the engine
                        st.session_state.db_connection = db_conn
                        st.session_state.db_engine = db_engine 
                        st.session_state.db_schema = db_conn.table_info
                        
                        st.success("✅ File processed and loaded into temporary DB!")
                        st.toast("Schema loaded!")

    # --- Raw Schema UI ---
    elif use_case == "Provide Schema Text":
        st.subheader("Raw Schema Input")
        schema_text = st.text_area("Paste your CREATE TABLE statements here:", height=200)
        if st.button("📌 Set Schema"):
            st.session_state.db_schema = schema_text
            st.session_state.db_connection = None # No executable connection
            st.session_state.db_engine = None # Clear file DB engine if it exists
            st.success("✅ Schema set successfully!")
            st.toast("Schema loaded!")

    # Display current schema if loaded
    if st.session_state.db_schema:
        with st.expander("View Current Schema", expanded=False):
            st.code(st.session_state.db_schema, language="sql")

# --- Main Chat Interface ---
st.header("💬 Chat with your Data")

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask a question or enter an SQL query to explain..."):
    if not st.session_state.db_schema:
        st.warning("Please configure a data source in the sidebar first.")
        st.stop()
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response_data = get_llm_response(prompt, st.session_state.db_schema)
                full_response = response_data["response_text"]
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})

                sql_query = extract_sql_query(full_response)
                if sql_query:
                    if st.session_state.db_connection:
                        with st.spinner("Executing query..."):
                            query_result = st.session_state.db_connection.run(sql_query)
                            st.markdown("---")
                            st.markdown("**📊 Query Result:**")
                            st.dataframe(query_result)
                    else:
                        st.info("A SQL query was generated, but it cannot be executed because no active database connection was found.")

            except Exception as e:
                st.error(f"An error occurred: {e}")
                # We don't add technical errors to the chat history