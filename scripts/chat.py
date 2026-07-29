from src.rag_pipeline import answer_question


def main():
    print("=" * 50)
    print("Engineering AI Copilot")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:
        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        answer = answer_question(question)

        print("\nAI:\n")
        print(answer)


if __name__ == "__main__":
    main()