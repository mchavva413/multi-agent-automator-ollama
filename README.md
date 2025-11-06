# 🤖 Multi-Agent Workflow Automator

> **Offline AI Automation Framework** built using **Ollama** and **Streamlit**, where multiple local AI agents (Researcher, Writer, Reviewer) collaborate to generate complete, polished content — without any external API calls.

---

## 🚀 Project Overview

This project demonstrates how you can **automate an entire workflow**, not just a single task — from research to writing and review — using local Large Language Models (LLMs) via **Ollama**.

### 🧩 Workflow
1. **Researcher Agent** – Generates concise, factual insights about a topic.  
2. **Writer Agent** – Expands those insights into a 400-word structured article.  
3. **Reviewer Agent** – Polishes the article for grammar, clarity, and tone.  

Each step runs automatically and sequentially inside your local environment.

---

## 🖼️ User Interface (Streamlit)

The app features a clean **corporate-style dashboard** built with Streamlit.

### 💼 UI Features
- Sidebar navigation (`🏠 Dashboard`, `ℹ️ About`, `⚙️ Settings`)
- Step-by-step progress display
- Real-time agent logs and results
- Download button for the final article (`.txt`)
- Custom corporate theme (blue & white)
- Supports multiple local models (`llama3`, `mistral`, `phi3`, etc.)

---

## 🧰 Tech Stack

| Component | Description |
|------------|--------------|
| **Language** | Python 3.11 |
| **UI Framework** | Streamlit |
| **LLM Runtime** | Ollama (runs local LLMs like `llama3`, `mistral`, etc.) |
| **Agents** | Custom-built logic (no external APIs) |
| **OS Compatibility** | macOS / Linux / Windows |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone this Repository
```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-workflow-automator.git
cd multi-agent-workflow-automator
2️⃣ Create a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# or
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install streamlit duckduckgo-search
4️⃣ Pull the Model
Make sure Ollama is installed:
➡️ https://ollama.com/download

Then pull a model:

bash
Copy code
ollama pull llama3
5️⃣ Run the App
bash
Copy code
streamlit run app.py
Visit the local URL (usually http://localhost:8501) to open the dashboard.

🧠 Example Workflow
Input topic:

yaml
Copy code
AI in Education 2025
Agents execute:

🔍 Researcher → Finds insights about the topic

✍️ Writer → Expands into a full draft

🧠 Reviewer → Refines and polishes

Output:
A fully formatted, publication-ready article generated offline.

💾 Project Structure
bash
Copy code
multi-agent-workflow-automator/
│
├── agents.py          # Agent logic (researcher, writer, reviewer)
├── main.py            # Terminal-based execution
├── app.py             # Streamlit dashboard
├── .gitignore         # Ignored files (venv, cache, etc.)
└── README.md          # This file
🌐 Future Enhancements
✅ Functional Settings tab (real-time model selection)

🧠 Add vector-based memory for persistent context

📊 Analytics dashboard for agent performance

🧾 Export to PDF with styling and metadata

🗣️ Optional voice input and summary output

👩‍💻 Author
Chavva Akshit
💼 AI Automation Developer & Research Enthusiast
📧 [your.email@example.com]
🌐 [LinkedIn / Portfolio link if you want to add later]

🪪 License
This project is released under the MIT License — feel free to fork, modify, and use it for educational or commercial purposes.
