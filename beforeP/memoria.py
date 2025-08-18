from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai.chat_models import ChatOpenAI

# Crear memoria y cadena de conversación
memory = ConversationBufferMemory()
llm = ChatOpenAI(model="gpt-3.5-turbo")
chain = ConversationChain(llm=llm, memory=memory)

# Conversación
print(chain.run("Hola, ¿cómo estás?"))
print(chain.run("¿Recuerdas cómo te saludé?"))  # LangChain recordará el saludo
