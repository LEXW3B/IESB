class Locadora(object):  #Aqui fica definida a superclasse com o nome (object)
    def __init__(self):
        '''Este bloco faz a ligação dos dados da (LISTAS, que serve como banco de dados) e o menu'''
        self.ListaCliente = []
        self.ListaCarro = []
        self.AluguelCarro = []
        self.menu()
        
    def alugar(self):
        '''Este bloco verifica se o cpf ja está cadastrado, se não estiver ele leva para o bloco de cadastrar um novo cpf. Se o cpf já for cadastrado ai vai aparecer uma lista de carros para ser alugados'''
        print("\n")
        print("="*28)
        print("-=-=-   Alugar Carro   -=-=-")
        print("="*28)
        print("\n") 
        print("="*28)       
        self.cpf = str(input("Digite seu CPF: "))
        print("="*28)
        while True:
            if not Cliente.existe_cliente(self):
                print("-"*28)
                print("Novo Cadastro!")
                print("-"*28)
                Cliente.novo_cliente(self)
            else:
                break            
        print("\n")    
        print("-"*28)        
        Carro.listar_carro(self)
        Carro.buscar_carro(self)
        Locadora.lista_aluguel(self)#
        print("-"*28)
        print("\n")
        
    def lista_aluguel(self):
        '''Este bloco lista os carros ja cadastrados e uma extensão do bloco lista alugados'''
        alugado = {
            'nome':self.nome,
            'cpf':self.cpf,
            'rg': self.rg,
            'placa':self.placa,
            'ano': self.ano,
            'categoria': self.categoria,
            'transmissao': self.transmissao,
            'combustivel': self.combustivel,
            'marca': self.marca,
            'modelo': self.modelo,
            'aluguel': self.aluguel
        }
        self.AluguelCarro.append(alugado)
        print("Carro alugado com sucesso!")
        
    def lista_alugados(self):
        '''Este bloco trás a lista dos carros para alugar'''
        print("\n")
        print("="*47)
        print("-=-=-   Carros disponíveis para aluguel   -=-=-")
        print("="*47)
        print("\n")
        
        if len(self.AluguelCarro) > 0:
            for i, loc in enumerate(self.AluguelCarro):
                print('-='*47)
                print(f"Carro {i+1}:")                
                print(f"Nome: {loc['nome']}")                
                print(f"CPF: {loc['cpf']}")                
                print(f"RG: {loc['rg']}\n")                
                print(f"Placa: {loc['placa']}")            
                print(f"Ano: {loc['ano']}")                
                print(f"Categoria: {loc['categoria']}")                
                print(f"Transmissão: {loc['transmissao']}")                
                print(f"Combustível: {loc['combustivel']}")                
                print(f"Marca: {loc['marca']}")                
                print(f"Modelo: {loc['modelo']}")                
                print(f"Aluguel:{loc['aluguel']}")
                print('-='*47)
            print('-='*26)
            print(f"Total de veículos alugados é: {len(self.AluguelCarro)}\n")
            print('-='*26)
        else:
            print('-='*26)
            print("\nNenhum veículo alugado para listar! ")
            print('-='*26)
            
    def menu(self):
        while True:
            print('-'*52)
            print('==========Bem-vindo a Locadora Boa Viagem===========')
            print('-'*52)
            print("|==-  1  -  Cadastrar novo veículo              -==|")
            print("|==-  2  -  Cadastrar novo cliente              -==|")
            print("|==-  3  -  Locação de veículo                  -==|")
            print("|==-  4  -  Relatório de locação                -==|")
            print("|==-  5  -  Busca de veículos cadastrados       -==|")
            print("|==-  6  -  Busca de clientes cadastrados       -==|")
            print("|==-  7  -  Relatório de veículos cadastrados   -==|")
            print("|==-  8  -  Relatório de clientes cadastrados   -==|")
            print("|==-  9  -  Alterar dados veículos cadastrados  -==|")
            print("|==-  10 -  Alterar dados clientes cadastrados  -==|")
            print("|==-  11 -  Finalizar o programa                -==|")
            print("="*52)
            while True:
                try:
                    print('-'*52)
                    opc = int(input("\nDigite o número da sua opção escolhida: "))
                    print('-'*52)
                    break
                except ValueError:
                    print('-'*52)
                    print("\nSomente números.Não aceita letras, tente novamente.\n")
                    print('-'*52)

            if opc == 1:
                Carro.novo_carro(self)

            elif opc == 2:
                Cliente.novo_cliente(self)

            elif opc == 3:
                Locadora.alugar(self)

            elif opc == 4:
                Locadora.lista_alugados(self)

            elif opc == 5:
                Carro.buscar_carro(self)

            elif opc == 6:
                Cliente.buscar_cliente(self)

            elif opc == 7:
                Carro.listar_carro(self)

            elif opc == 8:
                Cliente.listar_cliente(self)

            elif opc == 9:
                Carro.alterar_carro(self)

            elif opc == 10:
                Cliente.alterar_cliente(self)

            elif opc == 11:
                print('-'*52)
                print("\nPrograma finalizado, bom dia.")
                print('-'*52)
                break
            else:
                print('-'*52)
                print("\nResposta inválida, tente novamente.\n")
                print('-'*52)
          
class Carro(Locadora):#Aqui começa a subclasse Carro que está ligada por parâmentro a superclasse Locadora
    def __init__(self, placa, ano, categoria, transmissao, combustivel, marca, modelo, aluguel):
        self.placa = placa
        self.ano = ano
        self.categoria = categoria
        self.transmissao = transmissao
        self.combustivel = combustivel
        self.marca = marca
        self.modelo = modelo
        self.aluguel = aluguel
        
    def alterar_carro(self):#COMPLETO
        '''Este bloco modifica os dados de carros já cadastrados'''
        print("\n")
        print("="*43)
        print("-=-=-   Alterar dados dos Veiculos   -=-=-")
        print("="*43)
        print("\n")
        if len(self.ListaCarro) > 0:
            print('-='*43)
            self.placa = str(input("Digite a placa : ")).upper()
            print('-='*43)
            if Carro.existe_carro(self):
                for car in self.ListaCarro:
                    if car['placa'] == self.placa:
                        print('-='*43)
                        print(f"\n\tPlaca: {car['placa']}")
                        print(f"\tAno: {car['ano']}")
                        print(f"\tCategoria: {car['categoria']}")
                        print(f"\tTransmissão: {car['transmissao']}")
                        print(f"\tCombustível: {car['combustivel']}")
                        print(f"\tMarca: {car['marca']}")
                        print(f"\tModelo: {car['modelo']}")
                        print(f"\tAluguel: {car['aluguel']}\n")
                        print('-='*43)

                        print('-='*43)
                        car['placa'] = str(input("Placa:")).upper()
                        print('-='*43)
                        car['ano'] = str(input("Ano:"))
                        print('-='*43)
                        Carro.categoria(self)
                        car['categoria'] = self.categoria
                        Carro.transmissao(self)
                        car['transmissao'] = self.transmissao
                        Carro.combustivel(self)
                        car['combustivel'] = self.combustivel
                        car['marca'] = str(input("Marca:")).upper()
                        print('-='*43)
                        car['modelo'] = str(input("modelo:")).upper()
                        print('-='*43)
                        car['aluguel'] = print(f"\tAluguel: {car['aluguel']}\n")
                        print(f"Os dados da {self.placa} foram alterados")
                        print('-='*43)
                        break

            else:
                print(f"Não existe veiculo cadastrado com a placa informado {self.placa}")
                print('-='*43)
                    
        else:
            print("Não existe veículo a ser alterado!")
            print('-='*43)
        
    def listar_carro(self):#COMPLETO
        '''Este bloco lista todos os carros cadastrados'''
        if len(self.ListaCarro) > 0:
            for i, car in enumerate(self.ListaCarro):
                print('-='*37)
                print(f"Carro {i+1}:")
                print(f"Placa: {car['placa']}")
                print(f"Ano: {car['ano']}")
                print(f"Categoria: {car['categoria']}")
                print(f"Transmissão: {car['transmissao']}")
                print(f"Combustível: {car['combustivel']}")
                print(f"Marca: {car['marca']}")
                print(f"Modelo: {car['modelo']}")
                print(f"Aluguel:{car['aluguel']}")
                print('-='*37)
            print('-='*37)
            print(f"Total de carros é: {len(self.ListaCarro)}\n")
            print('-='*37)
        else:
            print('-='*37)
            print("\nNão existe veículo cadastrado para ser listado! ")
            print('-='*37)
    
    def buscar_carro(self):#COMPLETO
        '''Este bloco procura pela placa por um veiculo específico'''
        if len(self.ListaCarro) > 0:
            print('-='*26)
            self.placa = str(input("Digite a placa: ")).upper()
            print('-='*26)
            for car in self.ListaCarro:
                if car['placa'] == self.placa:
                    print(f"Placa: {car['placa']}")
                    print('-'*37)
                    print(f"Ano: {car['ano']}")
                    print('-'*37)
                    print(f"Categoria: {car['categoria']}")
                    print('-'*37)
                    print(f"Transmissão: {car['transmissao']}")
                    print('-'*37)
                    print(f"Combustível: {car['combustivel']}")
                    print('-'*37)
                    print(f"Marca: {car['marca']}")
                    print('-'*37)
                    print(f"Modelo: {car['modelo']}")
                    print('-'*37)
                    print(f"Aluguel:{car['aluguel']}")
                    print('-'*37)
                    break
        else:
            print('-='*37)
            print("Nenhum veiculo com a placa {car['placa']} foi encontrada.")
            print('-='*37)
          
    def buscar_carro_alugar(self):
        if len(self.ListaCarro) > 0:
            self.placa = str(input("Digite a placa: ")).upper()
            for car in self.ListaCarro:
                if car['aluguel'] == "ALUGADO":
                    print("Nenhum veiculo disponível para alugar.")
                else:
                    if car['placa'] == self.placa:
                        print(f"Placa: {car['placa']}")
                        print(f"Ano: {car['ano']}")
                        print(f"Categoria: {car['categoria']}")
                        print(f"Transmissão: {car['transmissao']}")
                        print(f"Combustível: {car['combustivel']}")
                        print(f"Marca: {car['marca']}")
                        print(f"Modelo: {car['modelo']}")
                        print(f"Aluguel:{car['aluguel']}")
                        if car['aluguel'] == "ALUGADO":
                            print("O veículo já está locado!")
                        else:
                            car['aluguel'] = "ALUGADO"
        else:
            print("Nenhum veiculo disponível para alugar!!!")
   
    def existe_carro(self):#COMPLETO
        '''Este bloco verifica se tem o carro que está procurando dentro da (ListaCarro)'''
        if len(self.ListaCarro) > 0:
            for car in self.ListaCarro:
                if car['placa'] == self.placa:
                    return True
        return False
    
    def categoria(self):#COMPLETO
        '''Este bloco você escolhe o nome do carro'''
        while True:
            print('-'*37)
            print("1 - Sedan\n2 - Picape\n3 - SUV\n4 - Fusca")
            print('-'*37)
            while True:
                try:
                    print('-'*37)
                    cat = int(input("\nDigite o número da categoria de sua preferência: "))
                    print('-'*37)
                    break
                except ValueError:
                    print('-'*37)
                    print("\nNão aceita letras!\n")
                    print('-'*37)

            if cat == 1:
                self.categoria = "SEDAN"
                break
            elif cat == 2:
                self.categoria = "PICAPE"
                break
            elif cat == 3:
                self.categoria = "SUV"
                break
            elif cat == 4:
                self.categoria = "FUSCA"
                break
            else:
                print('-'*37)
                print("\nOpção inválida, tente novamente.")
                print('-'*37)
                
    def transmissao(self):#COMPLETO
        '''Este bloco você escolhe o tipo de transmissão'''
        while True:
            print('-'*37)
            print("\n1 - Automático\n2 - Manual\n3 - Semiautomático")
            print('-'*37)
            while True:
                try:
                    print('-'*37)
                    trans = int(input("\nDigite o número do tipo de cambio de sua preferência: "))
                    print('-'*37)
                    break
                except ValueError:
                    print('-'*37)
                    print("\nNão aceita letras!\n")
                    print('-'*37)

            if trans == 1:
                self.transmissao = "AUTOMATICO"
                break
            elif trans == 2:
                self.transmissao = "MANUAL"
                break
            elif trans == 3:
                self.transmissao = "SEMIAUTOMÁTICO"
                break
            else:
                print('-'*37)
                print("\nOpção inválida, tente novamente.") 
                print('-'*37)   
                
    def combustivel(self):#COMPLETO
        '''Este bloco você escolhe o tipo de combustível'''
        while True:
            print('-'*37)
            print("\n1 - Gasolina\n2 - Álcool\n3 - Flex\n4 - Diesel\n5 - GNV")
            while True:
                try:
                    print('-'*37)
                    comb = int(input("\nDigite o número do tipo de combustível da sua preferência: "))
                    print('-'*37)
                    break
                except ValueError:
                    print('-'*37)
                    print("Não aceita letras!\n")
                    print('-'*37)

            if comb == 1:
                self.combustivel = "GASOLINA"
                break
            elif comb == 2:
                self.combustivel = "ALCOOL"
                break
            elif comb == 3:
                self.combustivel = "FLEX"
                break
            elif comb == 4:
                self.combustivel = "DIESEL"
                break
            elif comb == 5:
                self.combustivel = "GNV"
                break
            else:
                print('-'*37)
                print("\nOpção inválida, tente novamente.")
                print('-'*37)
       
    def novo_carro(self):#COMPLETO
        '''Este bloco cadastra um novo carro'''
        print("\n")
        print("="*37)
        print("-=-=-  Cadastrar Novo Veiculo   -=-=-")
        print("="*37)
        print("\n")
        while True:
            print('-'*37)
            self.placa = str(input("\n\nDigite a placa do carro: ")).upper()
            print('-'*37)
            if not Carro.existe_carro(self):
                break
            else:
                print('-'*37)
                print("\nJá cadastrado no sistema")
                print('-'*37)
        print('-'*37)
        self.ano = int(input("Digite o ano do carro: "))
        print('-'*37)

        print('-'*37)
        Carro.categoria(self)#chama a função reutilizável para escolher um tipo de categoria
        print('-'*37)

        print('-'*37)
        Carro.transmissao(self)#chama a função reutilizável para escolher um tipo de transmissão
        print('-'*37)

        print('-'*37)
        Carro.combustivel(self)#chama a função reutilizável para escolher um tipo de combustivel
        print('-'*37)
         
        print('-'*37)
        self.marca = str(input("Digite a marca do carro: ")).upper()
        print('-'*37)
        self.modelo = str(input("Digite o modelo do carro: ")).upper()
        print('-'*37)
        self.aluguel = "DISPONIVEL"
        carro = {
            'placa': self.placa,
            'ano': self.ano,
            'categoria': self.categoria,
            'transmissao': self.transmissao,
            'combustivel': self.combustivel,
            'marca': self.marca,
            'modelo': self.modelo,
            'aluguel': self.aluguel
        }
        self.ListaCarro.append(carro)           
                       
class Cliente(Locadora):#Sub classe relacionada aos clientes e ligada a superclasse por parâmetro
    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        
    def alterar_cliente(self):#COMPLETO
        '''Este bloco modifica os dados de clientes previamente cadastrados'''
        print("\n")
        print("="*31)
        print("-=-=-   Alterar Cliente   -=-=-")
        print("="*31)
        print("\n")
        if len(self.ListaCliente) > 0:
            print('-'*31)
            self.cpf = str(input("Digite o CPF : ")).upper()
            print('-'*31)
            if Cliente.existe_cliente(self):
                for clt in self.ListaCliente:
                    if clt['cpf'] == self.cpf:
                        print('-'*31)
                        print(f"\n\tNome: {clt['nome']}")
                        print(f"\tCPF: {clt['cpf']}")
                        print(f"\tRG: {clt['rg']}")
                        print('-'*31)

                        print('-'*31)
                        clt['nome'] = str(input("Nome: ")).upper()
                        print('-'*31)
                        clt['cpf'] = str(input("CPF: "))
                        print('-'*31)
                        clt['rg'] = str(input("RG: "))
                        print('-'*31)

                        print('-'*31)
                        print(f"Os dados de {self.nome} foi alterado")
                        print('-'*31)
                        break
            else:
                print('-'*50)
                print("Esse CPF não está cadastrado")
                print('-'*50)
        else:
            print('-'*50)
            print("Não existem clientes a serem alterados!")
            print('-'*50)
        
    def listar_cliente(self):#COMPLETO
        '''Este bloco imprime na tela todos o clientes cadastrado olhando dentro da (ListaCliente)'''
        print("\n")
        print("="*33)
        print("-=-=-   Lista de Clientes   -=-=-")
        print("="*33)
        print("\n")
        if len(self.ListaCliente) > 0:
            for i, clt in enumerate(self.ListaCliente):
                print('-='*26)
                print(f"\nCliente {i+1}:")
                print(f"Nome: {clt['nome']}")
                print(f"CPF: {clt['cpf']}")
                print(f"RG: {clt['rg']}\n")
                print('-='*26)
            print(f"Total de clientes é: {len(self.ListaCliente)}\n")
            print("\n")
            print("="*33)
        else:
            print("\nNenhum cliente para listar!\n") 
            print("\n")
            print("="*28)   
        
    def buscar_cliente(self):#COMPLETO
        '''Este bloco procura pelo cpf se o cliente está cadastrado na (ListaCliente)'''
        print("\n")
        print("="*32)
        print("-=-=-   Procurar Cliente   -=-=-")
        print("="*32)
        print("\n")
        if len(self.ListaCliente) > 0:
            print('-='*26)
            self.cpf = str(input("Digite o cpf: ")).upper()
            print('-='*26)
            for car in self.ListaCliente:
                if car['cpf'] == self.cpf:
                    print('-'*32)
                    print(f"\nNome: {car['nome']}")
                    print(f"CPF: {car['cpf']}")
                    print(f"RG: {car['rg']}\n")
                    print('-'*32)
                    break
        else:
            print("\nNenhum cliente cadastrado no sistema!\n")
            print('-='*26)
    
    def existe_cliente(self):#COMPLETO
        '''Este bloco valida pelo cpf se o cliente já está cadastrado procurando dentro de (ListaCliente)'''
        if len(self.ListaCliente) > 0:
            for clt in self.ListaCliente:
                if clt['cpf'] == self.cpf:
                    return True
        return False    
        
    def novo_cliente(self):#COMPLETO
        '''Este bloco cadastra um novo cliente e deixa salvo na (ListaCliente)'''
        print("\n")
        print("="*38)
        print("-=-=-   Cadastrar Novo Cliente   -=-=-")
        print("="*38)
        print("\n")
        while True:
            print('-='*26)
            self.cpf = str(input("Digite seu CPF: "))
            print('-='*26)
            if not Cliente.existe_cliente(self):#Verifica se o cpf já está cadastrado
                break
            else:
                print('-'*38)
                print("Já cadastrado no sistema")
                print('-'*38)
        print('-'*38)
        self.nome = str(input("Digite seu nome: ")).upper()
        print('-'*38)
        self.rg = str(input("Digite seu RG: "))
        print('-'*38)
        
        usuario = {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg
        }
        self.ListaCliente.append(usuario)    
Locadora()
