from turtle import pd
import unittest
import importlib
import sys

##Garantir que a função imputa_umidade_media(df) preencha os valores nulos 
#exclusivamente com a média da umidade daquela mesma espécie de planta, e não a média geral.

self.sensor_de_umidade = importlib.import_module('sensor_de_umidade')

####################################################################################


##Garantir que a função imputa_umidade_media(df) preencha os valores nulos 
#exclusivamente com a média da umidade daquela mesma espécie de planta, e não a média geral.

class TestSensorDeUmidade(unittest.TestCase):
    def setUp(self):
        # Dynamically import the sensor_de_umidade module
        self.sensor_de_umidade = importlib.import_module('sensor_de_umidade')

    def test_sensor_de_umidade(self):
        for i in df.index:
         if pd.isnull(df.loc[i, 'i']):
                print(media)

##########################################################################


class TestSensorDeUmidade(unittest.TestCase):
    def setUp(self):
        # Dynamically import the sensor_de_umidade module
        self.sensor_de_umidade = importlib.import_module('sensor_de_umidade')

    def test_sensor_de_umidade(self):
        for i in df.index:
         if pd.isnull(df.loc[i, 'i']):
                print(media)

i = float(input("Digite a umidade: "))
especie = input("Digite a espécie da planta: ")
media = especie.mean(i) 

