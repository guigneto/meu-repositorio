import random, matplotlib.pyplot as plt

'''
Funcoes para visualizar um caminho do TSP na tela
'''

def showTSP(caminho, titulo):
	xs = [coords[0] for (cidade, coords) in caminho]
	ys = [coords[1] for (cidade, coords) in caminho]
	nomes = [cidade for (cidade, coords) in caminho]
	
	for i in range(len(xs)):
		plt.annotate(nomes[i], # this is the text
						(xs[i],ys[i]), # this is the point to label
						textcoords="offset points", # how to position the text
						xytext=(5,5), # distance from text to points (x,y)
						ha='center') # horizontal alignment can be left, right or center

	plt.plot(xs+[xs[0]], ys+[ys[0]], 'pb-')
	plt.plot([xs[0]], [ys[0]], 'pb-', color='red')
	
	t = "{} (Custo: {:.2f})".format(titulo, custo(caminho))
	plt.suptitle(t)
	plt.gca().set_aspect('equal', adjustable='box')
	
	plt.show()

def show2OPT(caminho, A, B):
	xs = [coords[0] for (cidade, coords) in caminho]
	ys = [coords[1] for (cidade, coords) in caminho]
	nomes = [cidade for (cidade, coords) in caminho]
	
	for i in range(len(xs)):
		plt.annotate(nomes[i], # this is the text
						(xs[i],ys[i]), # this is the point to label
						textcoords="offset points", # how to position the text
						xytext=(5,5), # distance from text to points (x,y)
						ha='center') # horizontal alignment can be left, right or center

	plt.plot(xs, ys, 'pb-')
	plt.plot([xs[0]], [ys[0]], 'pb-', color='red')

	xs = (caminho[A][1][0], caminho[A+1][1][0])
	ys = (caminho[A][1][1], caminho[A+1][1][1])
	plt.plot(xs, ys, 'pb-', color='red')	

	xs = (caminho[B][1][0], caminho[B+1][1][0])
	ys = (caminho[B][1][1], caminho[B+1][1][1])
	plt.plot(xs, ys, 'pb-', color='red')	

	xs = (caminho[A][1][0], caminho[B][1][0])
	ys = (caminho[A][1][1], caminho[B][1][1])
	plt.plot(xs, ys, 'pb--', color='gray')	

	xs = (caminho[A+1][1][0], caminho[B+1][1][0])
	ys = (caminho[A+1][1][1], caminho[B+1][1][1])
	plt.plot(xs, ys, 'pb--', color='gray')	

	t = "Trocando arestas (Custo atual: {:.2f})".format(custo(caminho, True))
	plt.suptitle(t)
	plt.gca().set_aspect('equal', adjustable='box')
	
	plt.show()

'''
Permutacoes
'''

def troca(l, x, y):
	aux = l[x]
	l[x] = l[y]
	l[y] = aux

def perms(l, pos=0):
	if pos == len(l)-1:
		return [ l.copy() ]
	else:
		result = []
		for i in range(pos, len(l)):
			troca(l, pos, i)
			result += perms(l, pos+1)
			troca(l, pos, i)
		return result
		
def tsp(cidades):
	caminhos = perms(cidades, 1)
	
	melhor = caminhos[0]
	
	for caminho in caminhos:
		if custo(caminho) < custo(melhor):
			melhor = caminho
	
	return melhor

#def tsp( cidades ):


'''
Funcoes auxiliares para o TSP
'''

def dist( p1, p2 ):
	x1, y1 = p1
	x2, y2 = p2
	
	return ( (y2-y1)**2 + (x2-x1)**2 ) ** 0.5 

def custo (caminho):
	c = 0
	
	for i in range(len(caminho) - 1):
		c += dist( caminho[i][1], caminho[i+1][1] )
		
	c += dist( caminho[-1][1], caminho[0][1])
	
	return c
	
	

'''
Vizinho Mais Próximo
'''
	
def nn(cidades):
	pos = 0
	
	while pos < len(cidades)-1:
		maisProx = pos+1
		
		for i in range(pos+2, len(cidades)):
			d1 = dist(cidades[pos][1], cidades[maisProx][1])
			d2 = dist(cidades[pos][1], cidades[i][1])
			
			if d2 < d1:
				maisProx = i
		
		troca(cidades, pos+1, maisProx)
		pos += 1

'''
2-OPT
'''


'''
Funcao para gerar cidades aleatorias
'''

#def printRota( caminho ):

def gerarCidades():
	cidades = []
	n = int(input("Digite o número de cidades: "))
	
	for i in range(n):
		nome = chr(i+ord('A'))
		x = random.randint(0, 400)
		y = random.randint(0, 300)
		
		cidades.append( (nome, (x, y)) )
	
	return cidades




def main(args):
	
	#cidades = [ ("A", (0,4)), ("B", (1,0)), ("C", (1,1)), ("D", (2,2)), ("E", (3,2)), ("F", (3,3)), ("G", (4,1)) ]
	cidades = gerarCidades()
	print (cidades)
	showTSP(cidades, "Ordem Inicial")
	
	rotaNN = cidades.copy()
	nn(rotaNN)
	showTSP(rotaNN, "Nearest Neighbor")
	
	#rota = tsp(cidades)
	#showTSP(rota, "TSP")
	

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))