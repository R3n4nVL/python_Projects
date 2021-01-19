#primeira vez usando o método de "função"
#o progrma retorna o maior numero

def maximo(x,y):
    if x > y:
        return x
    else:
        return y


#Programa principal
x = int(input("Digite um valor:"))
y = int(input("Digite outro valor:"))

print(maximo(x, y))