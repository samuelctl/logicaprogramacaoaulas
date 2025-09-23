#classe - Espaço onde vou descrever objetos
#atributos  - que são ações desse objeto
#metodos - que são as ações desse objeto

# nome e vida - atacar
#self - quando quero me referir a algum atributo da class
#construtor - quando quero criar um novo objeto, chamo o construtir para acessar os atributos
class Personagem:
    #construtor
    def __init__(self, nome, vida):
        # encapsulamento
        self.__nome = nome
        self.__vida = vida
     # defininfdo GET
    @property
    def nome(self):
        return self.__nome
    
    #definindo SET
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def vida (self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida
    
    def atacar(self, personagem):
         personagem.vida -= 20
         print(f'{self.nome} atacou {personagem.nome} e tirou pontos de vida, agora esta com {personagem.vida} de vida')


class Guerreiro(Personagem):
    def __init__(self, nome, vida, escudo=False):
        super().__init__(nome, vida)
        self.__escudo = escudo
    @property
    def escudo(self):
        return self.__escudo
    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo
    # sobreescrevendo o metodo class pai
    def atacar(self, personagem):
        personagem.vida -= 40
        print(f'{self.nome} atacou {personagem.nome} e tirou pontos de vida\nagora esta com {personagem.vida} de vida')
    def protecao(self):
        self.__vida += 10




class Mago(Personagem):
    def __init__(self, nome, vida):     
        super().__init__(nome, vida)

    def curar(self, personagem):
        personagem.vida += 15
        print(f"{self.nome} usou poder de cura em {personagem.nome}")
        print(f"A vida de {personagem.nome} agora é de {personagem.vida}")

gandof = Mago('Gandof', 100)
aragorn = Guerreiro('Aragorn', 100)
frodo = Guerreiro('Frodo', 100)

aragorn.atacar(frodo)
gandof.curar(frodo)
aragorn.atacar(gandof)
gandof.curar(gandof)

        
    

'''class Batman:
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self, vida):
        self.__vida = vida
    
    def dano(self, personagem):
        personagem.vida -= 15
        print(f'O {self.nome} atacou o {personagem.nome} e perdeu 15 pontos de vida')
        print(f'A vida dele agora é: {personagem.vida}')
        if personagem.vida == 0:
            del(personagem)

personagem1 = Batman("Batman" , 200)
personagem2 = Batman("Coringa", 200)
personagem1.dano(personagem2)
personagem2.dano(personagem1)'''