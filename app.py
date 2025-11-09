import streamlit as st

def AI_insurance_assistance():
    st.title("AI Insurance Assistance")

    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
    if uploaded_file and "pdf_chunks" not in st.session_state:
        st.success("PDF processed and ready!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask your insurance-related question here...")

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = "Here is a placeholder response to your insurance question."

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    AI_insurance_assistance()