import time
from random import randint

def verifica_ordem(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    return True

def cria_lista_aleatoria(n):
    l = []
    for i in range(n):
        l.append(randint(0,100))
    return l

def qsort(l):
    if len(l) > 1:
        pivot = l[0]
        menores = []
        maiores= []
        for i in range(1, len(l)):
            if l[i] <= pivot:
                menores.append(l[i])
            else:
                maiores.append(l[i])
        return qsort(menores) + [pivot] + qsort(maiores)
    else:
        return l 
    
def main():
    l = cria_lista_aleatoria(15)
    print(f"Lista Desordenada: {l}\n")
    t1 = time.time()
    l = qsort(l)
    t2 = time.time()
    print(f"Lista Ordenada: {l}\n")
    print(verifica_ordem(l))
    print(f'Tempo:  {t2-t1:.2f}s')
if __name__ == '__main__':
    main()