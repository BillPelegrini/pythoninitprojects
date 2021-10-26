# SIMULADOR DE DADO
# Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir) e permitir que o usuário rode o script quantas vezes quiser.

# Habilidades praticas a aplicar:

# Tratamento de exceções
# Condicionais If/Else
# Input de dados
# Geração de valores
# Print
# Detalhes e boas Práticas: Você deve desenvolver um projeto em Python que irá rodar inicialmente na linha de comando e que, ao ser executado, deverá pergunta o seguinte ao usuário: “Você gostaria de jogar o dado?” Ou alguma variação dessa pergunta. Depois de ter feito essa pergunta, o seu programa precisa avaliar a resposta que foi digitado pelo usuário.

# Um passo importante aqui é que, quando digo avaliar quero dizer que você precisa receber o valor, tratar quando ele(a) disser que sim ou que não. Seu programa depois deverá fazer a ação necessária de acordo com a resposta que foi entrada pelo usuário. Seu script não deve quebrar ou para de funcionar caso o usuário entre algo que não seja esperado, como, por exemplo, um número. Trate as exceções ou erros para que seu script rode liso e sem problemas.

# Caso a resposta a pergunta inicial tenha sido “sim” ou positiva de alguma forma, gere um valor aleatoriamente entre 1 e 6(você pode claro alterar essa faixa) e exiba o número no console para o usuário. Na sequência pergunte se ele(a) quer rodar o script novamente e trate essa situação para que continue rodando enquanto a resposta for positiva, fechando apenas quando for um “não”.

import random

def show_dice(num):
    if num == 1:
        print("-----")
        print("|   |")
        print("| o |")
        print("|   |")
        print("-----")

    if num == 2:
        print("-----")
        print("|o  |")
        print("|   |")
        print("|  o|")
        print("-----")

    if num == 3:
        print("-----")
        print("|o  |")
        print("| o |")
        print("|  o|")
        print("-----")
    
    if num == 4:
        print("-----")
        print("|o o|")
        print("|   |")
        print("|o o|")
        print("-----")
    
    if num == 5:
        print("-----")
        print("|o o|")
        print("| o |")
        print("|o o|")
        print("-----")
    
    if num == 6:
        print("-----")
        print("|o o|")
        print("|o o|")
        print("|o o|")
        print("-----")


print("|----------*-------------*----------|")
print("|----------* Dice Roller *----------|")
print("|----------*-------------*----------|")

print("  ____")
print(" /\\' .\   _____")
print("/: \___\ / .  /\\")
print("\\' / . //____/..\\")
print(" \/___/ \\'  '\  /")
print("         \\'__'\/")

choice = input("\nDo you wanna roll a dice? Y/n: ")
choice = choice.lower()
while choice == "y":
    diceresult = random.randint(1,6)
    print("Your dice result is: {}" .format(diceresult))
    diceimage = show_dice(diceresult)
    choice = input ("Do yout wanna play again ?")
    choice = choice.lower()
if choice == "n":
    print("Thanks, see you next time, Bye!")
else: 
    print("Please, only letters Y or N are allowed!")
    choice == "y"






