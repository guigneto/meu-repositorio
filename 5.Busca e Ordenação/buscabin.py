#Algoritimo de busca binaria
def buscaBin(x,l):
    inicio = 0
    fim = len(l)-1
    while inicio <= fim:
        meio = (inicio+fim)//2
        if x == l[meio]:
            return meio #True
        elif x < l[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1 #False

#Recursivo:
def buscaBinRec(x,l,inicio,fim):
    if inicio < fim:
        return -1
    meio = (inicio+fim)//2
    if x == l[meio]:
        return meio
    if x < l[meio]:
        return buscaBinRec(x,l,inicio,meio-1)
    else:
        return buscaBinRec(x,l,meio+1,fim)
    