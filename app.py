import os
import streamlit as st
from langchain_groq import ChatGroq

#----PAGE CONFIGURATION----#
st.set_page_config(page_title="Groq AI ChatBot", page_icon="🐱")

st.title("🐱Groq AI ChatBot")
st.write("Ask me anything about Python, Data Science, or AI!")

#----SIDEBAR----#
st.sidebar.header("⚙️ Settings")   

api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.0)

model = st.sidebar.selectbox(
    "Select Model",
    ["llama-3.3-70b-versatile"]
)

#----USER INPUT----#
user_input = st.text_area("🗨️ Your Question:")

#----GENERATE RESPONSE----#
if st.button("Generate Response"):

    if not api_key:
        st.error("⚠️ Please enter your Groq API Key")
    elif not user_input:
        st.warning("⚠️ Please enter a question to ask")
    else:
        try:
            os.environ["GROQ_API_KEY"] = api_key

            groq_chat = ChatGroq(
                model=model,
                temperature=temperature 
            )

            with st.spinner("Generating response..."):
                response = groq_chat.invoke(user_input)

            st.success("Response:")
            st.write(response.content)

        except Exception as e:
            st.error(f"Error: {str(e)}")