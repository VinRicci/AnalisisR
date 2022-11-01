import requests
from play import Play
from data import Data
from mongo import Mongo
from random import choice

mongo = Mongo()

url = "https://rock-paper-scissors7.p.rapidapi.com/"

querystring = {"choice": choice(["rock", "paper", "scissors"])}
headers = {
	"X-RapidAPI-Key": "66e45b6164mshba07b33ab8d0c1cp15f551jsn2a58eeca9fa2",
	"X-RapidAPI-Host": "rock-paper-scissors7.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
resultado = response.json()

usuario = Play(resultado['user']['name'], resultado['user']['beats'])
ia = Play(resultado['ai']['name'], resultado['ai']['beats'])

data_juego = Data(usuario, ia, resultado['result'])
mongo.ingresarDatos(data_juego)
