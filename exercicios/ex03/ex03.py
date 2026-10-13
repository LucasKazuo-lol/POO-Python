class ContaBancaria:
    """
    Cria conta bancaria que permite fazer saque 
    e deposito
    """
    
    def __init__(self,id,titular,saldo=0):
        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"A conta\033[33m {self.id}\033[m do Titular \033[35m{self.titular}\033[m tem de saldo R$\033[32m{self.saldo:,.2f}\033[m"
    
    def deposito(self, valor):
        self.saldo += valor
        print(f"Deposito Concluido no valor de {valor}")
    
    def sacar(self,valor):
        if valor < self.saldo:
            self.saldo -= valor
            print(f"Saque feito saldo atual de {self.saldo}")
        else:
            print(f"Saque negado de {valor:.2f} na conta {self.id} do titular {self.titular}")

c1 = ContaBancaria(122,"Lucas",2300)
c1.deposito(400)
print(c1)
print("Saque de 500")
c1.sacar(90000)
print(c1)