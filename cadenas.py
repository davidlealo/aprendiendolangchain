from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI

# Crear prompt y modelo
template = PromptTemplate(
    input_variables=["tema"],
    template="Explícame {tema} en términos sencillos."
)
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Crear cadena
chain = LLMChain(llm=llm, prompt=template)
respuesta = chain.run(tema="física cuántica")
print(respuesta)
