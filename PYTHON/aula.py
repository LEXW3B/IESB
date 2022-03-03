
texto = 'ola mundo'
print(type(texto))

listas = [1,2,3,4,5]
print(type(listas[2]))

lista1 = []
lista1 = listas
print(lista1)

dicionario = {"melhor amigo":"Jailson","inimigo": "estevão"}
print(dicionario)
dicionario["melhor amigo"]

#montando uma lista
lista=list(range(1,30))
lista

#montando listas incrementais
pares=list(range(0,20,2))
print(pares)

impares=list(range(1,20,2))
print(impares)

#Estruturas condicionais
a = 11
if(a<10):
    print('maIOR QUE 10')
else :
    print('menor que 10')

# Crie um programa  que verifique se o numero de uma lista é impar ou PAR
for i in listas:
    if i%2 == 0:
        print(f'numero {i} par')
    else:
        print(f'o numero {i} e impar')


#estruturas de repetição
a=10
soma=0
while a>1:
  soma=soma+a
  a=a-1
print(soma)

soma=0
for i in impares:
  soma=soma+i
print(soma)

#tem um jeito fácil
soma=sum(impares)
print(soma)

class MyClass:
    """
    Aqui eu vou colocar
    uma string que define as
    principais informações sobre
    a classe que estou criando
    """
    
    atributo_da_classe = 1234
    outro_atributo = 5678
    
    def metodo_da_classe(self):
        return 'Olá povo!'

x = MyClass()
y = MyClass()

x

x.atributo_da_classe

x.outro_atributo = 99999
print(x.outro_atributo)
print(y.outro_atributo)

x




