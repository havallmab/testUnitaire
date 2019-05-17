import unittest
from unittest.mock import MagicMock
import exoUnitaire
from exoUnitaire import Exercice3
from math import pi


class TestStringMethods(unittest.TestCase):

	def testExo1(self):
		self.assertEqual(exoUnitaire.exercice1(3, 4), 3*4)

	def testExo1p2(self):
		self.assertRaises(ValueError, exoUnitaire.exercice1, 3, 'b')

	def testExo2(self):
		self.assertEqual(exoUnitaire.exercice2(5, 3, 4), 255)
		self.assertEqual(exoUnitaire.exercice2(2, 1, 3), 2)
		self.assertEqual(exoUnitaire.exercice2(2, 5, 3), -255)

	def testExo3(self):
		myDisk = Exercice3(5)
		self.assertEqual(myDisk.aire(), pi * (5**2))

	def testExo3p2(self):
		myDisk = Exercice3(3)
		self.assertEqual(myDisk.perimetre(), 2 * pi * 3)
		myDisk = Exercice3(0)
		self.assertEqual(myDisk.perimetre(), 0)

	def testExo3p3(self):
		myDisk = Exercice3(5)
		self.assertEqual(myDisk.dans_cercle(3, 3), True)
		myDisk = Exercice3(1)
		self.assertEqual(myDisk.dans_cercle(5, 3), False)

	def testExo3p4(self):
		self.assertRaises(ValueError, Exercice3, 'b')


if __name__ == '__main__':
	unittest.main()
