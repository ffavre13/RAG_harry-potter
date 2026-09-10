import streamlit as st
from retrieval import search
from generation import generate_response
from main import init

@st.cache_resource
def get_collection():
    return init()

collection = get_collection()

st.title("Harry Potter RAG")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
question = st.chat_input("Ask a question about Harry Potter movies...")
if question:

    st.session_state.messages.append({"role": "user", "content": question})
    
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Retrieving answer..."):
            results = search(question, collection)
            answer = generate_response(question, results)
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})