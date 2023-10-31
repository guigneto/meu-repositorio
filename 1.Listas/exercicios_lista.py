#Questao 1:
def regressiva(l):
  l2 = []
  for i in l:
    if i % 2 == 0:
      l2.append[i]
  l2.reverse()
  return l2


#Questao 2:
def metade():
  l = []
  for i in range(10):
    n = float(input(""))
    l.append(n / 2)
  print(l)


#Questao 3
def leitura(n):
  i = 0
  l = []
  while i < n:
    x = int(input("numero"))
    l.append(x)
    i += 1
  return l


#Questao 4
def ocorrencias(l, x):
  n = 0
  for i in l:
    if i == x:
      n += 1
  return n


#Questao 5
def maximo(l):
  m = l[0]
  for i in l:
    if i > m:
      m = i
  return m


#Questao 6
def posMax(l):
  p = 0
  for i in range(len(l)):
    if l[i] > l[p]:
      p = 1
  return p

#Questao 7
def troca(l,i,j):
  aux=l[i]
  l[i]= l[j]
  l[j]= aux
def inverter(l):
  PosFinal= len(l)-1
  for i in range (len(l//2)):
    troca(l,i,PosFinal-i)

#Questao 8
def fi(n):
  l = [1,1]
  if n == 1:
    return [1]
  if n == 2:
    return [1,1]
  else: 
    for i in range (n-2):
      l.append(l[-1]+[-2])
    return l

#Questao 10
def multiplos(k,n):
  l=[]
  j = 0
  i = 0
  while i < k:
    j = j + n
    l.append(j)
    i+=1
  return l

#Questao 11
def media(n):
  l = []
  passou = 0
  j =1
  for i in range ((n)-1):
    nota = float(input(f"Nota aluno {j}: "))
    j+=1
    l.append(nota)
  med = sum(l)/len(l)
  for m in l:
    if m >= 60:
      passou +=1
  print (med, passou)
    
#Questao 12
#def temperatura(n):

#Questao 13:
def iguais(l1,l2):
  a = 0
  for i in range (len(l1)):
    if l1(i)==l2(i):
      a+=1
    i+=1
  print (a)

#Questao 14
def salarios(n):
  l= []
  l2=[]
  for i in range ((n)-1):
    nome = input("Nome: ")
    sal= float(input("Salario: "))
    j = nome,sal
    l.append(j)
  for a,b in l:
    l2.append(b)
  media = sum(l2)/len(l)
  #print (media)
  for a,b in l:
    if b > media:
      print (a)

#Questao 15
def sublista(l,x,y):
  sl = []
  return True

#Questao 16
def semRepeticao(l):
  l2=[l[0]]
  for item in l:
    if item != l2[-1]:
      l2.append(item)
  return l2
def trocaL(l1,l2):
  l1=semRepeticao(l1)
  l2=semRepeticao(l2)
  trocasA = 0
  for carta in l1:
    if carta not in l2:
      trocasA+=1
  trocasB = 0
  for carta in l2:
    if carta not in l1:
      trocasB +=1
  return min(trocasA,trocasB)
  
#Questao 17
def criaMatriz(m,n):
  M=[]
  for i in range (m):
    M.append(n*[0])
  return M
  
#Questao 18
def imprimeMatriz(M):
  for i in M:
    for j in i:
      print(M[i][j], end='\t')
    print()

#Questao 19
def somaMatrizes(A,B):
  nLinhas = len(A)
  nColunas = len(A[0])
  C = criaMatriz(nLinhas,nColunas)
  for i in range (nLinhas):
    C[i][j] = A[i][j] + B[i][j]
  return C

#Questao 20
def lerNotas(m,n):
  alunos = []
  notas = []
  for i in range(m):
    for j in range (n):
      nota = int(input("Digite a nota {} do aluno {}: ".format(i+1,j+1)))
      notas.append(nota)
    alunos.append(notas)
  return alunos
def medias():
  m = int(input("Digite o numero de alunos: "))
  n = int(input("Digite o numero de avaliacoes: "))
  alunos = lerNotas(m,n)
  somaTotal = 0
  for i in range (m):
    somaAluno = 0
    for nota in alunos[i]:
      somaAluno += nota
    mediaAluno = somaAluno/len(alunos[i])
    somaTotal += mediaAluno
    print("Aluno {}: {}".format(i+1,mediaAluno))
  mediaTotal = somaTotal/len(alunos)
  print("Media da turma: {}".format(mediaTotal))

#Questao 21
  
def main():
  salarios(5)

main()