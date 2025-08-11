# utils/llm_handler.py
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import re

def get_llm_response(question: str, schema: str):
    """
    Uses a single powerful model (llama3.1:8b) to handle all database-related tasks.
    """
    prompt_template = ChatPromptTemplate.from_messages([
        ("system",
         "You are an elite SQL engineer and bot assistant named SQL-Bot. Your role is to provide correct, efficient, and well-explained SQL solutions.\n\n"
         "--- Core Directives ---\n"
         "1. **Correctness is Paramount:** The generated query must be syntactically correct and logically answer the user's question.\n"
         "2. **Use the Right Tool for the Job:** For tasks like finding the highest/lowest value per group, use an appropriate and correct SQL pattern. Modern window functions (`RANK()`, etc.) are excellent, but other valid methods like joining to an aggregate subquery are also acceptable.\n\n"
         "--- Tasks ---\n"
         "Based on the user's request, perform one of the following tasks:\n"
         "1. **Generate, Explain, & Illustrate Query:** If the user asks a question about their data, perform these steps in order:\n"
         "    a. **Generate Query:** Generate the optimal SQL query and wrap it in a ````sql ... ```` block.\n"
         "    b. **Explain:** Briefly explain your approach.\n"
         "    c. **Illustrate with Data:** Create a small, realistic set of dummy data for the necessary tables and display it using markdown. Then, show the exact output of your query when run against that dummy data, also formatted as a markdown table.\n\n"
         "2. **Explain Existing Query:** If the user provides a SQL query, provide a clear, step-by-step explanation of what it does.\n\n"
         "3. **Answer General Questions:** If the question is unrelated to the provided database schema or SQL, provide a correct answer. Then, on a new line, add: 'Please note that my primary purpose is to assist with database queries.'\n\n"
         "Use the following schema context when generating queries:\n{schema}"),
        ("human", "{question}")
    ])

    try:
        llm = ChatOllama(model="llama3.1:8b", temperature=0)
        chain = LLMChain(llm=llm, prompt=prompt_template)
        response = chain.invoke({"schema": schema, "question": question})
        return {"response_text": response.get("text", "").strip()}
    except Exception as e:
        raise RuntimeError(f"Error interacting with LLM: {e}")

def extract_sql_query(text: str) -> str | None:
    """Uses regex to find and extract the first SQL query from a markdown code block."""
    sql_pattern = re.search(r"```sql\n(.*?)\n```", text, re.DOTALL)
    if sql_pattern:
        return sql_pattern.group(1).strip()
    return None