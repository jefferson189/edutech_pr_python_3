from cpf_cnpj_rudimentar import CpfCnpj
from validate_docbr import CNPJ

#cpf_um = Cpf("15316264754")
#print(cpf_um)

exemplo_cnpj = "35379838000112"
exemplo_cpf = "08873067999"
#cnpj = CNPJ()
#print(cnpj.validate_exemplo_cnpj))

documento = CpfCnpj(exemplo_cnpj, 'cnpj')
documento1 = CpfCnpj(exemplo_cpf, 'cpf')
print("Cnpj:", documento)
print("Cpf:", documento1)