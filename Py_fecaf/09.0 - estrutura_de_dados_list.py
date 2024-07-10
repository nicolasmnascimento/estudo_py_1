    #Manipulando listas - list

#Criando uma lista
nomes = ["Ana", "Pedro"]

print (f"Lista original: {nomes}")


#"cont" para contar o número de repetições e "append" para adicionar novos dados dentro da list
for cont in range (1):
    novo_nome = input(f"Digite seu nome {cont} : " )
    nomes.append (novo_nome)

print (f"Lista adicionando nome: {nomes}")



#Adicionando n quantidades de nomes com "while"
resp = "S"
while resp == "S":
    novo_nome = input(f"Digite seu nome {cont} : " )
    nomes.append (novo_nome)
    resp = input ("Deseja cadastrar mais um nome [S/N]: ")

    print (f"Lista adicionando n nomes: {nomes}")

 #Listando elementos pela posição
print (nomes[0])

#Removendo o último elemento da lista
nomes.pop ()
print (f"Removendo o último: {nomes}")

#Removendo um elemento qualquer
nomes.remove ("Pedro")
print (f"Removendo um elemento qualquer: {nomes}")

#Verificando a existência de um elemento
nome_pesquisado = input ("Digite um nome para pesquisar: ")
if nome_pesquisado in nomes:
    print ("Nome cadastrado")
else:
    print ("Nome não cadastrado")