def éPrimo(k):
    for i in range(2,k):
        if k % i == 0:
            return maior_primo(k)
    return k





def maior_primo(k):
    for k in reversed(range(1,k+1)):
        if all(k % i!=0 for i in range(2,k)):
            return k


