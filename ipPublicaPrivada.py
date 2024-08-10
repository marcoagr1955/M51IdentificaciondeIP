import socket

import requests


def obtener_ip_privada():

    hostname = socket.gethostname()

    ip_privada = socket.gethostbyname(hostname)

    return ip_privada


def obtener_ip_publica():

    try:

        respuesta = requests.get('https://api.ipify.org?format=json')

        respuesta.raise_for_status()  # Lanza un error si la solicitud no fue exitosa

        ip_publica = respuesta.json()['ip']

        return ip_publica

    except requests.RequestException as e:

        return f"Error al obtener la IP pública: {e}"


ip_publica = obtener_ip_publica()

print(f"Tu dirección IP pública es: {ip_publica}")


ip_privada = obtener_ip_privada()

print(f"Tu dirección IP privada es: {ip_privada}")