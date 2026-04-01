# 🤖 Agentic AI Assistant for Real-Time Problem Solving

An intelligent **multi-agent AI assistant** built using **Groq + Gemini APIs** that can solve real-time problems, debug code, and analyze files using a scalable agent-based architecture.

---

## 🚀 Features

* ⚡ Ultra-fast responses using Groq API
* 🧠 Advanced reasoning using Gemini API
* 🤖 Multi-Agent Architecture (Planner + Specialized Agents)
* 🛠️ Code debugging assistant
* 📂 File analysis (CSV, PDF, TXT)
* 📊 Data insights using Pandas
* 💬 Chat memory support
* 🧩 Modular and scalable design

---

## 🧠 Problem Statement

Developers, students, and data professionals often face challenges such as:

* Debugging code efficiently
* Extracting insights from files (PDF, CSV, TXT)
* Switching between multiple tools for different tasks
* Lack of real-time intelligent assistance
* Time-consuming manual analysis

---

## 💡 Solution

This project solves these problems by building a **Multi-Agent AI System** that:

* Uses a **Planner Agent** to understand user intent
* Routes tasks to specialized agents (Code, Data, File, General)
* Leverages **Groq for speed ⚡** and **Gemini for reasoning 🧠**
* Processes uploaded files and provides context-aware responses
* Combines multiple capabilities into a unified intelligent assistant

---

## 🏗️ Project Architecture

```
agentic-ai-assistant/
│
├── app.py
├── .gitignore
├── requirements.txt
├── .env (not pushed)
│
├── agents/
│   ├── planner_agent.py      # Main decision maker
│   ├── code_agent.py         # Code debugging
│   ├── data_agent.py         # Data analysis
│   ├── file_agent.py         # File processing
│   └── general_agent.py      # General queries
│
├── models/
│   ├── gemini_model.py
│   └── groq_model.py
│
├── tools/
│   ├── code_debugger.py
│   ├── file_analyzer.py
│   └── data_agent.py
│
├── utils/
│   ├── memory.py
│   └── helpers.py
│
└── prompts/
    └── agent_prompt.py
```

---

## ⚙️ Tech Stack

* Python
* Streamlit
* Groq API
* Google Gemini API
* Pandas
* PyPDF2

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment

This project is deployed using Streamlit Cloud.

### Steps:

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Create new app
4. Select your repo and `app.py`
5. Add secrets (API keys)
6. Deploy 🚀

---

## 💯 Key Highlights

* Multi-Agent AI System with task-specific agents
* Real-time intelligent responses
* Modular and scalable architecture
* Handles multiple tasks in a single platform
* File-aware and context-aware assistant

---

## 🚀 Future Enhancements

* 🔄 AI-based planner (LLM decision making)
* 🎤 Voice-based interaction
* 🌐 Web search integration
* 🧠 Vector database memory (FAISS)
* 🤖 Advanced multi-agent collaboration

---

## 📬 Contact

For any queries, reach out via GitHub.

📧 Email: [pandugaanjali2003@gmail.com](mailto:pandugaanjali2003@gmail.com)
🔗 GitHub: https://github.com/AnjaliPanduga

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
