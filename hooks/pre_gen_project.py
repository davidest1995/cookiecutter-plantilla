import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
   print(f"{ERROR_COLOR}ERROR: {project_slug=} El título del proyecto no puede empezar por X, hay una restricción.{RESET_ALL}")

   sys.exit(1)

print(f"{MESSAGE_COLOR}Let's go! Se creó una nueva carpeta llamada {project_slug}!")
print(f"Ubicación del proyecto: { os.getcwd() }{RESET_ALL}")