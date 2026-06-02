# chat.py
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

llm = ChatOllama(model="llama3.2", temperature=0.7)

history = [
    SystemMessage(content="You are a helpful assistant. Be concise and clear.")
]

print("Chat with Llama 3.2 (type 'quit' to exit)\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Goodbye!")
        break

    if not user_input:
        continue

    history.append(HumanMessage(content=user_input))

    # Streaming — words print as they arrive
    print("\nAssistant: ", end="", flush=True)
    full_response = ""

    for chunk in llm.stream(history):
        word = chunk.content
        print(word, end="", flush=True)
        full_response += word

    print("\n")  # newline after response finishes

    # Save the complete response to history
    history.append(AIMessage(content=full_response))
