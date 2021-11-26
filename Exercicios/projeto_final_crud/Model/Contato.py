class Contato:
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email

# Alterar os dados
    def setTelefone(self, telefone):
        self.telefone = telefone

    def setEmail(self, email):
        self.email = email

# Mostrar os dados
    def getTelefone(self):
        return self.telefone

    def getEmail(self):
        return self.email