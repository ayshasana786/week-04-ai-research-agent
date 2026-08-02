from langgraph.graph import StateGraph, START, END

from state import AgentState
from nodes import planner_node, research_node, summary_node

# Create StateGraph
graph_builder = StateGraph(AgentState)

# Add nodes
graph_builder.add_node("planner", planner_node)
graph_builder.add_node("research", research_node)
graph_builder.add_node("summary", summary_node)


def route_question(state: AgentState):
    """
    Decide whether research is needed.
    """
    question = state["question"].lower().strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if question in greetings:
        return "summary"

    return "research"


# Graph Flow
graph_builder.add_edge(START, "planner")

graph_builder.add_conditional_edges(
    "planner",
    route_question,
    {
        "research": "research",
        "summary": "summary"
    }
)

graph_builder.add_edge("research", "summary")
graph_builder.add_edge("summary", END)

# Compile Graph
graph = graph_builder.compile()