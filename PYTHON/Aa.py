#adicionar categorias
def new_category():
    carro.push()

#adicionar cliente
def new_client ():
    cliente.push()

#alugar um carro
def rent_a_car ():
    cliente.pop()
    
#relatorio de locação
def lease_report ():
    cliente.push()

print('-=-=-= Bem-vindo a Locadora Boa Viagem, escolha uma das oopções abaixo: -=-=-=')
print('==============================================================================')
print('1 - Cadastrar um Novo Veiculo')
print('2 - Cadastrar um Novo Cliente')
print('3 - Realizar a locaçção de um Veiculo')
print('4 - Relatório de locação')
print('==============================================================================')

menu = int(input('Digite o numeros de uma opção acima: '))

# cliente = {
#     'Nome': 'José da Silva',
#     'CPF': 89775452,
#     'RG': 789546
# }

# carro = {
#     'categoria': ['Sedan', 'Picape', 'SUV'],
#     'transmissão': ['automático', 'manual'],
#     'tipo combustível': ['Diesel', 'Álcool', 'Flex', 'GNV'],
#     'Marca': ['Ford', 'Volkswagen', 'Honda'],
#     'Modelo': ['EcoSport', 'Gol', 'corolla']
# }

