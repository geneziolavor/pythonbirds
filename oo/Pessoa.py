class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':
    genezio = Pessoa(nome='genezio')
    maria = Pessoa(genezio, nome='maria')
    print(Pessoa.cumprimentar(genezio))
    print(id(genezio))
    print(genezio.cumprimentar())
    print(genezio.nome)
    print(genezio.idade)
    for filho in genezio.filhos:
        print(filho.nome)





