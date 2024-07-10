#Manipulando conjuntos - sets

usuarios = {"Ana", "Maria", "Ana"}
usuarios_novos = usuarios.add("Felipe")
print (f"Adicionando usuários: {usuarios}")

#União de conjuntos
novos_usuarios = {"Marcos", "Anderson", "Amanda", "Nicolas", "Ana"}
todos_usuarios = usuarios.union(novos_usuarios)
print (f"União de conjuntos: {todos_usuarios}")

#Duplicadas no conjuntos
usuarios_comuns = usuarios.intersection(novos_usuarios)
print (f"Duplicadas no conjuntos: {usuarios_comuns}")

#Distintos nos conjuntos
usuarios_diferentes = usuarios.difference(novos_usuarios)
print (f"Distintos no conjuntos: {usuarios_diferentes}")