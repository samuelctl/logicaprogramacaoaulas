class Espirito:
    def __init__(self, nome, vida, esquivo=True):
        self.__nome = nome
        self.__vida = vida
        self.__esquivo = esquivo
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self,vida):
        self.__vida = vida
    @property
    def esquivo(self):
        return self.__esquivo
    @esquivo.setter
    def esquivo(self, esquivo):
        self.__esquivo = esquivo
    def ataque(self, personagem):
        personagem.vida -= 50
        print(f'{self.nome} atacou {personagem.nome} e tirou pontos de vida, agora esta com {personagem.vida} de vida')
    def esquivo(self, personagem):
        self.__vida += 400
        print(f'{self.nome} usou esquivo a vida atual é: {personagem.vida}')


class Coringa(Espirito):
    def __init__(self, nome, vida):     
        super().__init__(nome, vida)

    def curar(self, personagem):
        personagem.vida += 15
        print(f"{self.nome} usou poder de cura em {personagem.nome}")
        print(f"A vida de {personagem.nome} agora é de {personagem.vida}")

    def ataque(self, personagem):
        personagem.vida -= 50
        print(f'{self.nome} atacou {personagem.nome} e tirou pontos de vida, agora esta com {personagem.vida} de vida')
class Rato(Espirito):
    def __init__(self, nome, vida):
        super().__init__(nome,vida)
    def atacar(self, personagem):
        personagem.vida -=200
        print(f'{self.nome} atacou {personagem.nome} e tirou pontos de vida, agora esta com {personagem.vida} de vida')
        
fantasma_real = Espirito('Fantasma', 250)
curandeira = Coringa("Beth", 300)
rato = Rato("Rataria", 350)
fantasma_real.ataque(curandeira)
print("-" *20, "Ataque", 20* "-")
curandeira.curar(curandeira)
print("-" *20, "Cura", 20* "-")
rato.atacar(fantasma_real)
print("-" *20, "Atacar", 20* "-")
fantasma_real.esquivo(fantasma_real)
print("-" *20, "Esquivo", 20* "-")
curandeira.ataque(fantasma_real)
print("-" *20, "Ataque", 20* "-")
fantasma_real.ataque(rato)
print("-" *20, "Ataque", 20* "-")
curandeira.curar(rato)
print("-" *20, "Cura", 20* "-")




        
    
    
   