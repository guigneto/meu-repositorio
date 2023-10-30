clientes = {"123.456.789-00": ("Maria da Silva", "maria@gmail.com"), "234.567.890-00": (
    "Joao da Cruz", "joao@gmail.com"), "345.678.900-00": ("Jose de Souza", "zezinho@gmail.com")}

produtos = {"A0001": (1.20, "Pera", 1), "A0002": (3.40, "Uva", 1), "A0003": (1.00, "Maca", 1), "A0004": (
    10.00, "Salada de frutas", 1), "A0005": (12.00, "Acai medio", 1), "A0006": (3.00, "Granola", 1), "A0007": (5.00, "Suco 300ml", 1)}


pedidos = {"345": ("123.456.789-00", True, [("A0001", 3), ("A0002", 1), ("A0003", 5),
                   ("A0004", 1)]), "123": ("234.567.890-00", False, [("A0005", 2), ("A0006", 1)])}


def verificaEstoque(codProduto, produtos, pedidos):
    qtd = produtos[codProduto][2]

    for codPed in pedidos:
        cpf, status, lista = pedidos[codPed]
        if not status:
            for codProd, qtdProd in lista:
                if codProd == codProduto:
                    qtd -= qtdProd
    if qtd >= 0:
        print(f"Quantidade suficiente de {produtos[codProduto][1]}")
    else:
        print(f"Quantidade insuficiente de {produtos[codProduto][1]}")


def imprimePedido(codPedido, produtos, pedidos):
    print(f"Pedido #{codPedido}")
    cpf, status, lista = pedidos[codPedido]
    for codProd, qtdProd in lista:
        nomeProduto = produtos[codProd][1]
        valorUnitario = produtos[codProd][0]
        valorTotal = valorUnitario*qtdProd
        print(
            f"-{nomeProduto}\n Qtd:{qtdProd}\n Valor unitario: R$ {valorUnitario:.2f}\n Valor total: R$ {valorTotal:.2f}")
    if status == False:
        print('Status: Em aberto')
    else:
        print("Status: Entregue")

# def valorTotalPedido(codPedido,clientes,produtos,pedidos):
#     valorTotal = 0
#     cliente = pedidos[codPedido][0]
#     cpf,status,lista = pedidos[codPedido]
#     for codProd,qtdProd in lista:
#         valorUnitario = produtos[codProd][0]
#         valorTotal += (valorUnitario*qtdProd)
#     print (f"Cliente {clientes[cliente][0]} gastou R$ {valorTotal:.2f}")


def valorTotalPedido(codPedido, produtos, pedidos):
    valorTotal = 0
    cpf, status, lista = pedidos[codPedido]
    for codProd, qtdProd in lista:
        valorUnitario = produtos[codProd][0]
        valorTotal += (valorUnitario*qtdProd)
    return valorTotal


def valorTotalCliente(clientes, produtos, pedidos):
    for codPedidos in pedidos:
        cliente = pedidos[codPedidos][0]
        print(
            f"Cliente {clientes[cliente][0]} gastou R$ {valorTotalPedido(codPedidos,produtos,pedidos):.2f}")


def main():
    clientes = {"123.456.789-00": ("Maria da Silva", "maria@gmail.com"), "234.567.890-00": (
        "Joao da Cruz", "joao@gmail.com"), "345.678.900-00": ("Jose de Souza", "zezinho@gmail.com")}

    produtos = {"A0001": (1.20, "Pera", 1), "A0002": (3.40, "Uva", 1), "A0003": (1.00, "Maca", 1), "A0004": (
        10.00, "Salada de frutas", 1), "A0005": (12.00, "Acai medio", 1), "A0006": (3.00, "Granola", 1), "A0007": (5.00, "Suco 300ml", 1)}

    pedidos = {"345": ("123.456.789-00", True, [("A0001", 3), ("A0002", 1), ("A0003", 5),
                       ("A0004", 1)]), "123": ("234.567.890-00", False, [("A0005", 2), ("A0006", 1)])}
    codPedido = "345"
    codProduto = "A0006"
    print(verificaEstoque(codProduto, produtos, pedidos))
    print(imprimePedido(codPedido, produtos, pedidos))
    print(valorTotalPedido(codPedido, clientes, produtos, pedidos))
    print(valorTotalCliente(clientes, produtos, pedidos))
    return 0


main()
