import os
import openai

api_key = os.environ.get('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')

def interactuar_con_chatGPT(consulta):
    openai.api_key = api_key
    mensajes = [
        {"role": "user", "content": "You: " + consulta}
    ]
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=mensajes,
        temperature=1,
        max_tokens=150,
        stop=["\n", "You:", "chatGPT:"]
    )
    print("chatGPT:", respuesta.choices[0].message['content'])

def main():
    while True:
        consulta = input("Ingrese su consulta: ")
        if consulta.strip():
            print("You:", consulta)
            interactuar_con_chatGPT(consulta)
        else:
            print("Por favor, ingrese una consulta válida.")

if __name__ == "__main__":
    main()