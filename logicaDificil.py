# Terceiro Desafio de projto do bootcamp Ifood / Escrevendo as classes de um Jogo
# Lucas Galvão dos Santos
# 16/Novembro/2023

# Solicita ao usuário as informações do herói
nome_heroi = input("Digite o nome do herói: ")
idade_heroi = (int(input("Digite a idade do herói: ")))
tipo_heroi = input("Digite o tipo do herói (mago, guerreiro, monge, ninja): ")

# Define a classe Heroi
class heroi:
    
    # Método construtor para inicializar as propriedades do herói
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    # Método para realizar o ataque com base no tipo do herói
    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "um ataque desconhecido"

        print(f"O {self.tipo} {self.nome} de {self.idade} anos atacou usando {ataque}")

# Cria um objeto da classe Heroi com as informações fornecidas pelo usuário
heroi_do_usuario = heroi(nome_heroi, idade_heroi, tipo_heroi)

# Chama o método atacar para exibir a mensagem de ataque
heroi_do_usuario.atacar()