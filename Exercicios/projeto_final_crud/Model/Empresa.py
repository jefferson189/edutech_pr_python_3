class Empresa:
    def __init__(self, razao_social, endereco, cnpj, id_empresa, num_funcionarios, area_atuacao):
        self.razao_social = razao_social
        self.endereco = endereco
        self.cnpj = cnpj
        self.id_empresa = id_empresa
        self.num_funcionarios = num_funcionarios
        self.area_atuacao = area_atuacao

# para alterar os dados
    def setArea_atuacao(self, area_atuacao):
        self.area_atuacao = area_atuacao

    def setRazaoSocial(self, razao_social):
        self.razao_social = razao_social

    def setEndereco(self, endereco):
        self.endereco = endereco

    def setCnpj(self, cnpj):
        self.cnpj = cnpj

    def setId_empresa(self, id_empresa):
        self.id_empresa = id_empresa

    def setNum_funcionarios(self, num_funcionarios):
        self.num_funcionarios = num_funcionarios


#Mostrar os dados
    def getRazaoSocial(self):
        return self.razao_social

    def getEndereco(self):
        return self.endereco

    def getCnpj(self):
        return self.cnpj

    def getId_empresa(self):
        return self.id_empresa

    def getNum_funcionarios(self):
        return self.num_funcionarios

    def getArea_atuacao(self):
        return self.area_atuacao