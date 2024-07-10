#Manipulando tuplas - tuple

cores = ("Vermelha", "Azul", "Amarelo", "Verde", "Azul", "Cinza")
print (f"Meu carro é {cores[2]}")
#print acima destaca em qual posição vai retirar a váriavel para resposta, neste caso é o Amarelo na posição 2

#Função len conta todos os dados dentro da tupla ou list
qtd = len(cores)
#print vai mostrar a quantidade total de cores dentro da tupla
print (f"Tenho {qtd} de opções de cores")


cor = input("Digite uma cor: ")
if cor in cores:
    qtd_cor = cores.count(cor)
    print (f"Temos {qtd_cor} tipo de {cor}")
else:
    print(f"A cor {cor} não existe na loja")