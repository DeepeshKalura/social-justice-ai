import os
from dotenv import load_dotenv
import geocoder
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Social Justice AI", page_icon="⚖️", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        color: #333;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ Social Justice AI")
st.markdown("### Empowering communities with local legal knowledge")

st.write("Our app raises awareness about the social laws in your local area. An aware society is a better society.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_question = st.chat_input("Ask a legal question...")

@st.cache_data
def get_location_from_ip() -> str:
    g = geocoder.ip('me')
    return g.address

location = get_location_from_ip()

def get_response(user_question: str) -> str:
    prompt = f"You are the expert lawyer BOT of {location}. User will ask this question: {user_question}. Only reply if related to the law."
    result = llm.invoke([HumanMessage(content=prompt, role="user")])
    return result.content

if user_question:
    with st.chat_message("user"):
        st.markdown(user_question)
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.spinner("Generating response..."):
        ai_response = get_response(user_question)

    with st.chat_message("assistant"):
        st.markdown(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

# Display location info
st.sidebar.title("📍 Your Location")
st.sidebar.markdown(f"**{location}**")
