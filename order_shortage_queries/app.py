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
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt = """
Heyy, i am telling you that you are an expert in Converting English Queries into SQL queries.
I have an sql database named orders where i have 3 tables. 
Information about the tables and their columns with their data types are as follows:
table1. orders, with column names order_numbers, items, ordered_qty, delivered_qty and datatypes are object, object, number and number.
table2. correlation_master, with column names items, rca_id and datatypes are object and number.
table3. rca, with column names rca_id, rca and datatypes are object and number.

The 3 tables are correlated to each other.
As orders table contains the order details, correlation_master is the mapping file where those items whose orders could not be fulfilled are mentioned in the items column
and their associated reason id is mentioned in rca_id column, rca table is the mapping file where reasons mentioned in rca_id column of correlation_master are mapped with their explanation,
in rca column.

So here i will give you some idea about the data retrieval technique.
I will give some examples of sql queries:
Example1. If i want to see all the records where orders could not be fulfilled, i will write the query like "SELECT * FROM orders where delivered_qty<ordered_qty"
Example2. If i want to select average ordered_qty of items from the orders table, i will write the query like "SELECT items,avg(ordered_qty) FROM EMPLOYEES group by items"
Example3. If i want to see all records from the orders table where orders could not be fulfilled with their rca_id, i will write the query like 
"select o.order_numbers, o.items, o.ordered_qty, o,delivered_qty, cm.rca_id from (SELECT * FROM orders where delivered_qty<ordered_qty) o
left join correlation_master cm on
upper(o.items) = upper(cm.items)"

Above are the only Examples you need to generate the SQL queries according to the question.
So give me the sql queries like above in return when you get a question in english language.

Things to keep in mind:
when u join using two tables, always do the string formatting like making every record in same case like upper or lower,
and strip the whitespaces if any.
U need to think that edge cases must be handled.
Provide only SQL query, Do not return ``` or **SQL Query:** in response.
"""

st.set_page_config(page_title='Ask me the question in English, i will retrieve the SQL Query')
st.header('Ask me the question in English, i will retrieve the SQL Query')
question = st.text_input("Input: ", key='input')
submit = st.button('Give it a Try.')

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,'orders.db')
    st.subheader(f'Your Query Returned with SQL Query:\n{response}')
    for row in data:
        print(row)
        st.header(row)

# Example Questions
# give me the value of that rca descrioption due to whic most of the orders can not be fulfilled