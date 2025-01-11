from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.runnables.history import RunnableWithMessageHistory

def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = input("Por favor, ingresa tu API key de OpenAI: ").strip()
    return api_key

def main():
    openai_api_key = get_openai_api_key()
    llm = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=openai_api_key)

    # Memoria con límite de 10 interacciones
    memory = ConversationBufferWindowMemory(k=10)
    conversation = RunnableWithMessageHistory(llm=llm, memory=memory)

    print("Modelo configurado correctamente.")
    while True:
        prompt = input("\nEscribe tu mensaje (o 'salir' para terminar): ")
        if prompt.lower() == "salir":
            print("¡Hasta luego!")
            break
        response = conversation.invoke(prompt)
        print(f"\nRespuesta:\n{response}")

if __name__ == "__main__":
    main()
