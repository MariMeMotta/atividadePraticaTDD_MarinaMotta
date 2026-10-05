"""
Módulo data_cleaner.py
Responsável pelo pipeline de limpeza e validação dos dados de sensores IoT.
"""

import math

class DataCleaner:
    @staticmethod
    def remover_nulos_e_nan(dados: list) -> list:
        """Remove valores None e NaN da lista de dados."""
        if not isinstance(dados, list):
            raise TypeError("A entrada deve ser uma lista.")
        
        return [
            v for v in dados 
            if v is not None and not (isinstance(v, float) and math.isnan(v))
        ]

    @staticmethod
    def filtrar_intervalo_temperatura(dados: list, min_temp: float = 0.0, max_temp: float = 50.0) -> list:
        """Filtra leituras anômalas de temperatura fora de um intervalo válido."""
        dados_limpos = DataCleaner.remover_nulos_e_nan(dados)
        return [t for t in dados_limpos if min_temp <= t <= max_temp]

    @staticmethod
    def normalizar_umidade(dados: list) -> list:
        """Garante que leituras de umidade estejam estritamente entre 0.0 e 100.0%."""
        dados_limpos = DataCleaner.remover_nulos_e_nan(dados)
        return [max(0.0, min(100.0, float(u))) for u in dados_limpos]