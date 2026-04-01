# 🤖 Agentic AI Assistant for Real-Time Problem Solving

An intelligent multi-model AI assistant built using **Groq + Gemini APIs** that can solve real-time problems, debug code, and analyze files using a modular agent-based architecture.

---

## 🚀 Features

* ⚡ Ultra-fast responses using Groq API
* 🧠 Advanced reasoning using Gemini API
* 🛠️ Code debugging assistant
* 📂 File analysis (CSV, PDF, TXT)
* 📊 Data insights using Pandas
* 🧠 Intelligent agent decision-making
* 💬 Chat memory support
* 🧩 Modular architecture (scalable & clean)

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

This project solves these problems by building an **Agentic AI system** that:

* Understands user queries intelligently
* Routes tasks to the best model (Groq for speed ⚡, Gemini for reasoning 🧠)
* Processes uploaded files and gives context-aware answers
* Combines multiple capabilities (chat, debugging, analysis) into one system
* Acts as a unified AI assistant for real-world problem solving

---

## 🏗️ Project Architecture

```
agentic-ai-assistant/
│
├── app.py                  # Streamlit UI
├── .gitignore                   
├── requirements.txt
├── .env (not pushed)
├── agents/
│   └── main_agent.py       # Decision-making logic
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

* Multi-model AI system (Groq + Gemini)
* Real-time intelligent responses
* Modular and scalable architecture
* Handles multiple tasks in one system
* File-aware AI assistant

---

## 🚀 Future Enhancements

* 🔄 Auto tool selection (true agent behavior)
* 🎤 Voice-based interaction
* 🌐 Web search integration
* 🧠 Vector database memory (FAISS)
* 🤖 Multi-agent collaboration system

---

## 📬 Contact

For any queries, reach out via GitHub.

📧 Email: pandugaanjali2003@gmail.com

🔗 GitHub: https://github.com/AnjaliPanduga


---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
