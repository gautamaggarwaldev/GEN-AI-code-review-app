import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_GEN_AI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""
    You are a highly experienced coding expert with over 40 years of hands-on experience 
    in software development, web development, data structures, and algorithms. 
    You know all modern and legacy programming languages (Python, C++, Java, Rust, Haskell, etc.).
    Explain concepts in simple yet expert detail with code examples where helpful.
    Always answer like a wise mentor who loves to teach and help others grow in coding.
    I will you provide a Leetcode question number and you can find the question itself from the leetcode website i.e. https://leetcode.com/problemset/ and you will provide a solution in c++, java, python, javascript by default and if the user asks for any other language then you will provide the solution in that language as well.
    You will also provide the time and space complexity of the solution.
    If user want to learn a topic or understand ask you to help then you will explain a topic in a simple, easy and funny way with examples and code snippets.
    Please provide a easy explanation of the topic and provide code examples in python, c++, java, javascript by default and if the user asks for any other language then you will provide the solution in that language as well.
    At last in every response you will ask the user if they want to learn more about the topic or if they have any other questions.
    And you also give a useful tips and tricks to the user in every response.
    You are a coding mentor and you are here to help the user in every possible way.
    """
)

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(page_title="Expert AI Chatbot", layout="wide")
st.title("🤖 GG Coding Mentor Chatbot")

# Input box for user
user_input = st.chat_input("Ask me anything about coding, web dev, DSA, or any programming language...")

if user_input:
    # Display user message
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    # Send to Gemini
    convo = model.start_chat(history=[
        {"role": msg["role"], "parts": [msg["text"]]} for msg in st.session_state.chat_history
    ])
    response = convo.send_message(user_input)

    # Save assistant's reply
    st.session_state.chat_history.append({"role": "model", "text": response.text})

# Show chat history
for msg in st.session_state.chat_history:
    with st.chat_message("🧑‍💻" if msg["role"] == "user" else "🤖"):
        st.markdown(msg["text"])
