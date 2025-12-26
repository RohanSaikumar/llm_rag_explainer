import streamlit as st
from ragchain import rag_chain, Chroma_database_creation
from langchain_core.messages import HumanMessage, AIMessage
import json
import os
from dotenv import load_dotenv

load_dotenv(override = True)
folder_path = os.getenv("DOCS_PATH")

st.set_page_config(
    page_title="LLM Architecture Explainer",
    page_icon="🧠",
    layout="wide"
)

@st.cache_resource
def get_retriever():
    return Chroma_database_creation(folder_path)

retriever = get_retriever()

rag_chain = rag_chain(retriever)

st.title("LLM Architecture Explainer")
if 'responses' not in st.session_state:
    st.session_state['responses'] = []
if 'requests' not in st.session_state:
    st.session_state['requests'] = []
if "input" not in st.session_state:
    st.session_state["input"] = ""



textcontainer = st.container()

chat_history = []

with textcontainer:
    query = st.chat_input("Query: ", key="input")
    st.markdown(st.session_state["responses"][0]["content"])

    if query:
        with st.spinner("Generating response..."):
            st.success('Done!')
            answer = rag_chain.invoke({"input": query, "chat_history": chat_history})
            chat_history.extend([HumanMessage(content=query),AIMessage(content=answer)])
            st.session_state["requests"].append({"role": "user", "content": query})
            st.session_state["responses"].append({"role": "assistant", "content": answer})
        

response_container = st.container()
with response_container:
    for i in range(len(st.session_state["responses"])):
        with st.chat_message(st.session_state["responses"][i]["role"]):
            st.markdown(st.session_state["responses"][i]["content"])

    

##make streamlit better
##finalise the app
##github push
