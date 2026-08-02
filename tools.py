from ddgs import DDGS
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun


def clean_query(query: str) -> str:
    """
    Clean the user's query before searching.
    """
    query = query.lower()

    words_to_remove = [
        "what is",
        "who is",
        "what are",
        "who are",
        "explain",
        "define",
        "tell me about"
    ]

    for word in words_to_remove:
        query = query.replace(word, "")

    query = query.replace("?", "").strip()

    return query


def search_wikipedia(query: str) -> str:
    """
    Search Wikipedia using LangChain.
    """
    try:
        query = clean_query(query)

        wikipedia = WikipediaQueryRun(
            api_wrapper=WikipediaAPIWrapper(
                top_k_results=1,
                doc_content_chars_max=1200
            )
        )

        result = wikipedia.invoke(query)

        print("\n========== WIKIPEDIA RESULT ==========")
        print(result)

        return result

    except Exception as e:
        print("\nWikipedia Error:", e)
        return ""


def search_duckduckgo(query: str) -> str:
    """
    Search DuckDuckGo and return top search results.
    """
    try:
        query = clean_query(query)

        output = ""

        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        if not results:
            print("\nNo DuckDuckGo results found.")
            return ""

        print("\n========== DUCKDUCKGO RESULT ==========")

        for result in results:
            title = result.get("title", "")
            body = result.get("body", "")[:300]  # Limit body length
            url = result.get("url", "")

            output += f"Title: {title}\n"
            output += f"Body: {body}\n"

            if url:
                output += f"URL: {url}\n"

            output += "\n"

        print(output)

        return output

    except Exception as e:
        print("\nDuckDuckGo Error:", e)
        return ""