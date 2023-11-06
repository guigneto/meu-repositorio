import time
import random
def cria_lista(n): # cria uma lista de tamanho n com elementos aleatórios
    l = []
    for i in range(n):
        l.append(random.randint(0, 10000))
    return l

def troca(l, i, j): # troca o elemento i pelo elemento j
    aux = l[i]
    l[i] = l[j]
    l[j] = aux

def bubble1(l): # ordena a lista l por bubble sort
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                troca(l, j, j+1)
    return l

def bubble2(l): # ordena a lista l por bubble sort
    for i in range(len(l)):
        trocou = False
        for j in range (0, len(l)-i-1):
            if l[j] > l[j+1]:
                troca(l, j, j+1)
                trocou = True
        if not trocou:
            return l

def main(): 
    l = cria_lista(10000) # cria uma lista de tamanho 10000
    # print(f"->Lista Desordenada: {l}\n") 
    # time1 = time.time() 
    # print(f"->Lista Ordenada:{bubble1(l)}\n") 
    # time2 = time.time() 
    # print(f"Tempo: {time2 - time1:.2f} segundos\n") # imprime o tempo de execução
    return 0
if __name__ == '__main__':
    main()  # chamada da função principal