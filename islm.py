# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:48:00 2022

@author: Gustavo Pietruza
"""

import pandas as pd
import matplotlib.pyplot as plt

def C_at(C0, c, Y_ant, T_ant):
    #Calcula o consumo presente
    C_at = C0 + c*(Y_ant - T_ant)
    return C_at

def I_at(I0, d, Y_ant, f, i_ant):
    I_at = I0 + d*Y_ant - f*i_ant
    return I_at

def T_at(T0, t, Y_ant):
    T_at = T0 + t*Y_ant
    return T_at

def D_at(D_ant, T_at, G_at):
    D_at = D_ant - T_at + G_at
    return D_at

def Y_at(C_at, I_at, G_at):
    Y_at = C_at + I_at + G_at
    return Y_at

def i_at(k, h, Y_at, M):
    i_at = (k/h * Y_at) - (1/h * M)
    return i_at

#Período inicial

C0 = 500
I0 = 400
G0 = 200
T0 = 100
D0 = 600
M = 3000
c = 0.8
d = 0.1
f = 1000
t = 0.05
k = 0.4
h = 9000

#Definição das variáveis de p = 0
#Multiplicador da renda
m = 1/(1-c-d+c*t)
#Gastos autônomos
A = C0 + I0 + G0 - c*T0
#Produto em p = 0
Y_eq = ((h*m)/(h+m*f*k))*A + ((m*f)/(h+m*f*k))*M
#Juros em p = 0
i_eq = i_at(k, h, Y_eq, M)
#Tributos arrecadados em p = 0
T = T0 + t*Y_eq
#Consumo em p = 0
C = C0 + c*(Y_eq - T)
#Investimento em p = 0
I = I0 + d*Y_eq - f*i_eq
#Gastos governamentais em p = 0
G = G0
#Dívida pública em p = 0
D = D0 + T - G
#Cria listas para armazenar os valores, incluindo o período inicial
lista_Y = [Y_eq]
lista_C = [C]
lista_I = [I]
lista_T = [T]
lista_G = [G]
lista_M = [M]
lista_i = [i_eq]
lista_D = [D]
#Define as variáveis de p = 0 como as de p-1
Y_ant = Y_eq
i_ant = i_eq
T_ant = T
D_ant = D

#Choque
G = 600
#Define o período de análise
p = 31
for period in range(1,p):
    C = C_at(C0, c, Y_ant, T_ant)
    I = I_at(I0, d, Y_ant, f, i_ant)
    T = T_at(T0, t, Y_ant)
    Y = Y_at(C, I, G)
    i = i_at(k, h, Y, M)
    D = D_at(D_ant, T, G)
    lista_Y.append(Y)
    lista_C.append(C)
    lista_I.append(I)
    lista_T.append(T)
    lista_G.append(G)
    lista_M.append(M)
    lista_i.append(i)
    lista_D.append(D)
    Y_ant = Y
    i_ant = i
    T_ant = T
    D_ant = D

#Cria um dataframe com os valores coletados
data = {'RENDA': lista_Y, 'JUROS': lista_i, 'CONSUMO': lista_C, 'INVESTIMENTO': lista_I, 'GASTOS GOVERNAMENTAIS': lista_G, 'TRIBUTOS': lista_T, 'QUANTIA DE MOEDA': lista_M, 'DÍVIDA DO GOVERNO': lista_D}    
df_data = pd.DataFrame(data)

#Cria um gráfico 3x3 demonstrando a evolução dos valores
fig, axes = plt.subplots(3, 3, figsize=(8, 8), constrained_layout=True)
for col, ax in zip(df_data.columns, axes.flat):
    df_data[col].plot(ax=ax, rot=0)
    ax.set_title(col)
for ax in axes.flat[df_data.columns.size:]:
    ax.set_axis_off()
plt.show()