from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["nombre"],
    template="Hola, {nombre}. ¿En qué puedo ayudarte?"
)
prompt = template.format(nombre="David")
print(prompt)  # "Hola, David. ¿En qué puedo ayudarte?"
