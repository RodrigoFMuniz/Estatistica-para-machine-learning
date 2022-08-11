import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)


dados = pd.read_csv('./microdados_enem_2019_sp.csv',
                    sep=';', encoding='iso-8859-1')

print(dados.head(10))
print(dados.shape)
print(dados.dtypes)
