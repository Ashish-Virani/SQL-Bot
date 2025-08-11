🤖 SQL Bot: Your AI Database Assistant
SQL Bot is an intelligent, conversational application that allows you to interact with your databases using natural language. Built with Python and Streamlit, it leverages the power of local large language models (LLMs) through Ollama to translate your questions into executable SQL queries and explain complex queries in simple terms.

This tool is designed for data analysts, developers, and anyone who wants to access database information without writing SQL manually.

## ✨ Features
Multiple Data Sources:

Direct MySQL Connection: Securely connect to your live MySQL databases.

File Upload: Upload CSV or XLSX files, which are instantly loaded into a temporary, queryable database.

Schema-Only Mode: Provide a CREATE TABLE schema, and the bot will generate queries without needing a live connection.

Intelligent AI Core: Powered by llama3.1:8b, the bot can handle a variety of tasks:

Text-to-SQL: Ask a question like "show me the total sales last month," and get a ready-to-run SQL query.

SQL-to-Text: Paste a complex SQL query to receive a step-by-step explanation of what it does.

General Q&A: Ask off-topic questions and receive helpful answers.

Rich, Data-Driven Examples: When generating a query, the bot also creates and displays dummy data to illustrate exactly how the query works and what the output will look like.

Interactive UI: A clean and user-friendly web interface built with Streamlit makes it easy to configure your data source and chat with the bot.

## 🛠️ Technology Stack
Backend: Python

Frontend: Streamlit

AI/LLM: Ollama with llama3.1:8b

Core Libraries:

langchain-community for LLM and database integration.

pandas for data manipulation.

sqlalchemy and mysql-connector-python for database connections.

## 🚀 Getting Started
Follow these steps to set up and run the SQL Bot on your local machine.

### Prerequisites
Make sure you have the following installed:

Python 3.9+

### 1. Clone the Repository
Clone this project to your local machine.

Bash

git clone https://your-repository-url/sql-bot.git
cd sql-bot
### 2. Set Up a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

Bash

# Create a virtual environment
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
### 3. Install Dependencies
Install all the required Python packages from the requirements.txt file.

Bash

pip install -r requirements.txt
### 4. Download the Ollama Model
Pull the llama3.1:8b model so the application can use it.

Bash

ollama pull llama3.1:8b
Ensure the Ollama application is running in the background.

### 5. Run the Application
Launch the Streamlit app.

Bash

streamlit run app.py
Your web browser should automatically open to the application's URL.

## 📖 How to Use
Select a Data Source: Use the sidebar on the left to choose how you want to provide data.

Connect to MySQL: Enter your database credentials and click "Connect".

Upload a File: Upload a CSV or XLSX file, give your data a table name, and click "Load Data".

Provide Schema Text: Paste one or more CREATE TABLE statements and click "Set Schema".

View Schema: Once a data source is configured, you can expand the "View Current Schema" section to see the tables and columns the bot is aware of.

Chat with the Bot: Type your question into the chat input at the bottom of the page.

Ask a question about your data (e.g., "What is the average rating?").

Provide a SQL query for the bot to explain.

Ask a general knowledge question.

Get Results: The bot will respond with the generated SQL, an explanation, and an illustrative example. If you have a live database connection, it will also execute the query and display the results in a table.

## 📁 Project Structure
The project is organized into a main application file and a utils directory for modular, reusable code.

sql-bot/
├── utils/
│   ├── __init__.py           # Makes 'utils' a Python package
│   ├── database.py         # Handles all database connections
│   ├── file_processor.py   # Processes uploaded CSV/XLSX files
│   └── llm_handler.py        # Contains all LLM prompt and API logic
├── app.py                    # The main Streamlit application file
├── requirements.txt          # A list of all Python dependencies
└── README.md                 # This file
