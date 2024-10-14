# Segundo Desafio de projto do bootcamp Ifood / Calculadora de partidas Rankeadas
# Lucas Galvão dos Santos
# 16/Novembro/2023

def calculo(x, y):
    return x - y

vitorias = (int(input("Digite o número de vitórias: ")))
derrotas = (int(input("Digite o número de derrotas: ")))

resultado = calculo(vitorias, derrotas)

if (resultado < 10):
    conclusao = "Ferro"

elif (resultado >= 11 and resultado <= 20):
    conclusao = "Bronze"

elif (resultado >= 21 and resultado <= 50):
    conclusao = "Prata"

elif (resultado >= 51 and resultado <= 80):
    conclusao = "Ouro"

elif (resultado >= 81 and resultado <= 90):
    conclusao = "Diamante"

elif (resultado >= 91 and resultado <= 100):
    conclusao = "Lendário"

elif (resultado >= 101):
    conclusao = "Imortal"

print(f"O Herói tem de saldo {resultado} vitórias e está no nível de {conclusao}")