import streamlit as st
import requests

# Configure the Streamlit page
st.set_page_config(
    page_title="Graphrag - Customer Support",
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

# Page title and caption
st.title("🤖 Customer Support")
st.caption("📞 Reliable & AI-Powered Customer Support")

# Custom CSS for styling
st.markdown(
    """
    <style>
        .main { background-color: #f4f9f9; color: #000000; }
        .sidebar .sidebar-content { background-color: #d1e7dd; }
        .stTextInput textarea { color: #000000 !important; }
        .stSelectbox div[data-baseweb="select"] { color: black !important; background-color: #d1e7dd !important; }
        .stSelectbox svg { fill: black !important; }
        .stSelectbox option, div[role="listbox"] div { background-color: #d1e7dd !important; color: black !important; }
        .stCaption { color: #FF6347 !important; }  /* Tomato color */
        
        /* Align assistant messages to the right */
        .stChatMessage.assistant {
            text-align: right;
            background-color: #d1e7dd;
            color: black;
        }

        /* Ensure the chat messages are contained properly */
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
        }

        .stChatMessage.user {
            background-color: #f1f1f1;
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with features and footer
with st.sidebar:
    st.divider()
    st.markdown("### Customer Support Features")
    st.markdown("""
    - 🤖 AI-Powered Assistance
    - 📞 24/7 Support
    - 📝 Customer Support
    - 🔍 Query Resolution
    """)
    st.divider()
    st.markdown("Built with Gemma API | LangChain")

# Backend API URL
API_URL = "http://127.0.0.1:9999/chat"

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_query = st.chat_input("Enter your query")

if user_query:
    # Append user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    # Send request to backend
    with st.spinner("Thinking..."):
        payload = {"messages": [user_query]}
        response = requests.post(API_URL, json=payload)

    # Handle response
    if response.status_code == 200:
        response_data = response.json()
        agent_response = response_data.get("response", "No response received.")
        st.session_state.chat_history.append({"role": "assistant", "content": agent_response})
    else:
        st.error("Failed to get a response from the server.")

    # Rerun to display updated chat history
    st.rerun()
