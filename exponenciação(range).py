# EXPONENCIAÇÃO


count = 1
z = int(input("Digite a Base:"))
n = int(input("Digite o range do expoente:"))


while count <= n:
    x = z**count
    print("{}**{} = {} ".format(z, count, x))
    count += 1



#Ex:        2 -> Expoente
#          8 |  =  64
#     base <-|
