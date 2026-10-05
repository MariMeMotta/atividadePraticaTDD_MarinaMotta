"""
Módulo imputacao_umidade.py
Responsável por imputar valores ausentes de umidade usando a média por espécie.
"""

import pandas as pd


def imputa_umidade_media(df: pd.DataFrame) -> pd.DataFrame:
    """Imputa os valores nulos da coluna 'umidade' com a média calculada

    exclusivamente para a mesma 'especie'.
    """
    df_limpo = df.copy()

    # Preenche nulos de 'umidade' com a média agrupada por 'especie'
    df_limpo["umidade"] = df_limpo["umidade"].fillna(
        df_limpo.groupby("especie")["umidade"].transform("mean")
    )

    return df_limpo