# workflow_graph.py
from langgraph.graph import StateGraph
from agents import researcher, writer, reviewer

graph = StateGraph()

graph.add_node("research", researcher)
graph.add_node("write", writer)
graph.add_node("review", reviewer)

graph.add_edge("research", "write")
graph.add_edge("write", "review")

graph.set_entry_point("research")

