#Manipulando dicionarios

cliente = {
     "nome": "Leonid", 
    "cidade": "São roque",
    "nascimento": 1976,
    "Ativo": False
}
print (cliente)

#Verificar por chave
print (f"Verificação do indice por chave: {cliente["cidade"]}")

#Atualizar um dado
cliente["nascimento"] = 2000
print (f"Atualização de dado na chave: {cliente}")

#Apagar uma chave
del cliente["cidade"]
print (f"Exclusão de chave: {cliente}")