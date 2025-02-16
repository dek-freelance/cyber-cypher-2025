import streamlit as st

st.set_page_config(page_title="Chatbot with Groq & LangChain", layout="wide")

st.sidebar.title("Enhance Your Startup!")
st.sidebar.page_link("pages/ideation.py", label="Ideation", icon="💡")
st.sidebar.page_link("pages/funding.py", label="Funding", icon="💰")
st.sidebar.page_link("pages/tasks.py", label="Tasks", icon="📋")

st.title("Welcome!")
st.write("Select an option from the sidebar to proceed.")
