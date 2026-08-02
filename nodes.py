import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from state import AgentState
from tools import search_wikipedia, search_duckduckgo

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def planner_node(state: AgentState) -> AgentState:
    """
    Planner Node
    Receives the user's question and prepares the research process.
    """

    question = state["question"]

    print("\n📌 Planner Node")
    print("Question:", question)

    state["reasoning"] = "Planning the research process."
    state["sources"] = []

    return state


def research_node(state: AgentState) -> AgentState:
    """
    Research Node
    Searches multiple sources and stores the collected information.
    """

    question = state["question"]

    print("\n🔍 Researching...")

    wiki_result = search_wikipedia(question)
    duck_result = search_duckduckgo(question)

    combined_results = ""

    if wiki_result:
        state["sources"].append("Wikipedia")

        combined_results += (
            "========== WIKIPEDIA ==========\n"
            f"{wiki_result}\n\n"
        )

    if duck_result:
        state["sources"].append("DuckDuckGo")

        combined_results += (
            "========== DUCKDUCKGO ==========\n"
            f"{duck_result}\n"
        )

    if not combined_results:
        combined_results = "No research results found."

    state["search_results"] = combined_results

    state["reasoning"] = (
        f"Collected information from {len(state['sources'])} source(s)."
    )

    return state


def summary_node(state: AgentState) -> AgentState:
    """
    Summary Node
    Generates the final summarized response.
    """

    prompt = f"""
You are an AI Research Assistant.

User Question:
{state["question"]}

Research Results:
{state["search_results"]}

Sources Used:
{", ".join(state["sources"]) if state["sources"] else "No external sources"}

Instructions:
- If research results are available, summarize them clearly.
- If research results are not available, answer naturally using your general knowledge.
- Keep the response concise, accurate, and well structured.
- Use headings and bullet points when appropriate.
"""

    print("\n📝 Summarizing...")

    response = llm.invoke(prompt)

    state["final_answer"] = response.content

    return state