# Autor: Antonio Betancourt

import json

with open("usuarios.json", "r", encoding="utf-8") as archivo:
    usuarios = json.load(archivo)

deporte = input("Ingrese el deporte a buscar: ") # Los deportes son: Fútbol, Baloncesto, Ajedrez, Gimnasia, Natación, Voleibol, Atletismo

print("\nPersonas que practican", deporte + ":")
encontro = False

for usuario in usuarios.values():
    if deporte in usuario["deportes"]:
        print(usuario["nombres"], usuario["apellidos"])
        encontro = True

if not encontro:
    print("No se encontraron personas que practiquen ese deporte.")

print("\nAhora buscaremos por rango de edad.") # Las edades son: 19, 25, 22, 28, 31
edad_min = int(input("Ingrese la edad mínima: "))
edad_max = int(input("Ingrese la edad máxima: "))

print("\nPersonas entre", edad_min, "y", edad_max, "años:")
encontro = False

for usuario in usuarios.values():
    if edad_min <= usuario["edad"] <= edad_max:
        print(usuario["nombres"], usuario["apellidos"])
        encontro = True

if not encontro:
    print("No se encontraron personas en ese rango de edad.")
