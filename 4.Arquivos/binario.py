import pickle


x = 5
y = 7
z = x+y
s = "Ola"
t = (1,2)
l = [x,y,z,s,t]
abias = "abias corpos"
with open("arq.bin","wb") as f:
    pickle.dump(l,f) #salvou uma LISTA
    pickle.dump("abias corpos",f)

with open("arq.bin","rb") as f:
    l = pickle.load(f) #l == lista // pickle.load lê a linha
    for item in l:
        with open("arq.txt","wt") as g:
            lista = str(l)
            g.write(lista)
        print(item)
    j = pickle.load(f)
    with open("arq.txt","at") as g:
        g.write("\n")
        g.write(j)
    print(j)