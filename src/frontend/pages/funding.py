import streamlit as st
import requests
import json

st.set_page_config(page_title="Funding", layout="centered")

st.title("💬 Chatbot powered by Groq & LangChain")

RolesNum = {
    "4": "Detailed Cost Estimator",
    "5": "Pitch PPT Generator",
    "6": "Investor & Event Locator",
    "7": "Term Sheet Analyzer",
}

# Dropdown for selecting role

selected_role_key = st.selectbox("Select an Funding Role:", list(RolesNum.values()))
selected_role = selected_role_key

keyArray = [key for key, val in RolesNum.items() if val == selected_role]
roleVariable = keyArray[0]
st.write(roleVariable)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    url = 'http://localhost:8001/api/v1/chatgroq'
    myobj = {'role': '1', 'msg': user_input}
    response = requests.post(url, json = myobj)
    response = response.json()[0].strip('["]')

    print("here", type(response[0]))
    st.session_state.messages.append({"role": "assistant", "content":  response})
    
    with st.chat_message("assistant"):
        st.markdown(response)
