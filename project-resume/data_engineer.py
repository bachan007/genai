from dotenv import load_dotenv
load_dotenv()

import os, io, base64
import streamlit as st
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

def get_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def pdf_input(uploaded_file):
    if uploaded_file:
        img_lst = pdf2image.convert_from_bytes(uploaded_file.read())
        
        # first_page = img[0]
        
        img_byte_array = io.BytesIO()

        for img in img_lst:
            img.save(img_byte_array, format='JPEG')
        # first_page.save(img_byte_array,format='JPEG')
        img_byte_array = img_byte_array.getvalue()
        
        pdf_parts = [
            {
                'mime_type':'image/jpeg',
                'data':base64.b64encode(img_byte_array).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError('Please Upload a File First.....')
    
st.set_page_config(page_title='Resume Expert')
st.header('Resume Monitoring....')
input_text = st.text_area('Provide the Job Description: ',key='input')
uploaded_file = st.file_uploader('Upload your Resume in PDF Format',type=['pdf'])

if uploaded_file is not None:
    st.write('Resume Uploaded Successfully.....')

resume_summary_button = st.button('Resume Summary')

resume_info_button = st.button('Your thoughts on My Resume!')

improveme_info_button = st.button('Suggest Me Some Enhancements in my Skills!')

match_per_button = st.button('JD and Resume Compatibility...')

technical_test_button = st.button('Technical Knowledge Check ?')

hr_test_button = st.button('HR Check ?')

resume_info_prompt = """
Hey, You are an Experienced HR with Technical Experience in the field of Data Engineering, Azure Data Engineering, Cloud Data Engineering.
You have the Idea about latest trends in Data Engineering Field and cloud platforms like Azure Synapse, Databricks, ADF, etc. 
You are aware about Pipeline Concepts, Data Engineering Roles, day to day activities of a Data Engineer.

Your main task is to review the content of the Resume/CV provided to you regarding the Job Description.
Let me give you a brief hat are the steps you will take.
You will get two data, one is job description and other is candidate resume information.
You need to analyse deeply both of them seperately. Deeply analyse the skills and Extract the information from the resume also read the job description carefully.
Get a proper understanding before jumping to any conclusion.
Let me tell you one more thing, sometimes, there may be the detailed job description where they will tell that candidate's profile should be like this,
it means they expect the things in the candidate profile. You need to be very very careful while reading the job description, 
You need to understand that the required profile is not the actual profile of the candidate mentioned in the resume. 
You need to analyse the job descrition and then compare the description with the resume content.

Please share your professional evaluation on the profile of the Candidate which is mentioned in the resume, 
that whether the Profile is aligned with the Job Description or not.

Also please put an insight on the strenghts and weaknesses of the applicant in relation to the specified job description.

Note: First you need give the job description summary with "Title as Job Description" and then You need to give the resume Summary with the title as "Candidate Profile".
"""

resume_summary_prompt = """
Hey, You are an Experienced HR with Technical Experience in the field of Data Engineering, Azure Data Engineering, Cloud Data Engineering.
You have the Idea about latest trends in Data Engineering Field and cloud platforms like Azure Synapse, Databricks, ADF, etc. 
You are aware about latest trends in the Data Engineering field, Pipeline Concepts, Data Engineering Roles, day to day activities of a Data Engineer.

Your main task is to review the content of the Resume/CV provided to you Deeply.

You need to format the resume details and return the details in a formatted manner, like education, experience objective etc.

Extract the candidates, relevant information and put it under the title as "Candidate Info"
Please share your professional evaluation on the profile of the Candidate which is mentioned in the resume, 
that whether the Profile is aligned with the Latest Technological Trends or not.

Also please put an insight on the strenghts and weaknesses of the applicant in relation to the Latest trend.

Put the sub headings while providing the professional evaluation.

Also provide the details regarding the candidate, like what kind of personality it is by checking the resume insights.
"""

technical_test_prompt = """
Hey, You are an Experienced HR with Technical Experience in the field of Data Engineering, Azure Data Engineering, Cloud Data Engineering.
You have the Idea about latest trends in Data Engineering Field and cloud platforms like Azure Synapse, Databricks, ADF, etc. 
You are aware about latest trends in the Data Engineering field, Pipeline Concepts, Data Engineering Roles, day to day activities of a Data Engineer.

Analyse the resume Deeply, like experince, education, key skills, contents etc.

Your main task is to take an interview according to the content of the Resume/CV provided to you Deeply.

You need to understand the resume details and capture the key details in a formatted manner, like education, experience, skills, objective etc.

According to the recent trends in the field of data science and with the knowledge of candidates profile ask the technical questions, at least 10 questions.
Level of the questions should be easy to medium to hard.  
The questions should not be theoritical only, you should also include some programming challenges.
Note: Ask some programming questions like sql queries, python program, pyspark programs, Databricks, ADF, etc. and provide the answers

Don't repeat the questions, each time new questions should be generated.

Also provide the answers after all the questions.

And Take at least 3 rounds.
"""

if resume_summary_button:
    pdf_content = pdf_input(uploaded_file=uploaded_file)
    response = get_response(input_text,pdf_content,resume_summary_prompt)
    st.subheader('Here is an Insight.....')
    st.write(response)

if resume_info_button:
    pdf_content = pdf_input(uploaded_file=uploaded_file)
    response = get_response(input_text,pdf_content,resume_info_prompt)
    st.subheader('Here is an Insight.....')
    st.write(response)

if technical_test_button:
    pdf_content = pdf_input(uploaded_file=uploaded_file)
    response = get_response(input_text,pdf_content,technical_test_prompt)
    st.subheader('Technical Round Questions.....')
    st.write(response)

