from math import pi, sqrt
import requests
#test


def exercice1(a, b):
	if type(a) != int or type(b) != int:
		raise ValueError
	return a*b


def exercice2(x, a, b):
	if x<a:
		return -255
	elif a<x<b:
		return x
	elif x>b:
		return 255


class Exercice3:

	def __init__(self, r):
		if type(r) != int or r < 0:
			raise  ValueError
		self.r = r

	def aire(self):
		return pi * (self.r**2)

	def perimetre(self):
		return 2 * pi * self.r

	def dans_cercle(self, x, y):
		d = sqrt((x**2)+(y**2))
		return d < self.r


class Exercice4:
	"""
	Ecrire une classe qui renvoie des informations sur un lieu
	"""

	def __init__(self):
		self.S = requests.Session()
		self.URL = "https://en.wikipedia.org/w/api.php"

	def localisation(self, searchWord):

		PARAMS = {
			"action": "query",
			"format": "json",
			"prop": "pageimages|pageterms",
			"titles": searchWord,
			"formatversion": "2"
		}
		R = self.S.get(url=self.URL, params=PARAMS)
		DATA = R.json()
		return DATA["query"]["pages"][0]["terms"]["description"]

	def getDescription(self, data):
		return data["query"]
