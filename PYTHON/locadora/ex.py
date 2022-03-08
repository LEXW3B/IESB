    

    


from xmlrpc.client import Boolean


def principal():

    while True:
        print('-=-=-= Bem-vindo a Locadora Boa Viagem, escolha uma das oopções abaixo: -=-=-=')
        print('==============================================================================')
        print('1 - Cadastrar um Novo Veiculo')
        print('2 - Cadastrar um Novo Cliente')
        print('3 - Realizar a locaçção de um Veiculo')
        print('4 - Relatório de locação')
        print('==============================================================================')

        menu = int(input('Digite o numero de uma opcao acima: ')).strip()

        while menu not in int:
            menu = int(input('Digite o numero de uma opcao acima: ')).strip()

    if menu == 1:
        print('esta funcionando')
    else :
        print('nao funciona')
    # else if == 3:
    #     print('nao funciona')
    # else if == 4: 
    #     print('nao funciona')   
            
    
    # def cadastrar_veiculos():    
    # carro = {
    #     'Categoria:' ['Sedan', 'Picape', 'SUV'],
    #     'Transmissão:' ['automática', 'manual'],
    #     'Combustivel:' ['Diesel', 'Álcool', 'Gasolina', 'Flex', 'GNV'],
    #     'Marca:' ['Ford'],
    #     'Modelo:' ['EcoEsport']
        
    # }


principal()













