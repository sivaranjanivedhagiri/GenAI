import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

from dotenv import load_dotenv
load_dotenv() # loading the env key


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## FUNCTION TO LOAD THE GEMINI PRO MODEL AND GET RESPONSE.
model = genai.GenerativeModel('gemini-1.5-flash')
#gemini-1.0-pro-vision

def get_gemini_responses(input, image):
    if input != '':
        responses = model.generate_content([input, image])
    else:
        responses=model.generate_content(image)
    return responses.text

#initiate the streamlit application
st.set_page_config(page_title="Gemini image demo")
st.header("Gemini application")
input = st.text_input('Input prompt :', key='Input')

upload_file = st.file_uploader('Choose an image.. ', type = ['png', 'jpeg', 'jpg'])

image = ''

if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded image.", use_column_width=True)

submit = st.button("Tell me about the image")

##if submit is clicked. 
if submit:
    response = get_gemini_responses(input, image)
    st.subheader('The response is')
    st.write(response)

