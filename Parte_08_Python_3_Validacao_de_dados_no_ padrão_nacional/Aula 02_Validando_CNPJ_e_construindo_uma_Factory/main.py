from cpf_cnpj import Documento

exemplo_cnpj = "35379838000112"
exemplo_cpf = "08873067999"

documento = Documento.cria_documento(exemplo_cnpj)
documento1 = Documento.cria_documento(exemplo_cpf)
print("Cnpj:", documento)
print("Cpf:", documento1)