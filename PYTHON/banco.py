
class banco:
    listaDeContas = []

    def iniciaConta(self):
        nome = input('Digite seu nome: \n')
        numero = input('Digite o numero da conta: \n')
        novaConta = conta(nome, numero)
        self.listaDeContas.append(novaConta)
        self.menuBanco()
        
    def acessarConta(self):
        numero = input('Por favor entre com o numero da conta: \n')
        for conta in self.listaDeContas:
            if(numero == conta.numero):
                conta.menu()
                
    def excluirConta(self):
        numero = input('Por favor entre com o numero da conta: \n')
        for conta in self.listaDeContas:
            if(numero == conta.numero):
                print(conta.nome)