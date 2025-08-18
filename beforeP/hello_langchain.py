from langchain_openai.chat_models import ChatOpenAI  # Importar el modelo de chat

# Inicializa el modelo (endpoint de chat)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Entrada de texto
texto = "¿Qué es LangChain?"

# Generar respuesta
respuesta = llm.invoke(texto)  # Método correcto para invocar el modelo
print(respuesta)
