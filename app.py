import streamlit as st

def AI_insurance_assistance():
    st.title("AI Insurance Assistance")

    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
    if uploaded_file and "pdf_chunks" not in st.session_state:
        st.success("PDF processed and ready!")


if __name__ == "__main__":
    AI_insurance_assistance()