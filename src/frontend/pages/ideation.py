import streamlit as st
import requests
import json
import pages.gvars

st.set_page_config(page_title="Ideation", layout="centered")
# i = 1

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)


st.title("Founderella AI Assistance")

# if(pages.gvars.inp and i==1):
#     i=i+1
#     url = 'http://localhost:8001/api/v1/chatgroq'
#     myobj = {'role': '1', 'msg': pages.gvars.inp}
#     response = requests.post(url, json = myobj)
#     response = response.json()[0].strip('["]')
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
#     st.session_state.messages.append({"role": "assistant", "content": response})


RolesNum = {
    "1": "SWOT Analysis",
    "2": "Market Analysis Summarizer",
    "3": "Strategic Roadmap Generator"
}

# Dropdown for selecting role

selected_role_key = st.selectbox("Select an Ideation Role:", list(RolesNum.values()))
selected_role = selected_role_key

keyArray = [key for key, val in RolesNum.items() if val == selected_role]
roleVariable = keyArray[0]

st.write(f"**Selected Role:** {selected_role}")
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
    print("inp: ", pages.gvars.inp)
    myobj = {'role': roleVariable, 'msg': pages.gvars.inp + ", " + user_input}
    response = requests.post(url, json = myobj)
    response = response.json()[0].strip('["]')

    print("here", type(response[0]))
    st.session_state.messages.append({"role": "assistant", "content":  response})
    
    with st.chat_message("assistant"):
        st.markdown(response)
