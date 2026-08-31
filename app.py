import streamlit as st
from groq import Groq

st.set_page_config(page_title="NexusAI", page_icon="🧠")
st.title("🧠 NexusAI")
st.write("Your AI Assistant by Paapie")

api_key = st.text_input("Enter your Groq API Key", type="password")

if api_key:
    client = Groq(api_key=api_key)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask NexusAI"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=st.session_state.messages,
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)
