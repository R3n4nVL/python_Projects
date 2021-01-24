# EXPONENCIAÇÃO


n = 0
z = int(input("Digite a Base:"))
count = int(input("Digite o range do expoente:"))


while n != count:
    x = z**n
    print("{}**{} = {} ".format(z, n, x))
    n += 1



#Ex:        2 -> Expoente
#          8 |  =  64
#     base <-|
