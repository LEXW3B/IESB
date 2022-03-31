


class Locadora(object): 
    
    def __init__(self):
        self.listaCliente = []
        self.ListaCarro = []
        self.menu()

    def menu(self):
        

        while True:
            print('-'*50)
            print('=========Bem-vindo a Locadora Boa Viagem==========')
            print('-'*50)
            print("|==-   1 - Cadastrar novo veículo             -==|")
            print("|==-   2 - Cadastrar novo cliente             -==|")
            print("|==-   3 - Locação de veículo                 -==|")
            print("|==-   4 - Relatório de locação               -==|")
            print("|==-   5 - Relatório de veículos cadastrados  -==|")
            print("|==-   6 - Relatório de clientes cadastrados  -==|")
            print("|==-   7 - Finalizar o programa !!!           -==|")
            print("="*50)

            while True:
                try:
                    opc = int(input("\nDigite a opção desejada: "))
                    break
                except ValueError:
                    print("\nOpção inválida, tente novamente!\n")

            if opc == 1:
                Carro.new_car(self)

            elif opc == 2:
                Cliente.new_cliente(self)

                '''elif opc == 3:
                    RentCar(carList, clientList)

                elif opc == 4:
                    RentReport(rentList)

                elif opc == 5:
                    CarReport(carList)

                elif opc == 6:
                    ClientReport(clientList)

                elif opc == 7:
                    print("\nFinalizando o programa!!!\n\nObrigado pela preferência\n")
                    break'''

            else:
                print("\nOpção inválida!\n")
   
        
        
class Carro(Locadora):
    def __init__(self, placa, ano, categoria, transmissao, combustivel, marca, modelo):
        self.placa = placa
        self.ano = ano
        self.categoria = categoria
        self.transmissao = transmissao
        self.combustivel = combustivel
        self.marca = marca
        self.modelo = modelo
        
    def new_car(self):
        
        self.placa = str(input("\n\nplaca: ")).upper()
        self.ano = int(input("Ano: "))
        
        while True:
          
            print("\nEscolha uma das categorias:\n1 - Sedan\n2 - Picape\n3 - SUV")
            while True:
                try:
                    ctg = int(input("\nDigite a opção desejada: "))
                    break
                except ValueError:
                    print("\nOpção inválida, tente novamente!\n")
            if ctg == 1:
                self.categoria = "Sedan"
                break
            elif ctg == 2:
                self.categoria = "Picape"
                break
            elif ctg == 3:
                self.categoria = "SUV"
                break
            else:
                print("\nOpção inválida")
        
        
        while True:
           
            print("\nEscolha uma das transmissões:\n1 - Automático\n2 - Manual")
            while True:
                try:
                    trns = int(input("\nDigite a opção desejada: "))
                    break
                except ValueError:
                    print("\nOpção inválida, tente novamente!\n")
            if trns == 1:
                self.transmissao = "Automático"
                break
            elif trns == 2:
                self.transmissao = "Manual"
                break
            else:
                print("\nOpção inválida")
      
        
        while True:            
            print("\nEscolha um dos combustíveis a seguir:\n1 - Gasolina\n2 - Álcool\n3 - Flex\n4 - Diesel\n5 - GNV")                
            while True:
                try:
                    cmbst = int(input("\nDigite a opção desejada: "))
                    break
                except ValueError:
                    print("\nOpção inválida, tente novamente!\n")
                    
            if cmbst == 1:
                self.combustivel = "Gasolina"
                break
            elif cmbst == 2:
                self.combustivel = "Álcool"
                break
            elif cmbst == 3:
                self.combustivel = "Flex"
                break
            elif cmbst == 4:
                self.combustivel = "Diesel"
                break
            elif cmbst == 5:
                self.combustivel = "GNV"
                break
            else:
                print("\nOpção inválida")
        
        self.marca = str(input("Digite a marca: ")).upper()
        self.modelo = str(input("Digite o modelo: ")).upper()
        
        carro = {
            'placa': self.placa,
            'ano': self.ano,
            'categoria': self.categoria,
            'transmissao': self.transmissao,
            'combustivel': self.combustivel,
            'marca': self.marca,
            'modelo': self.modelo
        }

        self.ListaCarro.append(carro)
        print(self.ListaCarro)

        
        
class Cliente(Locadora):
     
    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        
    def new_cliente(self):
        
        self.nome = str(input("Digite o nome do cliente: "))
        self.cpf = str(input("Digite o CPF: "))
        self.rg = str(input("Digite o RG: "))
        
        print(f"O cliente {self.nome} foi cadastrado com sucesso!\n")
        
        usuario = {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg,       
        }

        self.listaCliente.append(usuario)
        print(self.listaCliente)
        
            
Locadora()      
      
      
  
      
      
      
        
        
























