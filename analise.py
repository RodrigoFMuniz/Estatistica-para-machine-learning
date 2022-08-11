from dataset import dados1

# print(dados1.head(10))
print(dados1['IDADE'].value_counts())
print(dados1['IDADE'].value_counts().sort_index())
