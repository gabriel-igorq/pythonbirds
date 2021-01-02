class Pessoa:
    # Atributos de classe/default
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 26):
        # Atributos de instancia
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    # Método da instância
    def cumprimentar(self):
        return f'Olá {id(self)}'

    # Método da classe(usando decorator)
    @staticmethod
    def metodo_estatico():
        return 42

    # Usado para acessar dados da própria classe
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    rogerin.sobrenome = 'Costa'
    del rogerin.filhos
    rogerin.olhos = 1
    del rogerin.olhos
    print(rogerin.__dict__)
    print(biel.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(rogerin.olhos)
    print(biel.olhos)
    print(id(Pessoa.olhos), id(rogerin.olhos), id(biel.olhos))
    print(Pessoa.metodo_estatico(), rogerin.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), rogerin.nome_e_atributos_de_classe())