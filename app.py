import streamlit as st
from config import MODEL
from Tutors.base_tutor import pythonClassBot
from Chatbot.engine import ChatBot
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

st.set_page_config(page_title = "Python class Tutor")
st.title('Python class Bot')
st.markdown(""" 
This app is built using python OOP concepts: 
The concepts include:
-Encapsulation
-Inheritance
-Abstraction
-Polymorphism                
"""
)

if not api_key:
    st.info("Please update your api key in .env file")
    st.stop()

# Creating Objects
tutor = pythonClassBot()
chat_engine = ChatBot(api_key = api_key, model = MODEL)

#Initialize chat history

if "messages" not in st.session_state:
    chat_engine.add_system_message(tutor.get_system_prompt())
    chat_engine.add_assistant_message(tutor.greet())
    st.session_state.messages = chat_engine.messages

# Displaying chat messages

for message in st.session_state.messages[1:]:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Taking user input

if prompt:= st.chat_input("Ask anything about oops concepts... "):
    with st.chat_message("user"):
        st.markdown(prompt)

    #Streaming
    with st.chat_message('assistant'):
        response = st.write_stream(chat_engine.get_streaming_response(prompt))