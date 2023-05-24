# -*- coding: utf-8 -*-

import pandas as pd

perfil_mca = pd.read_excel("Perfil Aplicação Civil.xlsx")

print(perfil_mca)

#%% Selecionando apenas variáveis para análise

perfil_mca_select = perfil_mca.drop(columns=['estudante'])

print(perfil_mca_select)

#%% Gerando a matriz binária

perfil_mca_binaria = pd.get_dummies(perfil_mca_select)

#%% Importando numpy

import numpy as np

#%% Gerando a matriz de Burt

matriz_burt = np.matmul(perfil_mca_binaria.T,perfil_mca_binaria)

#%% Ajustando os nomes das colunas da matriz

matriz_burt.columns = matriz_burt.index

#%% Características dos dados

qnt_variaveis = 3

somatorio_de_categorias = 8

#%% Número de dimensões na análise

dimensoes = somatorio_de_categorias - qnt_variaveis
print(dimensoes)

#%% Inércia Total

I_total = (somatorio_de_categorias - qnt_variaveis)/qnt_variaveis
print(I_total)

#%% Média da inércia

media_inercia = I_total/dimensoes
print(media_inercia)

#%% Informações das variáveis

# Todas as categorias da variável
print(perfil_mca['aplicacao'].unique())

# O número de categorias na variável
print(len(perfil_mca['aplicacao'].unique()))

#%%