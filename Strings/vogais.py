def vogais(palavra):
    A = False
    E = False
    I = False
    O = False
    U = False
    
    for i in range(len(palavra)):
        if (palavra[i] == 'A'):
            A = True
        elif (palavra[i] == 'E'):
            E = True
        elif (palavra[i] == 'I'):
            I = True
        elif (palavra[i] == 'O'):
            O = True
        elif (palavra[i] == 'U'):
            U = True
    
    vogais = ""
    if (A):
        vogais += " A "
    if (E):
        vogais += " E "
    if (I):
        vogais += " I "
    if (O):
        vogais += " O "
    if (U):
        vogais += " U "
    return vogais


def main():

    palavra = input("Palavra: ")
    print (f'Vogais: {vogais(palavra)}')
    
    return 0
main()