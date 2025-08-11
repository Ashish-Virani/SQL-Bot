# 🚀 SQL Bot — AI Database Assistant
**SQL Bot is your personal AI-powered database assistant that lets you query and explore data just by asking questions in plain English.
Whether your data is in MySQL, CSV, or Excel, this bot will handle it — generating optimized SQL queries and even explaining complex ones.

# ✨ Key Features
📂 Multiple Data Sources
🔗 MySQL Connection — Connect to any live MySQL database securely.

📄 CSV & Excel Upload — Instantly load and query uploaded files.

📜 Schema Mode — Paste CREATE TABLE SQL and start asking questions without any data upload.

🤖 Smart AI Capabilities
Text ➡ SQL — Ask “Show top 5 highest selling products” and get a ready-to-run SQL query.

SQL ➡ Text — Paste a query and get a beginner-friendly explanation.

General Q&A — Beyond SQL, you can ask regular questions too.

Sample Outputs — Shows realistic dummy data for better understanding.

🖥 Modern Interactive UI
Built with Streamlit for a smooth chat-like experience.

Simple sidebar for source selection & schema viewing.

Real-time SQL generation & execution.

🛠 Tech Stack
Category	Tools & Technologies
Languages	Python
Frontend	Streamlit
AI Models	Ollama + llama3.1:8b
Libraries	Pandas, SQLAlchemy, LangChain, MySQL Connector
Data Handling	CSV, Excel, MySQL
Version Control	GitHub

📦 Installation & Setup
1️⃣ Create Virtual Environment
bash
Copy
Edit
python -m venv venv
Activate it:

bash
Copy
Edit
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Install & Start Ollama
Download the model:

bash
Copy
Edit
ollama pull llama3.1:8b
Keep Ollama running in the background.

4️⃣ Launch the App
bash
Copy
Edit
streamlit run app.py
Open in your browser and start chatting with your database.

📖 How to Use
Select a Data Source
Choose between:

Connect to MySQL — enter DB credentials.

Upload CSV/Excel — instantly query uploaded data.

Schema Mode — paste CREATE TABLE statements.

View Current Schema
See all tables & columns for reference.

Chat with SQL Bot
Ask questions, paste SQL for explanations, or explore your data.

Get Results

Generated SQL query.

AI explanation.

Dummy sample table.

Live DB output (if connected).

📂 Project Structure
bash
Copy
Edit
sql-bot/
├── utils/
│   ├── __init__.py        # Package initializer
│   ├── database.py        # DB connection handling
│   ├── file_processor.py  # CSV/Excel handling
│   └── llm_handler.py     # AI prompt & model logic
├── app.py                 # Main Streamlit app
├── requirements.txt       # Dependencies
└── README.md              # Documentation
🧠 Example Queries
You Ask	Bot Generates
“Show me the top 10 customers by spending”	SELECT customer_id, SUM(amount) AS total_spent FROM sales GROUP BY customer_id ORDER BY total_spent DESC LIMIT 10;
“Explain: SELECT COUNT(*) FROM orders WHERE status='Pending';”	Counts all orders where the status is ‘Pending’.

