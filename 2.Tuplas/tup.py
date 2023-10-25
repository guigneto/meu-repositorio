#Questao 1
def bonus(l):
  maior = l[0][1]
  for nome,mes,sal in l:
    if maior <= mes: 
      maior = mes
  for nome,mes,sal in l:
    if mes == maior:
      print(nome,sal*1.10)
#Questao 2
def lucro(produtos):
  menos20 = 0
  mais25 = 0
  for custo, venda in produtos:
    if venda < custo*1.20:
      menos20+=1 
    if venda > custo*1.25:
      mais25+=1
  print(f"{mais25} Produtos com mais de 25% de lucro")
  print(f"{menos20} Produtos com menos de 20% de lucro")

#Questao 3


#Questao 4 

def vooA(voos,origem,destino):
  for num,comp,escalas in voos:
    if escalas[0] == origem and escalas[-1] == destino:
      print (num,comp)

def vooB(voos,origem,destino):
  cont = 0
  for num,comp,escalas in voos:
    if escalas[0] == origem and destino in escalas:
        cont+=1
  print (cont)

def vooC(voos,origem,destino):
  for num,comp,escalas in voos:
    for i in range(len(escalas)-1):
      if escalas[i] == origem and escalas[i+1] == destino:
        return True
  return False

#Questao 5
def somaPontos(classificacao):
  soma = 0
  for _,pontos in classificacao:
    soma+=pontos
  return soma
def copaDoMundo(numJogos,classificacao):
  return 3*numJogos - somaPontos(classificacao)
  
def main():

  return 0
main()