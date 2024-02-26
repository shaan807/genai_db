from dotenv import load_dotenv
load_dotenv()  # load all the environment variables

import streamlit as st
import os
import psycopg2


import google.generativeai as genai

# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function To retrieve query from the database
def read_sql_query(sql, connection_string):
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur. fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# Define Your Prompt
prompt = ["""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS='Data Science'; 
    also the sql code should not have ``` in beginning or end and sql word in output
"""]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# if submit is clicked
if submit:
    sql_query = get_gemini_response(question, prompt)
    print(sql_query)
    # Connection of database
    connection_string = "dbname=query_less user=postgres password=12345678 host=localhost port=5432"
    response = read_sql_query(sql_query, connection_string)
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)


# import os
# import psycopg2
# from dotenv import load_dotenv
# import google.generativeai as genai
# import streamlit as st

# # Load environment variables (ensure GOOGLE_API_KEY is defined)
# load_dotenv()

# # Configure Genai Key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# # Function to get response from Gemini model
# def get_gemini_response(question, prompt):
#     model = genai.GenerativeModel('gemini-pro')
#     try:
#         response = model.generate_content([prompt[0], question])
#         return response.text
#     except Exception as e:
#         return f"Error: {e}"


# # Function to retrieve data from database
# def read_sql_query(sql, connection_string):
#     try:
#         conn = psycopg2.connect(connection_string)
#         cur = conn.cursor()
#         cur.execute(sql)
#         rows = cur.fetchall()
#         conn.commit()
#         conn.close()
#         return rows
#     except Exception as e:
#         print(f"Error: {e}")
#         return None


# # Define prompt
# prompt = ["""
# You are an expert in converting English questions to SQL query!
# The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION 
# \n\nFor example,\nExample 1 - How many entries of records are present?, 
# the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
# \nExample 2 - Tell me all the students studying in Data Science class?, 
# the SQL command will be something like this SELECT * FROM STUDENT 
# where CLASS='Data Science'; 
# also the sql code should not have ``` in beginning or end and sql word in output
# """]

# # Streamlit App configuration
# st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("Gemini App To Retrieve SQL Data")

# # User input
# question = st.text_input("Ask your question about the STUDENT database:", key="input")
# submit = st.button("Ask")

# # Process on submit
# if submit:
#     # Get SQL query from Gemini
#     sql_query = get_gemini_response(question, prompt)
#     st.subheader("Generated SQL Query:")
#     st.write(sql_query)  # Display the generated SQL query

#     if sql_query and sql_query.startswith("SELECT"):
#         # Connect to database and fetch data (only if query is a SELECT statement)
#         connection_string = "dbname=query_less user=postgres password=12345678 host=localhost port=5432"
#         data = read_sql_query(sql_query, connection_string)

#         if data:
#             st.subheader("Data from the database:")
#             for row in data:
#                 st.write(row)  # Display data in a user-friendly format (consider table view)
#         else:
#             st.write("No data found.")
#     else:
#         # Handle non-SELECT queries (e.g., INSERT, UPDATE, DELETE)
#         st.write("This query is not currently supported. Please ask a question that requires retrieving data from the database.")



from dotenv import load_dotenv
load_dotenv()  # load all the environment variables

import streamlit as st
import os
import psycopg2


import google.generativeai as genai

# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    sql_query = response.text
    # Remove the backticks characters from the beginning and end of the SQL query
    sql_query = sql_query[3:-3]
    return sql_query

# Function To retrieve query from the database
def read_sql_query(sql, connection_string):
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
     for row in rows:
        print(row)
    return rows

# Define Your Prompt
prompt = ["""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS='Data Science'; 
    also the sql code should not have ``` in beginning or end and sql word in output
"""]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# if submit is clicked
if submit:
    sql_query = get_gemini_response(question, prompt)
    print(sql_query)
    # Connection of database
    connection_string = "dbname=query_less user=postgres password=12345678 host=localhost port=5432"
    response = read_sql_query(sql_query, connection_string)
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)