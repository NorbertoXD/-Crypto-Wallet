import requests

from balance import app
from balance.views import *

apikey = "223C305D-FB30-4F3B-A4CC-FB1935013054"
headers = {
    "X-CoinAPI-Key": apikey
} 

moneda_origen = input("¿Que moneda quieres cambiar?")
moneda_destino = input("¿Que moneda deseas obtener?")

url = "http://rest.coinapi.io/v1/exchangerate/{moneda_origen}/{moneda_destino}"
respuesta = requests.get(url, headers=headers)
tipo_cambio = respuesta.json()

cambio = tipo_cambio["rate"]

print("Un {} vale como {:,.2f} {}".format(
    moneda_origen, cambio, moneda_destino,
))
