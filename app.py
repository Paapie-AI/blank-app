import streamlit as st
from groq import Groq
# Page setup
st.set_page_config(
    page_title="NexusAI",
    page_icon="🧠"
)
st.title("🧠 NexusAI")
st.caption("Your AI Assistant by Paapie")
# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = []
# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="gsk_..."
    )
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat = []
        st.rerun()
# Display previous messages
for message in st.session_state.chat:
    with st.chat_message(message["role"]):
        st.write(message["content"])
# ALWAYS show the chat box
user_input = st.chat_input("Ask NexusAI anything...")
# Handle message
if user_input:
    # Make sure API key exists
    if not api_key:
        st.warning("⚠️ Please enter your Groq API Key in the sidebar first.")
        st.stop()
    # Add user's message
    st.session_state.chat.append({
        "role": "user",
        "content": user_input
    })
    # Display user's message
    with st.chat_message("user"):
        st.write(user_input)
    # Connect to Groq
    try:
        client = Groq(api_key=api_key)
        with st.chat_message("assistant"):
            with st.spinner("NexusAI is thinking..."):
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=st.session_state.chat,
                    temperature=0.7,
                    max_tokens=2048
                )
                answer = response.choices[0].message.content
                st.write(answer)
        # Save response
        st.session_state.chat.append({
            "role": "assistant",
            "content": answer
        })
    except Exception as e:
        st.error(f"❌ Error: {e}")
