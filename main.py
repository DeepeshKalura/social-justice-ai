import os
from dotenv import load_dotenv
import geocoder
import streamlit as st 
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()


llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))




st.title("Social Justice AI")

st.write("Our app aware people about the social law of the local area. The aware society can make the better society.")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    

if user_question := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(user_question)
    st.session_state.messages.append({"role": "user", "content": user_question})



@st.cache_data
def get_location_from_ip()->str:
    g = geocoder.ip('me')
    location = g.address
    return location


location:str = get_location_from_ip()


def get_response(user_question:str)->str:
    prompt = f"You are the expert lawer BOT of this {location}. User will ask this question {user_question}."
    result = llm.invoke([HumanMessage(content=prompt, role="user")])
    return result.content
    
    

ai_response = get_response(user_question)

response = ai_response
with st.chat_message("assistant"):
    st.markdown(response)
st.session_state.messages.append({"role": "assistant", "content": response})
