import os
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

def get_openai_api_key():
    """
    Obtiene la API key de OpenAI desde una variable de entorno o la solicita al usuario.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = input("Ingresa tu OpenAI API key: ").strip()
    return api_key

def main():
    openai_api_key = get_openai_api_key()

    # Configuración del modelo y memoria
    print("Configurando modelo y memoria...")
    llm = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=openai_api_key)
    memory = ConversationBufferWindowMemory(k=10)
    conversation = ConversationChain(llm=llm, memory=memory)

    print("Modelo configurado correctamente.\n")
    print("Escribe tu mensaje (o 'salir' para terminar):")

    while True:
        prompt = input("> ")
        if prompt.lower() == "salir":
            print("¡Hasta luego!")
            break
        try:
            response = conversation.run(input=prompt)
            print(f"\nRespuesta:\n{response}\n")
        except Exception as e:
            print(f"Error: {str(e)}")
            break

if __name__ == "__main__":
    main()
