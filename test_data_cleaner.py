import unittest
import importlib
import sys

class TestDataCleaner(unittest.TestCase):
        # Dynamically import the data_cleaner module
    self.data_cleaner = importlib.import_module('data_cleaner')

##############################################################################

class TestDataCleaner(unittest.TestCase):
    def setUp(self):
        # Dynamically import the data_cleaner module
        self.data_cleaner = importlib.import_module('data_cleaner')
    if __name__ == '__main__':
        unittest.main()

    else:
        # If the module is imported, run the tests
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
        raise SystemExit(0)  # Prevents the script from exiting after tests are run

importlib.reload(self.data_cleaner)  # Reload the module to ensure the latest version is used 
def data_cleaner():
        # Dynamically import the data_cleaner module
    self.data_cleaner = importlib.import_module('data_cleaner')  # Re-import the module after reloading

def cleanup_module():
    """
    Cleanup the data_cleaner module by removing it from sys.modules.
    This ensures that the next import will load a fresh version of the module.
    """
    if 'data_cleaner' in sys.modules:
        del sys.modules['data_cleaner']

    
############################################################################

import unittest
from data_cleaner import DataCleaner


class TestDataCleaner(unittest.TestCase):

    def test_remover_nulos_e_nan(self):
        dados_corrompidos = [22.5, None, 25.0, float('nan'), 19.8]
        esperado = [22.5, 25.0, 19.8]
        resultado = DataCleaner.remover_nulos_e_nan(dados_corrompidos)
        self.assertEqual(resultado, esperado)

    def test_filtrar_intervalo_temperatura(self):
        # Temperaturas extremas causadas pela tempestade solar (-50, 150)
        leituras = [22.0, -50.0, 35.5, 150.0, 18.2]
        esperado = [22.0, 35.5, 18.2]
        resultado = DataCleaner.filtrar_intervalo_temperatura(leituras, min_temp=0.0, max_temp=50.0)
        self.assertEqual(resultado, esperado)

    def test_normalizar_umidade(self):
        umidades = [-10.0, 45.0, 105.0, 80.0]
        esperado = [0.0, 45.0, 100.0, 80.0]
        resultado = DataCleaner.normalizar_umidade(umidades)
        self.assertEqual(resultado, esperado)

    def test_entrada_invalida_gera_excecao(self):
        with self.assertRaises(TypeError):
            DataCleaner.remover_nulos_e_nan("entrada_invalida_string")


if __name__ == '__main__':
    unittest.main()