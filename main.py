import requests
from play import Play
from data import Data
from mongo import Mongo
from random import choice
from archivocsv import Archivocsv

mongo = Mongo()
csv = Archivocsv()

for i in range(1):
	url = "https://rock-paper-scissors7.p.rapidapi.com/"

	querystring = {"choice": choice(["rock", "paper", "scissors"])}
	headers = {

	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	resultado = response.json()
	usuario = Play(resultado['user']['name'], resultado['user']['beats'])
	ia = Play(resultado['ai']['name'], resultado['ai']['beats'])

	data_juego = Data(usuario, ia, resultado['result'])
	mongo.ingresarDatos(data_juego)
	csv.insert(data_juego)
