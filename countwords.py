def countwords(txt):
    lista = txt.split(" ")
    lista1 = []
    for i in lista:
        contador = len(i)
        lista1.append(contador) 
    zip_iterator = zip(lista,lista1)
    
    maior = dict(zip_iterator)
    print(max(maior, key=maior.get))

text = input("Insira o Texto: ")
countwords(text)
