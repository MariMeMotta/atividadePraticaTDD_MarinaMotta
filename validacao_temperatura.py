import unittest
import importlib
import sys


temperatura = float(input("Digite a temperatura: "))

class TestValidacaoTemperatura(unittest.TestCase):
    def setUp(self):
        # Dynamically import the validacao_temperatura module
        self.validacao_temperatura = importlib.import_module('validacao_temperatura')

    def remove_outliers_temperatura(self, data):
        self.remove_outliers_temperatura = importlib.import_module('validacao_temperatura')
        if (temperatura < -20 or temperatura > 60):
           return self.assertNotIsInstance
        else:
           return self.assertIsInstance
