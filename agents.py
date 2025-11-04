# agents.py
# Local multi-agent workflow using Ollama (llama3)
# Agents: Researcher → Writer → Reviewer

import subprocess, json

# --------------------------------------------------------------------
# 🧩 Ollama helper
def run_ollama(prompt: str, model: str = "llama3") -> str:
    """Send a prompt to a local Ollama model and return the generated text."""
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8").strip()


# --------------------------------------------------------------------
# 🔍 Researcher Step
def researcher_step(topic: str) -> str:
    """Generate 3 factual insights about the topic (offline, no web search)."""
    print("\n🔍 Researching...")
    prompt = (
        f"Provide three key factual insights about '{topic}'. "
        "Each insight should be concise, current, and distinct. "
        "Write as short bullet points (no fluff)."
    )
    return run_ollama(prompt)


# --------------------------------------------------------------------
# ✍️ Writer Step
def writer_step(research: str) -> str:
    """Turn research insights into a structured 400-word article."""
    print("\n✍️ Writing draft...")
    prompt = (
        "Using the following research insights, write a structured 400-word article. "
        "Include an introduction, three key insights as sections, and a conclusion. "
        "Keep the language professional and clear.\n\n"
        f"Research data:\n{research}"
    )
    return run_ollama(prompt)


# --------------------------------------------------------------------
# 🧠 Reviewer Step
def reviewer_step(draft: str) -> str:
    """Polish the text for clarity, grammar, and professional tone."""
    print("\n🧠 Reviewing and polishing...")
    prompt = (
        "Polish this article for clarity, grammar, flow, and conciseness. "
        "Do not change the structure — just improve the writing quality.\n\n"
        f"Draft:\n{draft}"
    )
    return run_ollama(prompt)

