# app.py
# Corporate-Style Multi-Agent Workflow Automator (Offline + Ollama)
# Clean white UI with blue accents, progress bar, and download feature

import streamlit as st
import subprocess
from io import BytesIO
import time

# --------------------------------------------------------------------
# Run Ollama locally
def run_ollama(prompt: str, model: str = "llama3") -> str:
    """Send a prompt to the local Ollama model and return the result."""
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8").strip()

# --------------------------------------------------------------------
# Agent steps
def researcher_step(topic: str) -> str:
    prompt = (
        f"You are a research analyst. Generate three key factual insights about '{topic}'. "
        "Each insight should be concise, data-backed, and unique."
    )
    return run_ollama(prompt)

def writer_step(research: str) -> str:
    prompt = (
        "Using the following research insights, write a 400-word article "
        "with an introduction, 3 structured sections, and a conclusion. "
        "Keep it professional, factual, and readable.\n\n"
        f"{research}"
    )
    return run_ollama(prompt)

def reviewer_step(draft: str) -> str:
    prompt = (
        "Edit the following article for grammar, clarity, and flow. "
        "Ensure it reads like a publication-ready piece.\n\n"
        f"{draft}"
    )
    return run_ollama(prompt)

# --------------------------------------------------------------------
# 🎨 Corporate Theme Styling
st.set_page_config(
    page_title="Multi-Agent Workflow Automator",
    layout="centered",
    page_icon="🤖"
)

st.markdown(
    """
    <style>
        body {
            background-color: #f9fafc;
            color: #0d1b2a;
            font-family: 'Inter', sans-serif;
        }
        .stApp {
            background-color: #f9fafc;
        }
        h1, h2, h3 {
            color: #003566;
        }
        .stTextInput > div > div > input {
            border: 1px solid #cfd8dc;
            border-radius: 8px;
            background-color: white;
            color: #0d1b2a;
            padding: 10px;
        }
        .stButton > button {
            background-color: #0077b6;
            color: white;
            font-weight: 600;
            border-radius: 8px;
            padding: 0.75em 2em;
            border: none;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #00b4d8;
            color: #023047;
        }
        .stProgress > div > div {
            background-color: #0077b6 !important;
        }
        .block-container {
            padding-top: 2rem;
        }
        hr {
            border: 0;
            border-top: 1px solid #e0e0e0;
            margin: 25px 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------
# 🧠 App Layout
st.title("🤖 Multi-Agent Workflow Automator")
st.caption("**AI Agents:** Researcher → Writer → Reviewer")
st.markdown("---")

topic = st.text_input("📘 Enter a topic", placeholder="e.g., The Future of AI in Healthcare")

if st.button("🚀 Run Workflow"):
    if not topic.strip():
        st.warning("⚠️ Please enter a topic first.")
    else:
        progress = st.progress(0)
        status_text = st.empty()
        st.markdown("---")

        # Step 1 — Research
        status_text.markdown("🔍 **Researching...**")
        progress.progress(25)
        time.sleep(0.5)
        research = researcher_step(topic)
        st.subheader("📊 Research Summary")
        st.write(research)

        # Step 2 — Writing
        status_text.markdown("✍️ **Writing article...**")
        progress.progress(55)
        time.sleep(0.5)
        draft = writer_step(research)
        st.subheader("📝 Draft Article")
        st.write(draft)

        # Step 3 — Review
        status_text.markdown("🧠 **Reviewing and polishing...**")
        progress.progress(85)
        time.sleep(0.5)
        final = reviewer_step(draft)
        st.subheader("✅ Final Polished Article")
        st.success("Workflow completed successfully!")
        st.write(final)
        progress.progress(100)

        # Download button
        st.markdown("---")
        st.info("💾 Save your final article:")
        text_bytes = final.encode("utf-8")
        file_buffer = BytesIO(text_bytes)

        st.download_button(
            label="⬇️ Download Final Article (.txt)",
            data=file_buffer,
            file_name=f"{topic.replace(' ', '_')}_final.txt",
            mime="text/plain",
        )

# Footer
st.markdown("---")
st.caption("© 2025 | Multi-Agent Workflow Automator • Powered by Ollama & Streamlit")

