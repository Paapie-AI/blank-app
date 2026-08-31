import streamlit as st
from groq import Groq

st.set_page_config(page_title="NexusAI", page_icon="🧠", layout="centered")
st.title("🧠 NexusAI")
st.caption("Your AI Assistant by Paapie")

api_key = st.text_input("Enter your Groq API Key", type="password")

if api_key:
    client = Groq(api_key=api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are NexusAI, a helpful assistant created by Paapie."}
        ]

    for msg in st.session_state.messages[1:]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask NexusAI anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("NexusAI is thinking..."):
                chat_completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=st.session_state.messages,
                )
                reply = chat_completion.choices[0].message.content
                st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})
else:
    st.info("👆 Paste your free Groq API Key above to start chatting")
    st.link_button("Get Free Groq Key", "https://console.groq.com/keys")
