# run the app using 
# streamlit run app.py

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai


api_key = os.getenv('GOOGLE-API-KEY')
genai.configure(api_key=api_key)


## Gemini Pro Model
model = genai.GenerativeModel('gemini-pro')

def model_response(question):
    res = model.generate_content(question)
    return res.text

st.set_page_config('Gemini Pro - Get Your Queries Solved')
st.header('Gemini Pro - Get Your Queries Solved')
input = st.text_input('Query Box: ',key='Type your Query Here.')
submit = st.button('Send')

if submit:
    response = model_response(input)
    st.write(response)