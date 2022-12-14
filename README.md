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

## Shape

    dados.shape

## Tipos de dados

    dados.dtypes

## Tratando o dataset

### Removendo colunas

    dados1 = dados.drop(columns=['CO_MUNICIPIO_RESIDENCIA', 'CO_UF_RESIDENCIA','NO_MUNICIPIO_NASCIMENTO','TP_ANO_CONCLUIU','TP_ENSINO','CO_MUNICIPIO_ESC','CO_UF_ESC','SG_UF_ESC','TP_DEPENDENCIA_ADM_ESC','TP_LOCALIZACAO_ESC','TP_SIT_FUNC_ESC'])

# Planejamento do estudo Estatístico

- Identificação da população e das variáveis.
- Plano para coleta de dados.
- Coleta de dados.
- Descrição dos dados usando técnicas da estatística descritiva.
- Interpretação dos dados e tomadas de decisões através da estatística inferencial.
- Análise de possíveis erros.

# Observações e experimentos

## Observações

- elementos analisados não foram sujeitos a interferências (Ex.: pesquisa eleitoral).

## Experimentos

- elementos foram manipulados para obtenção dos resultados (Ex.: análise de medicamentos em testes).

# Amostragem

- Amostragem é a medição ou contagem de parte de uma população.
- Censo é a medição ou contagem de toda a população.
- Amostras aleatórias: Todos os elementos tem chances iguais de serem relacionados. Pode ser com reposição ou sem reposição.
- Amostras tendenciosas: não representam a população.

# Técnicas de amostragem

- Aleatória Simples: Seleção executada por meio de sorteio, sem nenhum filtro.
- Estratificada: Divisão da população em grupos e seleção aleatória de uma amostra de cada grupo. (Ex: divisão por região, classe social, religião…).
- Conglomerado (Agrupamento): Divisão da população em grupos com características similares, porém heterogêneas, e seleção aleatória de alguns grupos para analisar todos os elementos destes grupos. (Ex.: Divisão da população de escolas estaduais por região, enfermeiros de uma rede de hospitais… ).
- Sistemática: Membros da população são ordenados numericamente e são selecionados aleatoriamente, obedecendo uma sequência numérica. (Ex.: criação de números para cada amostra e seleção obedecendo uma ordem numérica).
