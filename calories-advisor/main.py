from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

def get_gemini_response(prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt,image[0]])
    return response.text

def image_processing(file_upload):
    if file_upload is not None:
        bytes_data = file_upload.getvalue()
        img_parts = [
            {
                'mime_type':file_upload.type,
                'data':bytes_data
            }
        ]
        return img_parts
    else:
        raise FileNotFoundError('No File Uploaded.')
    
st.set_page_config(page_title='Nutrition Expert')
st.header('Nutrition Monitoring....')
uploaded_file = st.file_uploader('Upload your Meal Image.....',type=['jpg','jpeg','png'])

image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption='Uploaded Image')

submit = st.button('Give me the Calorie Details')

prompt1 = """
You need to act as an Expert Nutritionist. You will need to check the food items from the image 
and provide the calorie details, also provide the details of each food item in the image seperately in the format below:

1. Item 1 : Calories in Numbers
2. Item 2 : Calories in Numbers
----
----

You also need to give your expert advice on the food intakes, that whether the food id healthy or not.
Also provide the details of advantages and disadvantages of having the particular food item in the Image.

Like which food contains what, why the food is being eaten, what effects it have, how much one should eat, etc.

If there is health warning regarding the food, please mention it clearly.
"""

prompt2 = """
You need to act as an Expert Dietician.
You possess in-depth knowledge of nutrition, including the latest research and developments in the field.

You need to provide expert advice on a balanced diet.
You will need to check the food items from the image 
 I'm interested in understanding that whether the food items in the image are nutritious and well-rounded. 
 What key principles should I consider, and are there specific dietary guidelines you recommend for someone who is having the meal defined in image?
"""

prompt3 = """
You need to act as an Expert Dietician, who is having experience and in-depth knowledge of nutrition, 
having the idea of bad effects of the food intake.

You main aim is to provide the bad health impact of the food contained in the image.
"""

if submit:
    image_data = image_processing(uploaded_file)
    expert1_gemini_response = get_gemini_response(prompt=prompt1,image=image_data)
    expert2_gemini_response = get_gemini_response(prompt=prompt2,image=image_data)
    expert3_gemini_response = get_gemini_response(prompt=prompt3,image=image_data)

    st.header("Expert Opinion 1.......")
    st.write(expert1_gemini_response)
    st.header("Expert Opinion 2.......")
    st.write(expert2_gemini_response)
    st.header("Expert Opinion 3.......")
    st.write(expert3_gemini_response)