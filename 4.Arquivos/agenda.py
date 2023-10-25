import os

def limpaTela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")




def agenda():
    print("Escolha uma opção:\n(1)Cadastrar Número\n(2)Visualizar Agenda\n(3)Excluir Agenda\n(4)Sair\n----------")
    opcao = str(input("Opção: "))
    while opcao != "4":
        limpaTela()
        if opcao == "1":
            nome = str(input("Nome: "))
            numero = str(input("Número: "))
            f = open("./Arquivos/agenda.txt","a")
            f.write(f"Nome: {nome}\nNúmero: {numero}\n----------\n")
            f.close()
            limpaTela()            
            print("Escolha uma opção:\n(1)Cadastrar Número\n(2)Visualizar Agenda\n(3)Excluir Agenda\n(4)Sair\n----------")
            opcao = str(input("Opção: "))
            print("Escolha uma opção:\n(1)Cadastrar Número\n(2)Visualizar Agenda\n(3)Excluir Agenda\n(4)Sair\n----------")

        elif opcao == "2":
            limpaTela()
            a = open("./Arquivos/agenda.txt","r")
            for linha in a:
                print(linha)
            a.close()
            voltar = str(input("Digite qualquer coisa para VOLTAR: "))
            limpaTela()
            if len(voltar) > 0:
                print("Escolha uma opção:\n(1)Cadastrar Número\n(2)Visualizar Agenda\n(3)Excluir Agenda\n(4)Sair\n----------")
                opcao = str(input("Opção: "))

        elif opcao == "3":
            f = open("./Arquivos/agenda.txt","w")
            f.write("")
            f.close()
            limpaTela()
            print("Escolha uma opção:\n(1)Cadastrar Número\n(2)Visualizar Agenda\n(3)Excluir Agenda\n(4)Sair\n----------")
            opcao = str(input("Opção: "))
            
        else:
            print("----------\nOpção inválida, tente novamente\n----------")
            print("Escolha uma opção:\n(1)Cadastrar Número\n(2)Visualizar Agenda\n(3)Excluir Agenda\n(4)Sair\n----------")
            opcao = str(input("Opção: "))
    limpaTela()
    print("Tchau! =D")
    return 0
agenda()
