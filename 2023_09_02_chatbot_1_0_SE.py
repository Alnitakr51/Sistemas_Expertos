# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 08:08:33 2023

@author: Gadiel Jimenez
"""
# Base de datos de preguntas y respuestas predefinidas
base_memoria = {
    "Hola": "Hola! ¿Cómo te encuentras?",
    "¿Cómo estás?": "Perfecto, en funcionamiento",
    "Kevin es furro?": "Definitivamente camarada"
}

def pregunta_chat(pregunta):
    respuesta = base_memoria.get(pregunta)

    if respuesta is not None:
        return respuesta
    else:
        nueva_respuesta = input(f"Desconozco la respuesta a '{pregunta}'. ¿Qué debo responder?: ")
        base_memoria[pregunta] = nueva_respuesta
        return "Gracias por la información"

print("Hola, soy Chispa Culpable. Puedes preguntarme lo que quieras.")

while True:
    pregunta = input("Tú: ")

    if pregunta.lower() == "desactivate":
        print("Chispa Culpable: Hasta pronto")
        break
    
    respuesta = pregunta_chat(pregunta)
    print("Chispa Culpable:", respuesta)
