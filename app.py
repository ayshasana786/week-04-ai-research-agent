from graph import graph


def main():
    print("=" * 60)
    print("🤖 AI Research Agent using LangGraph")
    print("=" * 60)

    while True:
        question = input("\nEnter your research question (or type 'exit'): ")

        if question.lower() == "exit":
            print("\n👋 Thank you for using AI Research Agent!")
            break

        initial_state = {
            "question": question,
            "search_results": "",
            "final_answer": "",
            "reasoning": "",
            "sources": []
        }

        result = graph.invoke(initial_state)

        print("\n" + "=" * 60)
        print("🧠 AGENT REASONING")
        print("=" * 60)
        print(result["reasoning"])

        print("\n" + "=" * 60)
        print("📚 SOURCES USED")
        print("=" * 60)

        if result["sources"]:
            for source in result["sources"]:
                print("✔", source)
        else:
            print("No external sources used.")

        print("\n" + "=" * 60)
        print("📄 FINAL SUMMARY")
        print("=" * 60)
        print(result["final_answer"])


if __name__ == "__main__":
    main()