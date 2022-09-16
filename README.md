# Modelo-de-Choque-IS-LM
Modelagem para choque econômico em modelo IS-LM intertemporal e economia fechada, com o objetivo de avaliar a evolução das variáveis envolvidas ao longo do tempo

ANÁLISE DAS VARIÁVEIS

Y : Produto da economia em p
Y_ant : Produto da economia em p-1
C : Consumo das famílias na economia em 
C0 : Consumo autônomo das famílias, independente da variação do produto da economia
c : Propensão marginal a consumir das famílias, varia entre 0 e 1, e indica a percentagem da renda alocada para o consumo
I : Investimentos das famílias em p
I0 : Investimento autônomo das familias, independente da variação do produto da economia
d : Sensibilidade do investimento de acordo com a renda, efeito renda sobre os investimentos
f : Sensibilidade do investimento de acordo com a taxa de juros, efeito juros sobre os investimentos
T : Tributo coletado pelo governo em p
T_ant : Tributo coletado pelo governo em p-1
T0 : Tributo autônomo coletado pelo governo, independente da variação do produto da economia
t : Propensão marginal a tributar, é a parcela do acréscimo de renda destinada à tributação
G : Gastos do governo em p
G0 : Gastos do governo autônomo, independente da variação do produto da economia
D : Dívida do governo no período p
D_ant : Dívida do governo no período p-1
D0 : Dívida do governo autônomo, independente da tributação e gastos governamentais
i : Taxa de juros da economia em p
i_ant : Taxa de juros da economia em p-1
Mo : Quantidade de moeda ofertada na economia, fixada pelo Banco Central
Md : Quantidade de moeda demandada na economia
M : Mo = Md
h : Sensibilidade da demanda por moeda de acordo com a renda
k : Sensibilidade da demanda por moeda de acordo com a taxa de juros

CURVA IS:

Y = C + I + G           
C = C0 + c * (Y_ant - T)  
I = I0 + d * Y_ant - f * i_ant
T = T0 + t * Y_ant        
G(t) = G0                     
D(t) = D_ant + T - G

Y = C0 + c * (Y_ant - (T0 + t * Y_ant )) + I0 + d * Y_ant - f * i_ant + G0
Y = C0 + c * Y_ant - c * T0 - c * t * Y_ant + I0 + d * Y_ant - f * i_ant + G0
Y = Y_ant * (c - c * t + d) + C0 + I0 + G0 - c * T0 - f * i_ant

CURVA LM:

M = k * Y - h * i
h * i = k * Y - M
i = k / h * Y - 1 / h * M
i_ant = k / h * Y_ant - 1 / h * M

EQUILÍBRIO:

Y = Y_ant * (c - c * t + d) + C0 + I0 + G0 - c * T0 - f * (k / h * Y_ant - 1 / h * M)
Y = Y_ant * (c - c * t + d) + C0 + I0 + G0 - c * T0 - f * k/h * Y_ant + f / h * M)
Y = Y_ant * [(c - c * t + d) - f * k / h] + C0 + I0 + G0 - c * T0 + f / h * M
Y = Y_ant * [((c - c * t + d) * h - f * k) / h] + C0 + I0 + G0 - c * T0 + f / h * M

Assumindo Y == Y_ant e i == i_ant

Y = Y * (c - c * t + d) + C0 + I0 + G0 - c * T0 - f * i
Y - Y * (c - c * t + d) =  C0 + I0 + G0 - c * T0 - f * i
Y * (1 - c - d + c * t) = C0 + I0 + G0 - c * T0 - f * i
Y = [1 / (1 - c - d + c * t)] * (C0 + I0 + G0 - c * T0) - [1 / (1 - c - d + c * t)] * f * i

Multiplicador simples: m = [1 / (1 - c - d + c * t)]
