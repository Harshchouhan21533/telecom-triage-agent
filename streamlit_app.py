import streamlit as st
import requests

st.set_page_config(page_title="Telecom AI Agent", layout="centered")

st.title("📡 Telecom Support AI Agent")
st.write("Chat with AI for telecom issues")

# Session ID (for memory)
session_id = st.text_input("Session ID", value="123")

# Chat history display
if "chat" not in st.session_state:
    st.session_state.chat = []

# User input
user_input = st.text_input("Enter your query:")

if st.button("Send"):
    if user_input:
        url = "http://127.0.0.1:8000/triage"

        payload = {
            "query": user_input
        }

        params = {
            "session_id": session_id
        }

        try:
            response = requests.post(url, json=payload, params=params)
            data = response.json()

            bot_reply = data.get("response", "No response")

            # Save chat
            st.session_state.chat.append(("You", user_input))
            st.session_state.chat.append(("Bot", bot_reply))

        except Exception as e:
            st.error(f"Error: {e}")

# Display chat
st.subheader("💬 Conversation")

for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")