# 🤖 SQL Bot — AI Database Assistant

SQL Bot is your personal AI-powered database assistant that lets you query and explore data just by asking questions in plain English. Whether your data is in MySQL, CSV, or Excel, this bot will handle it — generating optimized SQL queries and even explaining complex ones.

-----

## ✨ Key Features

  - **Multiple Data Sources**
      - **MySQL Connection:** Connect to any live MySQL database securely.
      - **CSV & Excel Upload:** Instantly load and query uploaded files.
      - **Schema Mode:** Paste `CREATE TABLE` SQL and start asking questions without any data upload.
  - **Smart AI Capabilities**
      - **Text ➡ SQL:** Ask “*Show top 5 highest selling products*” and get a ready-to-run SQL query.
      - **SQL ➡ Text:** Paste a query and get a beginner-friendly explanation.
      - **General Q\&A:** Beyond SQL, you can ask regular questions too.
  - **Modern Interactive UI**
      - Built with **Streamlit** for a smooth chat-like experience.
      - Simple sidebar for source selection & schema viewing.
      - Real-time SQL generation & execution.

-----

## 🛠️ Tech Stack

| Category | Tools & Technologies |
| :--- | :--- |
| **Languages** | Python |
| **Frontend** | Streamlit |
| **AI Models** | Ollama + llama3.1:8b |
| **Libraries** | Pandas, SQLAlchemy, LangChain, MySQL Connector |
| **Data Handling** | CSV, Excel, MySQL |
| **Version Control**| GitHub |

-----

## 📦 Installation & Setup

1.  **Create Virtual Environment**

    ```bash
    python -m venv venv
    ```

    Activate it:

      - **Windows:** `venv\Scripts\activate`
      - **macOS/Linux:** `source venv/bin/activate`

2.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Install & Start Ollama**
    Download the model:

    ```bash
    ollama pull llama3.1:8b
    ```

    Keep the Ollama application running in the background.

4.  **Launch the App**

    ```bash
    streamlit run app.py
    ```

    Open the provided URL in your browser and start chatting with your database.

-----

## 📖 How to Use

  - **Select a Data Source:** Choose between connecting to MySQL, uploading a file, or providing a schema in text mode.
  - **View Current Schema:** See all tables & columns for reference in the sidebar.
  - **Chat with SQL Bot:** Ask questions, paste SQL for explanations, or explore your data.
  - **Get Results:** The bot provides the generated SQL query, an AI explanation, a sample table, and live DB output if connected.

-----

## 📂 Project Structure

```
sql-bot/
├── utils/
│   ├── __init__.py         # Package initializer
│   ├── database.py       # DB connection handling
│   ├── file_processor.py   # CSV/Excel handling
│   └── llm_handler.py      # AI prompt & model logic
├── app.py                  # Main Streamlit app
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

-----

## 🧠 Example Queries

| You Ask | Bot Generates |
| :--- | :--- |
| “Show me the top 10 customers by spending” | `SELECT customer_id, SUM(amount) AS total_spent FROM sales GROUP BY customer_id ORDER BY total_spent DESC LIMIT 10;` |
| “Explain: `SELECT COUNT(*) FROM orders WHERE status='Pending';`” | This query counts all orders where the status is ‘Pending’. |
