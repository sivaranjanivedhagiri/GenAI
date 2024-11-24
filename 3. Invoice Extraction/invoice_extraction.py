# from dotenv import load_dotenv
# load_dotenv() # load all the environment variables from .env

# import streamlit as st
# import os
# from PIL import Image

# import google.generativeai as genai
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # function to load the gemini pro vision
# model = genai.GenerativeModel('gemini-pro-vision')


# def get_gemini_response(input, image, prompt):
#     response = model.generate_content([input, image[0], prompt])
#     return response.text

# def input_image_setup():
#     if upload_file is not None:
#         # Read the files into bytes
#         bytes_data = upload_file.getvalue()
#         image_parts = [
#             {
#                 "mine_type":upload_file.type,
#                 "data":bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         raise FileNotFoundError('No file uploaded')
    

# # initiate our streamlit application
# st.set_page_config(page_title="Multi language Invoice Extractor")
# st.header("Multi language Invoice Extractor")
# input = st.text_input('Input Prompt : ', key="input")

# upload_file = st.file_uploader("Choose an image of the invoice ..", type=['jpg','jpeg','png'])
# image = ''

# if upload_file is not None:
#     image = Image.open(upload_file)
#     st.image(image, caption="Uploaded Image.", use_column_width=True)

# submit = st.button('Tell me about the invoice')

# input_prompt = """
#     You are in expert in understanding invoice. We will upload a image as invoice 
#     and you need to answer any questions based on uploaded invoice image     
# """
# #If submit button is clicked
# if submit:
#     image_data = input_image_setup(upload_file)
#     response = get_gemini_response(input_prompt, image_data, input)
#     st.subheader('The response is')
#     st.write(response)



# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input,image[0],prompt])
    return response.text
    

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image.
               """

## If ask button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)