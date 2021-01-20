def esb():
    print("-=-"*13)

linha = 1
coluna = 1

esb()
print("\t\t\tTABUADA")
esb()

while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end="\t")
        coluna = coluna + 1
#no final da execução acima coluna = 11 porém ele executa quando valer 10 o "while coluna"
    linha = linha + 1
    print()
    coluna = 1
# é necessario para executar o trecho do código no laço - while "coluna"