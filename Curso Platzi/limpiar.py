import nbformat

# Nombre del archivo que quieres limpiar
notebook_path = "notebook_1_modelos_prompts_y_cadenas_333eebfc-c9ab-4201-91b8-d7b1a14ec5d3.ipynb"
output_path = "notebook_limpio.ipynb"

# Cargar notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Si existen metadatos de widgets, eliminarlos
if "widgets" in nb["metadata"]:
    print("Eliminando metadata.widgets...")
    del nb["metadata"]["widgets"]

# También podrías limpiar las salidas de las celdas si lo deseas:
for cell in nb.get("cells", []):
    if "outputs" in cell:
        cell["outputs"] = []
    if "execution_count" in cell:
        cell["execution_count"] = None

# Guardar notebook limpio
with open(output_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Notebook limpio guardado en: {output_path}")
