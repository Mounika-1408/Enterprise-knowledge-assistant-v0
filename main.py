from assistant import initialize_assistant, ask_question

knowledge_base = input("Enter Knowledge Base Folder: ")

retriever = initialize_assistant(knowledge_base)

print("\n========================================")
print("🏢 Enterprise Knowledge Assistant")
print("Type 'exit' to quit.")
print("========================================\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    answer, sources = ask_question(
        retriever,
        question
    )

    print("\n🤖 Answer:\n")
    print(answer)

    print("\n📄 Sources:")

    for source in sources:
        print(source)

    print("\n" + "=" * 60 + "\n")