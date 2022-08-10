# Estatística para machine learning

## O que é estatística?

- Ciência que objetiva coletar, organizar, analisar e interpretar dados para tomadas de decisão.

## Aplicações

- Inteligência Artificial (Machine Learning e Deep Learning).
- Ciência de Dados.
- Economia e Administração.
- Engenharia.
- Educação.
- Biomedicina.
- Pesquisas Científicas.

## Tipos

- Probabilistica
- Inferencial
- Descritiva

## Probabilística

- Conceitos de probabilidades (espaço amostral, eventos e tipos de probabilidades).
- Distribuições de probabilidade discretas e contínuas: Binomial, Poisson, Exponencial e Normal.

## Inferencial

- Estimativa: estimação de parâmetros e intervalo de confiança.
- Testes de hipóteses: paramétricos e não paramétricos.
- Correlação e Regressão Linear.

## Descritiva

- Tipos de Variáveis.
- População e Amostragem.
- Medidas de Posição: Média, Mediana, Moda e Quartis.
- Medidas de Dispersão: Amplitude, Variância, Desvio Padrão e coeficiente de variação.
- Assimetria.

## Principais ferramentas

- Python
- Linguagem R
- SPSS
- SAS
- Minitab
- Excel
- Microsoft Power BI ou Tableu
- Stata
- Matlab
- Emblem

# Conceitos fundamentais

## Dados

- Informações provenientes de contagens, medidas, observações e respostas, formando conjuntos de dados.

## População

- relação de todos os dados de interesse. São extraídos parâmetros.

## Amostra

- é um subconjunto da população. São extraídas estatísticas.

## Classificação dos dados

- Qualitativos: atributos não numéricos.

  - Nominais: Denominações (cores, gênero, raça, títulos…)
  - Ordinais: atributos que podem ser classificados (Ex: classificação de filmes mais assistidos, grau de escolaridade, nível de satisfação…).

- Quantitativos: medidas numéricas ou de contagem.
  - Discreto: valores finitos ou enumeráveis (quantidade de pessoas numa sala, número de carros em um estacionamento…)
  - Contínuo: infinitos valores possíveis num intervalo (renda, tempo, altura…).

# Código

## Importando pacotes

    import numpy as np
    import pandas as pd
    pd.set_option('display.max_columns', None)

## Importando o DATASET

    dados = pd.read_csv('./microdados_enem_2019_sp.csv', sep=';', encoding='iso-8859-1')

## Apresentando os dados

    dados.head()
