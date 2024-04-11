# run the app using 
# streamlit run image_recog.py

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

api_key = os.getenv('GOOGLE-API-KEY')
genai.configure(api_key=api_key)


## Gemini Pro Model
model = genai.GenerativeModel('gemini-pro-vision')

def model_response(question, image):
    if question:
        res = model.generate_content([question,image])
    else:
        res = model.generate_content(image)
    return res.text

st.set_page_config('Gemini Pro - Get Your Queries Solved')
st.header('Gemini Pro - Find the info Associated with the Image You Upload!')
input = st.text_input('Query Box: ',key='Type your Query Here.')
upload_image = st.file_uploader('Upload an Image !',type=['jpeg','png'])
image = ''


if upload_image is not None:
    img = Image.open(upload_image)
    st.image(img, caption='uploaded image')

submit = st.button('Explore the Image')

if submit:
    response = model_response(input,img)
    st.write(response)