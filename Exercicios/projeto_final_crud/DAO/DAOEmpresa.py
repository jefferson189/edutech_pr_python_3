from Model.Empresa import Empresa
from conexao import Conexao


class DAOEmpresa:

    def __init__(self):
        print("in init")

    def adicionarEmpresa(self):

        try:
            razaoSocial = input('Razão Social:')
            endereco = input('Endereço:')
            cnpj = input('cnpj:')
            num_funcionarios = input('Número de funcionários:')
            area_atuacao = input('Área de atuação:')
            novaEmpresa = Empresa(razaoSocial, endereco, cnpj, num_funcionarios, area_atuacao)
            # Adiciona Banco
            con = Conexao.getConnection('Estalecendo Conexao')
            cursor = con.cursor()
            query = "INSERT INTO empresa(razao_social, endereco, cnpj, num_funcionarios, area_atuacao)" \
                    "VALUES(%s,%s,%s,%s,%s)"
            dados = novaEmpresa.getRazaoSocial(), novaEmpresa.getEndereco(), novaEmpresa.getCnpj(),\
                        novaEmpresa.getNum_funcionarios(), novaEmpresa.getArea_atuacao()
            cursor.execute(query, dados)
            con.commit()

        except TypeError as error:
            print("Failed to insert the record from table: {}".format(error))

        finally:
            cursor.close()
            con.close()
            print("MySQL connection is closed")


    def listaEmpresas(self):

        try:
            con = Conexao.getConnection('Estalecendo Conexao')
            cursor = con.cursor()
            query = "select * from empresa"
            cursor.execute(query)
            # get all records
            records = cursor.fetchall()

            print("\n Mostra dados")
            for row in records:
                print("Id = ", row[0], )
                print("Razão Social = ", row[1])
                print("Endereço  = ", row[2])
                print("Cnpj  = ", row[3])
                print("Número de funcionários  = ", row[4])
                print("Área de atuação  = ", row[5])

        except TypeError as error:
            print("Failed to show the record from table: {}".format(error))

        finally:
            cursor.close()
            con.close()
            print("MySQL connection is closed")

    def deletaEmpresa(self):

        try:
            con = Conexao.getConnection('Estalecendo Conexao')
            cursor = con.cursor()
            nomeEmpresa = input('Nome da Empresa:')
            query = "DELETE from empresa WHERE razao_social = %s"
            cursor.execute(query, nomeEmpresa)
            con.commit()

        except TypeError as error:
            print("Failed to delete record from table: {}".format(error))

        finally:
            cursor.close()
            con.close()
            print("MySQL connection is closed")