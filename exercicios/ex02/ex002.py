class Gafanhoto:
    """
    Essa classe cria um gafanhoto que é uma pessoa 
    que tem nome e idade
    
    pra criar uma pessoa usa
    varial = (nome, idade)
    """
    
    def __init__(self, n="vazio", i=0): #Metodo Construtor
        #Atributos da instancia
        self.nome = n
        self.idade = i

    # metodos que a instancia tem
    def aniversario(self):
        self.idade = self.idade + 1
    
    
    def __str__(self): #dunder method
        return f"\033[32m{self.nome}\033[m é uma pessoa daora mas tem \033[31;47m{self.idade}\033[m ent ta envelhecendo"
    
    def __getstate__(self):
        return f"estado: {self.nome} | idade: {self.idade}"
    
# declarando os objetos

g1 = Gafanhoto("lucas", 18)
g1.aniversario()

g2 = Gafanhoto("Fernanda", 19)


print(g1.__doc__) # dunder attribute
print(g1)

print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)

# print(g2)
# print(g2.__getstate__())