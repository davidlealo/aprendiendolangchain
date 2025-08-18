import os
from langchain.chat_models import ChatOpenAI

def get_openai_api_key():
    """
    Obtiene la API key de OpenAI desde la variable de entorno o solicita al usuario que la ingrese.

    Returns:
        str: API key de OpenAI.
    """
    # Intentar obtener la API key desde la variable de entorno
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("No se encontró la API key de OpenAI en las variables de entorno.")
        api_key = input("Por favor, ingresa tu API key de OpenAI: ").strip()
    
    return api_key

def main():
    """
    Programa principal que utiliza la API key de OpenAI para interactuar con el modelo de LangChain.
    """
    # Obtener la API key
    openai_api_key = get_openai_api_key()

    # Configurar el modelo
    try:
        llm = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=openai_api_key)
        print("Modelo configurado correctamente.")
    except Exception as e:
        print(f"Error al configurar el modelo: {e}")
        return

    # Ejemplo de interacción con el modelo
    while True:
        prompt = input("\nEscribe tu mensaje (o 'salir' para terminar): ")
        if prompt.lower() == "salir":
            print("¡Hasta luego!")
            break
        try:
            response = llm.predict(prompt)
            print(f"\nRespuesta:\n{response}")
        except Exception as e:
            print(f"Error al interactuar con el modelo: {e}")

if __name__ == "__main__":
    main()
