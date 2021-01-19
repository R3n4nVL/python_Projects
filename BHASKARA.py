import math

a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))

k = b**2 - 4*a*c
#DELTA

if k > 0:
#DUAS RAIZES REAIS
    r = math.sqrt(k)

    X = (- b + r) / 2 * a
    Y = (- b - r) / 2 * a

    if X>Y:
        t1 = Y
        t2 = X
    else:
        t1 = X
        t2 = Y


    print("as raízes da equação são",t1,"e",t2)

else:
    print("esta equação não possui raízes reais")
#NENHUMA RAIZ

if k == 0:
    
    r = math.sqrt(k)
    X = (- b + r) / 2 * a

    print("a raiz desta equação é", X)

#APENAS UMA RAIZ




