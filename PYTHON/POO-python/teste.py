
#sem frufru

class Locadora(object):

    def __init__(self):
        self.ListaCliente = []
        self.ListaCarro = []
        self.AluguelCarro = []
        self.menu()

    def alugar(self):
        '''Este bloco verifica se o cpf ja está cadastrado, se não estiver ele leva para o bloco de cadastrar um novo cpf. Se o cpf já for cadastrado ai vai aparecer uma lista de carros para ser alugados'''
        print("\n")
        print("="*50)
        print("-=-=-   To Hire   -=-=-")
        print("="*50)
        print("\n")
        
        self.cpf = str(input("Digite o CPF: "))
        while True:
            if not Cliente.existe_cliente(self):
                print("Novo Cadastro!")
                Cliente.novo_cliente(self)
            else:
                break
            
        print("\n")    
        print("="*50)        
        Carro.listar_carro(self)
        Carro.buscar_carro_alugar(self)
        Locadora.lista_aluguel(self)
        print("="*50)
        print("\n")

    def listar_aluguel(self):
        '''Este bloco trás a lista dos carros para alugar'''
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
        print(self.AluguelCarro)

    def lista_alugados(self):
        '''Este bloco aluga os carros'''
        print("\n")
        print("="*50)
        print("-=-=-   rental cars   -=-=-")
        print("="*50)
        print("\n")
        
        if len(self.AluguelCarro) > 0:
            for i, loc in enumerate(self.AluguelCarro):
                print('-='*50)
                print(f"Carro {i+1}:")
                print('-='*50)
                print(f"Nome: {loc['nome']}")
                print('-='*50)
                print(f"CPF: {loc['cpf']}")
                print('-='*50)
                print(f"RG: {loc['rg']}\n")
                print('-='*50)
                print(f"Placa: {loc['placa']}")
                print('-='*50)
                print(f"Ano: {loc['ano']}")
                print('-='*50)
                print(f"Categoria: {loc['categoria']}")
                print('-='*50)
                print(f"Transmissão: {loc['transmissao']}")
                print('-='*50)
                print(f"Combustível: {loc['combustivel']}")
                print('-='*50)
                print(f"Marca: {loc['marca']}")
                print('-='*50)
                print(f"Modelo: {loc['modelo']}")
                print('-='*50)
                print(f"Aluguel:{loc['aluguel']}")
                print('-='*50)
            print(f"Total de veículos alugados é: {len(self.AluguelCarro)}\n")
        else:
            print("\nNenhum veículo alugado para listar! ")

    def menu(self):

        while True:
            print("Bem Vindo a locadora BOA VIADAGEM")
            print("1 - Cadastrar novo veículo")
            print("2 - Cadastrar novo cliente")
            print("3 - Locação de veículo")
            print("4 - Relatório de locação")
            print("5 - Busca de veículos cadastrados")
            print("6 - Busca de clientes cadastrados")
            print("7 - Relatório de veículos cadastrados")
            print("8 - Relatório de clientes cadastrados")
            print("9 - Alterar dados veículos cadastrados")
            print("10 - Alterar dados clientes cadastrados")
            print("11 - Finalizar o programa !!!")

            while True:
                try:
                    opc = int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nNão aceita letras!\n")

            if opc == 1:
                Carro.novo_carro(self)

            elif opc == 2:
                Cliente.novo_cliente(self)

            elif opc == 3:
                Locadora.alugar(self)

            elif opc == 4:
                Locadora.listar_aluguel(self)

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
                print("\nFinalizado!!!")
                break

            else:
                print("\nInválido!\n")


class Carro(Locadora):
    def __init__(self, placa, ano, categoria, transmissao, combustivel, marca, modelo, aluguel):
        self.placa = placa
        self.ano = ano
        self.categoria = categoria
        self.transmissao = transmissao
        self.combustivel = combustivel
        self.marca = marca
        self.modelo = modelo
        self.aluguel = aluguel

    def alterar_carro(self):
        if len(self.ListaCarro) > 0:
            self.placa = str(input("Digite a placa : ")).upper()
            if Carro.existe_carro(self):
                for car in self.ListaCarro:
                    if car['placa'] == self.placa:
                        print(f"\n\tPlaca: {car['placa']}")
                        print(f"\tAno: {car['ano']}")
                        print(f"\tCategoria: {car['categoria']}")
                        print(f"\tTransmissão: {car['transmissao']}")
                        print(f"\tCombustível: {car['combustivel']}")
                        print(f"\tMarca: {car['marca']}")
                        print(f"\tModelo: {car['modelo']}")
                        print(f"\tAluguel: {car['aluguel']}\n")

                        car['placa'] = str(input("Placa:")).upper()
                        car['ano'] = str(input("Ano:"))
                        Carro.categoria(self)
                        car['categoria'] = self.categoria
                        Carro.transmissao(self)
                        car['transmissao'] = self.transmissao
                        Carro.combustivel(self)
                        car['combustivel'] = self.combustivel
                        car['marca'] = str(input("Marca:")).upper()
                        car['modelo'] = str(input("modelo:")).upper()
                        car['aluguel'] = print(
                            f"\tAluguel: {car['aluguel']}\n")

                        print(f"Os dados da {self.placa} foram alterados")
                        break

            else:
                print(
                    f"Não existe veiculo cadastrado com a placa informado {self.placa}")
        else:
            print("Não existe veículo a ser alterado!")

    def listar_carro(self):
        if len(self.ListaCarro) > 0:
            for i, car in enumerate(self.ListaCarro):
                print(f"Carro {i+1}:")
                print(f"Placa: {car['placa']}")
                print(f"Ano: {car['ano']}")
                print(f"Categoria: {car['categoria']}")
                print(f"Transmissão: {car['transmissao']}")
                print(f"Combustível: {car['combustivel']}")
                print(f"Marca: {car['marca']}")
                print(f"Modelo: {car['modelo']}")
                print(f"Aluguel:{car['aluguel']}")
            print(f"Total de veículos é: {len(self.ListaCarro)}\n")
        else:
            print("\nNenhum veículo para listar! ")

    def buscar_carro(self):
        if len(self.ListaCarro) > 0:
            self.placa = str(input("Digite a placa: ")).upper()
            for car in self.ListaCarro:
                if car['placa'] == self.placa:
                    print(f"Placa: {car['placa']}")
                    print(f"Ano: {car['ano']}")
                    print(f"Categoria: {car['categoria']}")
                    print(f"Transmissão: {car['transmissao']}")
                    print(f"Combustível: {car['combustivel']}")
                    print(f"Marca: {car['marca']}")
                    print(f"Modelo: {car['modelo']}")
                    print(f"Aluguel:{car['aluguel']}")
                    break
        else:
            print("Nenhum veiculo cadastrado")

    # def buscar_carro_alugar(self):
    #     if len(self.ListaCarro) > 0:
    #         self.placa = str(input("Digite a placa: ")).upper()
    #         for car in self.ListaCarro:
    #             if car['aluguel'] == "ALUGADO":
    #                 print("Nenhum veiculo disponível para alugar TOPEZERA!")
    #             else:
    #                 if car['placa'] == self.placa:
    #                     print(f"Placa: {car['placa']}")
    #                     print(f"Ano: {car['ano']}")
    #                     print(f"Categoria: {car['categoria']}")
    #                     print(f"Transmissão: {car['transmissao']}")
    #                     print(f"Combustível: {car['combustivel']}")
    #                     print(f"Marca: {car['marca']}")
    #                     print(f"Modelo: {car['modelo']}")
    #                     print(f"Aluguel:{car['aluguel']}")
    #                     if car['aluguel'] == "ALUGADO":
    #                         print("O veículo já está locado!")
    #                     else:
    #                         car['aluguel'] = "ALUGADO"
    #     else:
    #         print("Nenhum veiculo disponível para alugar!!!")

    def existe_carro(self):
        if len(self.ListaCarro) > 0:
            for car in self.ListaCarro:
                if car['placa'] == self.placa:
                    return True
        return False

    def categoria(self):
        while True:
            print("1 - Sedan\n2 - Picape\n3 - SUV")
            while True:
                try:
                    ctg = int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nNão aceita letras!\n")

            if ctg == 1:
                self.categoria = "SEDAN"
                break
            elif ctg == 2:
                self.categoria = "PICAPE"
                break
            elif ctg == 3:
                self.categoria = "SUV"
                break
            else:
                print("\nInválida")

    def transmissao(self):
        while True:
            print("\n1 - Automático\n2 - Manual")
            while True:
                try:
                    trns = int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nNão aceita letras!\n")

            if trns == 1:
                self.transmissao = "AUTOMATICO"
                break
            elif trns == 2:
                self.transmissao = "MANUAL"
                break
            else:
                print("\nInválida")

    def combustivel(self):
        while True:
            print("\n1 - Gasolina\n2 - Álcool\n3 - Flex\n4 - Diesel\n5 - GNV")
            while True:
                try:
                    cmbst = int(input("\nDigite: "))
                    break
                except ValueError:
                    print("Não aceita letras!\n")

            if cmbst == 1:
                self.combustivel = "GASOLINA"
                break
            elif cmbst == 2:
                self.combustivel = "ALCOOL"
                break
            elif cmbst == 3:
                self.combustivel = "FLEX"
                break
            elif cmbst == 4:
                self.combustivel = "DIESEL"
                break
            elif cmbst == 5:
                self.combustivel = "GNV"
                break
            else:
                print("\nInválida")

    def novo_carro(self):

        while True:
            self.placa = str(input("\n\nplaca: ")).upper()
            if not Carro.existe_carro(self):
                break
            else:
                print("\nJá cadastrado no sistema")
        self.ano = int(input("Ano: "))

        Carro.categoria(self)

        Carro.transmissao(self)

        Carro.combustivel(self)

        self.marca = str(input("Digite a marca: ")).upper()
        self.modelo = str(input("Digite o modelo: ")).upper()
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
        print(self.ListaCarro)


class Cliente(Locadora):

    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

    def alterar_cliente(self):
        if len(self.ListaCliente) > 0:
            self.cpf = str(input("Digite o CPF : ")).upper()
            if Cliente.existe_cliente(self):
                for clt in self.ListaCliente:
                    if clt['cpf'] == self.cpf:
                        print(f"\n\tNome: {clt['nome']}")
                        print(f"\tCPF: {clt['cpf']}")
                        print(f"\tRG: {clt['rg']}")

                        clt['nome'] = str(input("Nome: ")).upper()
                        clt['cpf'] = str(input("CPF: "))
                        clt['rg'] = str(input("RG: "))

                        print(f"Os dados de {self.nome} foi alterado")
                        break

            else:
                print("Esse CPF não está cadastrado")
        else:
            print("Não existem clientes a serem alterados!")

    def listar_cliente(self):
        if len(self.ListaCliente) > 0:
            for i, clt in enumerate(self.ListaCliente):
                print(f"\nCliente {i+1}:")
                print(f"Nome: {clt['nome']}")
                print(f"CPF: {clt['cpf']}")
                print(f"RG: {clt['rg']}\n")
            print(f"Total de clientes é: {len(self.ListaCliente)}\n")
        else:
            print("\nNenhum cliente para listar!\n")

    def buscar_cliente(self):
        if len(self.ListaCliente) > 0:
            self.cpf = str(input("Digite o cpf: ")).upper()
            for car in self.ListaCliente:
                if car['cpf'] == self.cpf:
                    print(f"\nNome: {car['nome']}")
                    print(f"CPF: {car['cpf']}")
                    print(f"RG: {car['rg']}\n")
                    break
        else:
            print("\nNenhum cliente cadastrado no sistema!\n")

    def existe_cliente(self):
        if len(self.ListaCliente) > 0:
            for clt in self.ListaCliente:
                if clt['cpf'] == self.cpf:
                    return True
        return False

    def novo_cliente(self):
        while True:
            self.cpf = str(input("Digite o CPF: "))
            if not Cliente.existe_cliente(self):
                break
            else:
                print("Já cadastrado no sistema")
        self.nome = str(input("Nome do cliente: ")).upper()
        self.rg = str(input("RG: "))
        usuario = {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg
        }

        self.ListaCliente.append(usuario)
        print(self.ListaCliente)


Locadora()
