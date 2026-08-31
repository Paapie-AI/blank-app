import streamlit as st
from groq import Groq

st.set_page_config(page_title="NexusAI", page_icon="🧠", layout="centered")
st.title("🧠 NexusAI")
st.caption("Your AI Assistant by Paapie")

api_key = st.text_input("Enter your Groq API Key", type="password", placeholder="gsk_...")

if api_key:
    try:
        client = Groq(api_key=api_key)
    except Exception as e:
        st.error(f"Invalid API Key: {e}")
        st.stop()
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask NexusAI anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("NexusAI is thinking..."):
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=st.session_state.messages,
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

else:
    st.info("👆 Paste your free Groq API Key above to start chatting")
    st.link_button("Get Free Groq Key", "https://console.groq.com/keys")
