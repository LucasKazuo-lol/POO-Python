class Gafanhoto:
    def __init__(self): #Metodo Construtor
        #Atributos da instancia
        self.nome = ""
        self.idade = 0

    # metodos que a instancia tem
    def aniversario(self):
        self.idade = self.idade + 1
    
    def mensagem(self):
        return f"{self.nome} é uma pessoa daora mas tem {self.idade} ent ta envelhecendo"
    
# declarando os objetos

g1 = Gafanhoto()
g1.nome = "Lucas"
g1.idade = 18
g1.aniversario()
print(g1.mensagem())