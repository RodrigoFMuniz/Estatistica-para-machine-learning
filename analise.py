from dataset import dados1

# print(dados1.head(10))
print(dados1['IDADE'].value_counts())
print(dados1['IDADE'].value_counts().sort_index())

menores_12 = dados1.query('IDADE <= 12')[
    'NO_MUNICIPIO_RESIDENCIA'].value_counts().sort_index()

maiores_11 = dados1.loc[dados1.IDADE > 11]

print(maiores_11.head(40))
