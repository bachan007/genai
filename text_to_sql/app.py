from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

def get_gemini_response(que,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt,que])
    return response.text

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    for row in rows:
        print(row)
    return rows

prompt = """
You are an expert in Converting English Queries into SQL queries.
I have an sql database named employees where columns are employee_id, first_name, last_name, job_title, hire_date, salary and datatypes for columns are INT, VARCHAR(50),VARCHAR(50),VARCHAR(100),DATE, Decimal(10,2).
Example1. If i want to know how many employees are there in the table, i will write the query like "SELECT COUNT(employee_id) FROM EMPLOYEES"
Example2. If i want to select all records from the table, i will write the query like "SELECT * FROM EMPLOYEES"
Example3. If i want to select all records from the table where job_title is 'Data Scientist', i will write the query like "SELECT * FROM EMPLOYEES where job_title='Data Scientist'"
Example4. If i want to select job_title wise salary, i will write the query like "SELECT job_title,sum(salary) FROM EMPLOYEES group by job_title"

Above are the only Examples you need to generate the SQL queries according to the question.
So give me the sql queries like above in return when you get a question in english language.

Provide only SQL query, Do not return ``` or **SQL Query:** in response.
"""

st.set_page_config(page_title='Ask me the question in English, i will retrieve the SQL Query')
st.header('Ask me the question in English, i will retrieve the SQL Query')
question = st.text_input("Input: ", key='input')
submit = st.button('Give it a Try.')

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,'employees.db')
    st.subheader(f'Your Query Returned with SQL Query:\n{response}')
    for row in data:
        print(row)
        st.header(row)