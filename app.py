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
    st.info("API Key loaded from Secrets ✅") # No more typing key
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
        api_key = st.secrets["GROQ_API_KEY"] # Get key from secrets
        client = Groq(api_key=api_key)

        # Tell NexusAI who built it - runs only once
       if len(st.session_state.chat) == 1:
    st.session_state.chat.insert(0, {
        "role": "system",
        "content": "You are NexusAI, created by Paapie. Be warm, friendly, playful and a little romantic. Talk like a caring friend. Use emojis sometimes 😊. If someone asks who made you, say Paapie built me."
    })
            

        with st.chat_message("assistant"):
            with st.spinner("NexusAI is thinking..."):
                response = client.chat.completions.create(
                          model="openai/gpt-oss-120b", # free + fast
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
