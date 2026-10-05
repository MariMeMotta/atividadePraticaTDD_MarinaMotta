import unittest
import importlib
import sys



def setUp(self):
        # Dynamically import the validacao_temperatura module


 def remove_outliers_temperatura(self, data):
        if (temperatura < -20 or temperatura > 60):
           return self.assertNotIsInstance
    
#################################################################################

import unittest
import importlib
import sys



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

#####################################################################

"""
Módulo test_validacao_temperatura.py
Suíte de testes automatizados para o módulo validacao_temperatura.py.
"""

import unittest
from validacao_temperatura import validar_temperatura, remover_outliers_temperatura


class TestValidacaoTemperatura(unittest.TestCase):

    def test_temperatura_valida(self):
        # Temperaturas dentro do limite (-20 a 60) devem retornar True
        self.assertTrue(validar_temperatura(25.0))
        self.assertTrue(validar_temperatura(-20.0))
        self.assertTrue(validar_temperatura(60.0))

    def test_temperatura_outlier_invalida(self):
        # Temperaturas fora do limite devem retornar False
        self.assertFalse(validar_temperatura(-25.0))
        self.assertFalse(validar_temperatura(100.0))

    def test_remover_outliers_de_lista(self):
        # Remove anomalias trazidas pela tempestade solar
        leituras_sensor = [22.5, -35.0, 18.0, 75.0, 0.0]
        esperado = [22.5, 18.0, 0.0]
        
        resultado = remover_outliers_temperatura(leituras_sensor)
        self.assertEqual(resultado, esperado)

    def test_tipo_de_dado_invalido_gera_excecao(self):
        # Garante que dados corrompidos como strings disparam exceção
        with self.assertRaises(TypeError):
            validar_temperatura("trinta_graus")


if __name__ == '__main__':
    unittest.main()





