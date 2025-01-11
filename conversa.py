# Importar librerías necesarias
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

# Inicializar el modelo
def iniciar_bot(api_key: str):
    # Configurar el modelo y la memoria
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",  # Puedes usar "gpt-4" si tienes acceso
        openai_api_key=api_key,
        temperature=0.7
    )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation = ConversationChain(llm=llm, memory=memory)
    return conversation

# Función principal
def main():
    import getpass

    # Solicitar la API key
    api_key = getpass.getpass("Introduce tu API key de OpenAI: ")

    # Iniciar el bot
    bot = iniciar_bot(api_key)

    print("Bot: ¡Hola! Soy tu asistente virtual.")
    nombre = input("Bot: ¿Cómo te llamas? ")
    print(f"Bot: ¡Encantado de conocerte, {nombre}!")

    # Iniciar la conversación
    while True:
        user_input = input(f"{nombre}: ")
        if user_input.lower() in ["salir", "adiós"]:
            print("Bot: ¡Hasta luego! Que tengas un gran día.")
            break
        respuesta = bot.run(f"{nombre} dice: {user_input}")
        print(f"Bot: {respuesta}")

if __name__ == "__main__":
    main()