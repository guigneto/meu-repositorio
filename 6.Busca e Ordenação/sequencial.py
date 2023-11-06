l = [("Joao", "123.456.789-00"), ("Jose", "234.567.891-00"),
     ("Maria", "345.678.912-00"), ("Ana", "456.789.123-00")]

# Busca Sequencial


def busca(x, l):  # Nesta funcao , l eh uma lista de tuplas , e o elemento eh procurado sempre na primeira posicao de cada tupla
    for i in range(len(l)):
        if l[i][0] == x:
            return i
    return -1


def main():
    l1 = [3, 16, 5, 8, 9, 2, 1, 15, 6]
    x = int(input("Digite um número: "))
    if x in l1:
        print("Encontrei")
    else:
        print("Ops... ta aqui não!")

    l2 = [("Joao", "123.456.789-00"), ("Jose", "234.567.891-00"),
          ("Maria", "345.678.912-00"), ("Ana", "456.789.123-00")]
    if busca("Ana", l2):
        print("tem")
    return 0


main()
