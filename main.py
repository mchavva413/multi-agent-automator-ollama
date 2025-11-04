# main.py
# Runs the 3-step offline multi-agent workflow using Ollama (llama3)

from agents import researcher_step, writer_step, reviewer_step

def run_workflow(topic: str):
    print(f"\n🚀 Starting Multi-Agent Workflow for topic: {topic}\n")

    # Step 1 – Research
    research = researcher_step(topic)
    print("\n📘 Research Summary:\n", research)

    # Step 2 – Write
    draft = writer_step(research)
    print("\n📝 Draft Article:\n", draft)

    # Step 3 – Review
    final = reviewer_step(draft)
    print("\n✅ FINAL POLISHED ARTICLE:\n", final)


if __name__ == "__main__":
    try:
        topic = input("Enter a topic: ").strip()
        if not topic:
            print("⚠️ Please enter a topic and try again.")
        else:
            run_workflow(topic)
    except KeyboardInterrupt:
        print("\n🛑 Interrupted. Exiting.")

