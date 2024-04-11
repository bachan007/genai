from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai

from speech_to_text import speech_to_text
from text_to_speech import text_to_speech

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

def get_gemini_response(que,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt,que])
    return response.text

prompt = """
I am assigning you a name, i.e., Jarvis.

I request you:
Do not use ** in the text
"""

# question = speech_to_text()
question = 'ek lambi romantic shayri sunao'
print(question)

answer = get_gemini_response(question,prompt)
print(answer)

text_to_speech(answer)