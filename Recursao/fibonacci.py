def fibRec(n): #recursivo
    if n == 0: return 0;
    elif n ==1: return 1;
    else:
        return fibRec(n-1) + fibRec(n-2)

def fibIt(n): #iterativo
    x = 1;
    y = 1;
    for i in range (n-2):
        soma = x + y
        x = y
        y = soma
    return y

    
def main():
    print(fibRec(8))
    print(fibIt(8))
main()