"""
Módulo de pré-processamento e engenharia de atributos para o dataset do Titanic.

Mantém a lógica de negócio fora do notebook, conforme descrito no README do projeto:
"src/: Scripts Python contendo funções auxiliares para manter o Notebook
limpo e focado em negócio."
"""

import pandas as pd


def preprocess(filepath: str) -> pd.DataFrame:
    """
    Carrega os dados do Titanic e aplica o pipeline de limpeza inicial.

    Etapas:
    - Padronização dos nomes de colunas (lowercase)
    - Imputação de nulos em 'idade' (mediana por classe/sexo)
    - Imputação de nulos em 'embarque' (moda)
    - Criação da faixa etária ('faixa_etaria')

    Parameters
    ----------
    filepath : str
        Caminho para o arquivo CSV bruto.

    Returns
    -------
    pd.DataFrame
        DataFrame limpo, pronto para EDA e feature engineering adicional.
    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Arquivo não encontrado: {filepath}. Verifique o diretório 'data/'."
        )

    df.columns = df.columns.str.lower()

    df['idade'] = df['idade'].fillna(
        df.groupby(['classe', 'sexo'])['idade'].transform('median')
    )
    df['embarque'] = df['embarque'].fillna(df['embarque'].mode()[0])

    df['faixa_etaria'] = [
        'Criança' if idade < 12 else 'Adulto' if idade < 60 else 'Idoso'
        for idade in df['idade']
    ]

    return df


def _classificar_familia(tamanho: int) -> str:
    """Classifica o porte da família a partir do tamanho total (uso interno)."""
    if tamanho == 1:
        return 'Sozinho'
    elif 2 <= tamanho <= 4:
        return 'Pequena'
    else:
        return 'Grande'


def add_family_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria as features de dinâmica familiar.

    - 'tamanho_familia': irmaos_conjuges + pais_filhos + 1 (o próprio passageiro)
    - 'perfil_familiar': categorização em Sozinho / Pequena / Grande

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'irmaos_conjuges' e 'pais_filhos'.

    Returns
    -------
    pd.DataFrame
        DataFrame com as novas colunas adicionadas.
    """
    df['tamanho_familia'] = df['irmaos_conjuges'] + df['pais_filhos'] + 1
    df['perfil_familiar'] = df['tamanho_familia'].apply(_classificar_familia)
    return df


def add_deck_feature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extrai o deck a partir da primeira letra de 'nivel_cabine'.

    Nulos recebem 'U' (Unknown), assumindo que a ausência de registro
    tem peso preditivo.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame contendo a coluna 'nivel_cabine'.

    Returns
    -------
    pd.DataFrame
        DataFrame com a coluna 'deck' adicionada.
    """
    df['deck'] = df['nivel_cabine'].fillna('U').astype(str).str[0]
    return df