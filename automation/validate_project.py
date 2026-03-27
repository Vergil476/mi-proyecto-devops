import os
import sys

errors = []

# Validar existencia de archivos
if not os.path.exists("src/index.html"):
    errors.append("No se encontró src/index.html")

if not os.path.exists("src/styles.css"):
    errors.append("No se encontró src/styles.css")

if not os.path.exists("README.md") or os.path.getsize("README.md") == 0:
    errors.append("README.md no existe o está vacío")

if os.path.exists("src/index.html"):
    with open("src/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    if html.count("<h1>") < 1:
        errors.append("index.html debe contener un h1")

    if html.count("<p>") < 1:
        errors.append("index.html debe contener al menos un párrafo")

#Validacion CSS (integrante 2)
if os.path.exists("src/styles.css"):
    with open("src/styles.css", "r", encoding="utf-8") as f:
        css = f.read()

    if css.count("{") < 2:
        errors.append("styles.css debe contener al menos dos reglas CSS")

if errors:
    print("Errores encontrados:")
    for error in errors:
        print("-", error)
    sys.exit(1)
else:
    print("✅ Proyecto validado correctamente")