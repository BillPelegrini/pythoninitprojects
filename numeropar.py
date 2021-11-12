def numeroPar(x):
    x = int(x)
    for i in range(1,x+1):
        if i % 2 == 0:
            print(i)



num = input()
numeroPar(num)
