#1 , se n = 1
#n * (n-1) * (n-2) * ... * 1, se n > 1

def fat(n): 
    if n == 1: 
        return 1 
    else: 
        return (n*fat(n-1)) #recursividade

def main():
    print(fat(5))
main()