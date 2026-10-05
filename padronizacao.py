"""
Módulo padronizacao.py
Responsável por padronizar nomes de espécies de plantas em DataFrames Pandas.
"""

import pandas as pd


def padroniza_especie(df: pd.DataFrame, coluna: str = "especie") -> pd.DataFrame:
    """Padroniza a coluna de espécies: converte para minúsculas, remove espaços

    nas pontas e substitui caracteres especiais/underline por texto limpo.
    """
    df_limpo = df.copy()

    # 1. Converte para minúsculas
    # 2. Remove espaços em branco no início e no fim (.strip)
    # 3. Remove underlines e caracteres não alfanuméricos/espaços usando regex
    df_limpo[coluna] = (
        df_limpo[coluna]
        .astype(str)
        .str.lower()
        .str.strip()
        .str.replace(r"[^\w\s]|_", "", regex=True)
    )

    return df_limpo