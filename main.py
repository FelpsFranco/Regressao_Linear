# Dados Retirados https://www.kaggle.com/datasets/karthickveerakumar/salary-data-simple-linear-regression

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# Variavel Equivalente ao Arquivo
dados = pd.read_csv('Salary_Data.csv')
# Mostrando Dados
print(dados)
# Verificando se há valores nulos será retornado True
print(pd.isna(dados))

# Criando Plot de Relação Entra Anos de Experiência(x) e Salário(y)
X = dados["YearsExperience"].values.reshape(-1, 1)
y = dados["Salary"].values.reshape(-1, 1)
figure(figsize=(12, 9), dpi=80)
plt.scatter(X, y)
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.title("Graph2")
plt.show()

# Pode ser notado que os pontos plotados não seguem um Padrão em uma única linha reta

slopes = [i for i in range(5000, 16000, 1000)]
intercepts = [i for i in range(21000, 32000, 1000)]
reg_lines = {}

for i, j in zip(slopes, intercepts):
    reg_lines[i] = j

# Gerando novo Plot referente as possíveis variâncias, encontrando possíveis regressões
figure(figsize=(12, 9), dpi=80)
plt.scatter(X, y)

for m, c in reg_lines.items():
    y_new = m*X + c
    plt.plot(X, y_new)

plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.title("Graph2")
plt.show()

# Cada Regressão gera uma quantidade de erros, vamos realizar a soma desses erros
Sums = []
for m, c in reg_lines.items():
    sum_of_squares = 0
    y_new = lambda x: m * x + c

    for i, j in zip(X, y):
        sum_of_squares += (j - y_new(i)) ** 2

    Sums.append(list(sum_of_squares))

# Agora que temos a soma dos erros de cada Regressão possível, precisamos selecionar a que possuí soma miníma

# Calculando a soma mínima da lista de somas.
soma_min = min(Sums)

# Encontrando o índice da soma mínima na lista de somas
index = Sums.index(soma_min)

# Convertendo o dicionário reg_lines para a lista reg_lines_list para buscar a inclinação necessária: interceptar do índice
reg_lines_list = list(reg_lines.items())

m = reg_lines_list[index][0]
c = reg_lines_list[index][1]
y_new = m*X + c

# Gerando Plot com uma única regressão
figure(figsize=(12, 9), dpi=80)
plt.scatter(X, y)

plt.plot(X, y_new, c='red')

plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.title("Graph2")
plt.show()
