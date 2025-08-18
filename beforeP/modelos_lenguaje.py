from langchain_openai.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
respuesta = llm.invoke("¿Qué es LangChain?")
print(respuesta)
