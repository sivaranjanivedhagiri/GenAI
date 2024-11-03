from dotenv import load_dotenv
load_dotenv() # loading the env key

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
# Function to load the Gemini pro model and get response.
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# initialize our streamlit application
st.header("Gemini LLM aplication")

input = st.text_input("Input : ", key="input" )
submit = st.button("Ask the question ")

# when submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader('The response is ')
    st.write(response)


