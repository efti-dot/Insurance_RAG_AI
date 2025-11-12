import streamlit as st
from main import process_pdf, query_pdf
from prompt import OpenAIConfig
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Please check the OPENAI_API_KEY.")

ai = OpenAIConfig(api_key=api_key)

def AI_insurance_assistance():
    st.title("AI Insurance Assistance")

    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
    if uploaded_file and "pdf_chunks" not in st.session_state:
        st.session_state.pdf_chunks = process_pdf(uploaded_file)
        st.success("PDF processed and ready!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask anything about the uploaded PDF")

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = query_pdf(user_input, st.session_state.messages)

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    AI_insurance_assistance()