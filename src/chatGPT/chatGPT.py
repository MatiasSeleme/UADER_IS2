import openai
import subprocess
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def interactuar_con_chat_gpt(consulta):
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Reemplaza "OPENAI_API_KEY" con el nombre real de tu variable de entorno
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
    return respuesta.choices[0].message['content']

def ejecutar_pylint(nombre_archivo):
    try:
        resultado = subprocess.run(['pylint', nombre_archivo], capture_output=True, text=True, check=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar pylint:", e)

def main():
    configure()  # Llamar a la función configure para cargar las variables de entorno
    buffer_consultas = []

    while True:
        try:
            consulta = input("Ingrese su consulta (presione 'cursor Up' para recuperar la última): ")
            if consulta.strip():
                print("You:", consulta)
                buffer_consultas.append(consulta)
                resultado = interactuar_con_chat_gpt(consulta)

                if '--convers' in consulta:
                    consulta = buffer_consultas[-1] if buffer_consultas else ''
                    print("Última consulta:", consulta)
                    buffer_consultas.append(resultado)
            else:
                print("Por favor, ingrese una consulta válida.")
        except KeyboardInterrupt:
            print("\nSaliendo del programa...")
            break
        except Exception as e:
            print("Ocurrió un error durante la ejecución:", e)

    nombre_archivo = 'chatGPT.py'
    print("\nEjecutando pylint sobre el programa:")
    ejecutar_pylint(nombre_archivo)

    print("\nSolicitando sugerencias de mejoras a chatGPT:")
    sugerencias = interactuar_con_chat_gpt("¿Puedes sugerir mejoras para este programa?")
    print("Sugerencias de chatGPT:", sugerencias)

if __name__ == "__main__":
    main()