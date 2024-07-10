#Estrutura de controle de vendas

#Adicionar produtos

estoque_id= {
    "Manga": {"preco":3.50, "quantidade":10},
    "Laranja": {"preco":10.00, "quantidade":20},
    "Goiaba": {"preco":5.60, "quantidade":6},
    "Morango": {"preco":7.00, "quantidade":12},
    "Uva": {"preco":15.00, "quantidade":30}      
    }

nome = input("Digite o nome do produto: ")
if nome in estoque_id:
        print("Produto já existe no estoque!")
else:
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    estoque_id[nome] = {"preço": preco, "quantidade": quantidade}
    print(f"Produto {nome} adicionado com sucesso!")
    print (estoque_id)

#Atualizar o produto

nome = input("Digite o nome do produto a ser atualizado: ")
if nome not in estoque_id:
            print("Produto não encontrado!")
else:
    preco = float(input("Digite o novo preço do produto: "))
    quantidade = int(input("Digite a nova quantidade em estoque: "))
    estoque_id[nome] = {"preço": preco, "quantidade": quantidade}
    print(f"Produto {nome} atualizado com sucesso!")
    print (estoque_id)

#Visualizar estoque
estoque_real = input("Qual produto deseja consultar?: ")
print(f"O item {estoque_real} tem em estoque {estoque_id[nome]}")


