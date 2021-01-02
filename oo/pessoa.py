class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 26):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    biel = Pessoa(nome='Gabriel')
    rogerin = Pessoa(biel, nome='Rogério')
    print(Pessoa.cumprimentar(rogerin))
    print(id(rogerin))
    print(rogerin.cumprimentar())
    print(rogerin.nome)
    print(rogerin.idade)
    for filho in rogerin.filhos:
        print(filho.nome)