import streamlit as st
from groq import Groq
st.set_page_config(page_title="NexusAI", page_icon="🧠")
st.title("🧠 NexusAI")
st.write("Hi! I’m NexusAI by Paapie")
api_key = st.sidebar.text_input("Groq API Key", type="password")
if api_key:
    client = Groq(api_key=api_key)
    if "chat" not in st.session_state:
        st.session_state.chat = []
    # Display previous messages
    for msg in st.session_state.chat:
        st.chat_message(msg["role"]).write(msg["content"])
    user_input = st.chat_input("Ask me anything...")
    if user_input:
        # Add user's message
        st.session_state.chat.append({
            "role": "user",
            "content": user_input
        })
        # Display user's message
        st.chat_message("user").write(user_input)
        # Ask Groq
        with st.spinner("Thinking..."):
            try:
                res = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=st.session_state.chat,
                )
                answer = res.choices[0].message.content
                # Save AI response
                st.session_state.chat.append({
                    "role": "assistant",
                    "content": answer
                })
                # Display AI response
                st.chat_message("assistant").write(answer)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
