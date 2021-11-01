#0 1 1 2 3 5 8 13 21...
 
#numeros iniciais
num1 = 0
num2 = 1

#numero que será utilizado de indice para criação da lista e do iterador for:
numero = int(input("Digite um numero: "))

lista=[]

#for para iterar ate o numero digitado usando a formula de fibonnaci
#aqui a cada iteração em i ele adiciona na lista o valor de acordo com a formula
for i in range(numero):
        lista.append(num1)
        num1 = num1 + num2
        lista.append(num2)
        num2 = num2 + num1
            
#print da lista usando o numero digitado como limite do array e substituindo a virgula por espaços.
print(*lista[0:numero], sep=" ")

#https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci