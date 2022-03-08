
def cadastrar_veiculos():



   
def writeInt (msg):#validação de menu
    ok = False
    valor = 0
    while True:
        menu = str(input(msg))
        if menu.isnumeric():
            valor = int(menu)
            ok = True
        else:
            print('ERROR! Digite um numero valido: ')
        if ok:
            break
            return menu, valor
        
carro = {
    'Categoria:' ['Sedan', 'Picape', 'SUV'],
    'Transmissão:' ['automática', 'manual'],
    'Combustivel:' ['Diesel', 'Álcool', 'Gasolina', 'Flex', 'GNV'],
    'Marca:' ['Ford'],
    'Modelo:' ['EcoEsport']
}

while True:
    print('-=-=-= Bem-vindo a Locadora Boa Viagem, escolha uma das oopções abaixo: -=-=-=')
    print('==============================================================================')
    print('1 - Cadastrar um Novo Veiculo')
    print('2 - Cadastrar um Novo Cliente')
    print('3 - Realizar a locação de um Veiculo')
    print('4 - Relatório de locação')
    print('==============================================================================')
    menu = writeInt('Digite o numero de uma opcao acima: ')
    
    if menu == 1:
        print('esta funcionando')
    else :
        print('nao funciona com outro numero letra ou palavras')
    # else if == 3:
    #     print('nao funciona')
    # else if == 4: 
    #     print('nao funciona')   


    # def cadastrar_veiculos():    
    # 
















