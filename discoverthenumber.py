
import random

fim = 0
x = random.randint(0,100)
print(x)
while fim < 1:
        num = int(input("Digite um numero de 0 a 100: "))
        
        if num >= x + 20:
            print("Tá longe, numero muito alto")
        elif num >= x + 10:
            print("Tá perto, um pouco menos")
        elif num >= x + 5:
            print("Muito perto, um pouco menos")
        elif num in range(x,x+5):
            print("Quase passou raspando!!")
        if num <= x - 10:
            print("Tá longe, um pouco mais")
        elif num <= x - 5: 
            print("Quase! um pouco mais")
        elif num in range(x-5,x):
            print("Quase passou raspando!2")
        if num == x:
            print("Você acertou! O numero é {}".format(x))
            fim = 1
