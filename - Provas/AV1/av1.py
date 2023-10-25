usuarios = {"pkchu":("Pikachu","Kanto",(4,12,2000)),"drgnt":("Dragonite","Kanto",(1,10,2002)),"jpuff":("Jigglypuff","Kanto",(15,2,1988)),"blssy":("Blissey","Johto",(2,3,2000)),"trntr":("Tyranitar","Johto",(28,6,2001))}
conexoes = {"pkchu":(["blssy"],["jpuff"]),"drgnt":(["jpuff"],[]),"jpuff":([],["pkchu","trntr"]),"blssy":(["drgnt"],["trntr"]),"trntr":([],["blssy","jpuff"])}

def buscaDisponiveis(login,conexoes):
    l = []
    gostou,mutuos = conexoes[login]
    for user in conexoes:
        if user not in gostou or mutuos:
            l.append(user)
        l.pop(login)
        return l[0:20]

def main():
    usuarios = {"pkchu":("Pikachu","Kanto",(4,12,2000)),"drgnt":("Dragonite","Kanto",(1,10,2002)),"jpuff":("Jigglypuff","Kanto",(15,2,1988)),"blssy":("Blissey","Johto",(2,3,2000)),"trntr":("Tyranitar","Johto",(28,6,2001))}
    conexoes = {"pkchu":(["blssy"],["jpuff"]),"drgnt":(["jpuff"],[]),"jpuff":([],["pkchu","trntr"]),"blssy":(["drgnt"],["trntr"]),"trntr":([],["blssy","jpuff"])}
    login = "pkchu"
    print(buscaDisponiveis(login,conexoes))
main()