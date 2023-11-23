import re

respuestas = {
    r"(Hola|Hola!|Hola.)": "¡Hola! ¿En qué puedo ayudarte?",
    r"(Como estas\??|Como estas\?|Como va todo\??|Como va todo\?)": "Estoy bien, gracias por preguntar.",
    r"(Adiós|Hasta luego|Nos vemos|Chao|Bye)": "¡Hasta luego! Que tengas un buen día.",
}

def responder_mensaje(mensaje):
    for patron, respuesta in respuestas.items():
        if re.search(patron, mensaje, re.IGNORECASE):
            return respuesta
    return "Lo siento, no entendí. ¿Podrías reformular tu pregunta?"

print("¡Hola! Soy un chatbot simple. Puedes preguntarme lo que quieras o decir 'Adiós' para terminar.")
while True:
    user_input = input("Tú: ")
    if user_input.lower() in ['adios', 'hasta luego', 'chao', 'bye']:
        print(responder_mensaje(user_input))
        break
    else:
        respuesta = responder_mensaje(user_input)
        print("Chatbot:", respuesta)
