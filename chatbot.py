from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq


load_dotenv();

st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)
st.title("💬 Generative AI ChatBoat")


# iniciate chat 

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

# show chat history

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.chat_message(message["content"])

        # import llm model
llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.1
)

user_input=st.chat_input("Ask question..")


if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role":"user","content":user_input})

    response=llm.invoke(
        input=[{"role":"assistant","content":"you are a helpful assistant"}, *st.session_state.chat_history]
    )

    response_assistant=response.content
    st.session_state.chat_history.append({"role":"assistant","content":response_assistant})

    with st.chat_message("assistant"):
        st.markdown(response_assistant)
    



