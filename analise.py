from dataset import dados1

# print(dados1.head(10))
# print(dados1['IDADE'].value_counts())
# print(dados1['IDADE'].value_counts().sort_index())

# menores_12 = dados1.query('IDADE <= 12')[
#     'NO_MUNICIPIO_RESIDENCIA'].value_counts().sort_index()

# print(menores_12)

maiores_11 = dados1.loc[dados1.IDADE > 11]
# internet_sim = maiores_11.loc[maiores_11.ESCOLA == 'PÚBLICA']

# print(internet_sim.head(40))

# treineiros = maiores_11.query('IN_TREINEIRO == 1')[
# 'IN_TREINEIRO'].value_counts()

# print(treineiros)

# treineiros = maiores_11.loc[maiores_11.IN_TREINEIRO == 1]

# print(treineiros.head(40))

# print(maiores_11.head(40))

# treineiros.to_csv('treineiros_enem_2019_sp.csv',
#   encoding='iso-8859-1', index=False)

vestibulandos = maiores_11.loc[maiores_11.IN_TREINEIRO == 0]
print(vestibulandos)

vestibulandos.to_csv('vestibulandos_enem_2019_sp.csv',
                     encoding='iso-8859-1', index=False)

# print(vestibulandos.head(40))
