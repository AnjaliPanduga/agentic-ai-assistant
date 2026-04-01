import streamlit as st
from agents.planner_agent import planner_agent
from tools.file_analyzer import analyze_file
from tools.data_agent import analyze_data
from utils.memory import add_memory, get_memory, clear_memory

st.set_page_config(page_title="Agentic AI Assistant", layout="wide")

st.title("🤖 Agentic AI Assistant")
st.write("Real-Time Problem Solving using Groq + Gemini")

# Sidebar
st.sidebar.title("⚙️ Options")

if st.sidebar.button("Clear Chat"):
    clear_memory()

uploaded_file = st.sidebar.file_uploader("Upload CSV / PDF / TXT")

# 🔥 Store file content (IMPORTANT FIX)
file_content = None

# File Handling
if uploaded_file:
    st.subheader("📂 File Analysis")

    if uploaded_file.name.endswith(".csv"):
        result = analyze_data(uploaded_file)
        st.json(result)
        file_content = str(result)   # ✅ pass structured data to agent

    else:
        result = analyze_file(uploaded_file)
        st.text(result)
        file_content = result        # ✅ pass file text to agent

# Chat Input
user_input = st.chat_input("Ask anything...")

# 🔥 FIX: pass file_content to agent
if user_input:
    response = planner_agent(user_input, file_content)

    add_memory(user_input, response)

# Chat Display
for chat in get_memory():
    with st.chat_message("user"):
        st.write(chat["user"])

    with st.chat_message("assistant"):
        st.write(chat["bot"])