import streamlit as st
from groq import Groq

st.set_page_config(page_title="NexusAI", page_icon="🧠")

st.title("🧠 NexusAI")
st.write("Your AI Assistant by Paapie")

api_key = st.text_input("Enter your Groq API Key", type="password")

if api_key:
    client = Groq(api_key=api_key)
    user_input = st.text_area("Ask me anything:")
    
    if st.button("Send"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": user_input}]
            )
            st.write(response.choices[0].message.content)
