import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)


dados = pd.read_csv('./microdados_enem_2019_sp.csv',
                    sep=';', encoding='iso-8859-1')

# print(dados.head(10))
# print(dados.shape)
# print(dados.dtypes)

dados1 = dados.drop(columns=['CO_MUNICIPIO_RESIDENCIA', 'CO_UF_RESIDENCIA', 'NO_MUNICIPIO_NASCIMENTO', 'TP_ANO_CONCLUIU', 'CO_MUNICIPIO_NASCIMENTO',
                    'TP_ENSINO', 'CO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC', 'CO_UF_NASCIMENTO', 'TP_DEPENDENCIA_ADM_ESC', 'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC'])

print(dados.shape)

dados1.loc[:, 'NU_NOTA_CN'] /= 10
dados1.loc[:, 'NU_NOTA_CH'] /= 10
dados1.loc[:, 'NU_NOTA_LC'] /= 10
dados1.loc[:, 'NU_NOTA_MT'] /= 10


dados1 = dados1.rename(columns={'NU_NOTA_REDACAO': 'NOTA_REDACAO'})
dados1 = dados1.rename(columns={'NU_NOTA_CN': 'NOTA_CN', 'NU_NOTA_CH': 'NOTA_CH',
                       'NU_NOTA_LC': 'NOTA_LC', 'NU_NOTA_MT': 'NOTA_MT'})
dados1 = dados1.rename(columns={'NU_NOTA_COMP1': 'COMP1', 'NU_NOTA_COMP2': 'COMP2',
                       'NU_NOTA_COMP3': 'COMP3', 'NU_NOTA_COMP4': 'COMP4', 'NU_NOTA_COMP5': 'COMP5'})
dados1 = dados1.rename(columns={'NU_IDADE': 'IDADE', 'TP_SEXO': 'SEXO',
                       'TP_COR_RACA': 'RACA', 'Q025': 'INTERNET', 'TP_ESCOLA': 'ESCOLA'})

dados1["RACA"] = dados1["RACA"].replace(
    {0: ' Não declarada', 1: 'Branca', 2: 'Preta', 3: 'Parda', 4: 'Amarela', 5: 'Indígena'})

print(dados1.head(10))
