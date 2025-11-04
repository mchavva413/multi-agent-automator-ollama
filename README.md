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

