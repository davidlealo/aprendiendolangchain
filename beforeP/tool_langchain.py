from langchain.tools import tool

@tool
def calcular(operacion: str) -> str:
    """Realiza una operación matemática básica."""
    return str(eval(operacion))

print(calcular("3 + 5"))  # Resultado: "8"
