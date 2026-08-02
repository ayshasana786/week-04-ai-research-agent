from typing import TypedDict


class AgentState(TypedDict):
    # User's question
    question: str

    # Combined search results
    search_results: str

    # Final summarized response
    final_answer: str

    # Agent's reasoning or status
    reasoning: str

    # Sources used for research
    sources: list