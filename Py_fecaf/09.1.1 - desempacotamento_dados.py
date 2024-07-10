#Desempacotamento dos dados

aluno = ("Leonid", 10, 5)

#Poderia ser feito assim:
nome = aluno[0]
nota_1 = aluno[1]
nota_2 = aluno [2]
media = (nota_1 + nota_2) / 2

print (f"{nome} tem nota {nota_1} e a nota {nota_2} com a média {media}")

#Desempacotamento
estudante = ("Nicolas", 7, 10)
aluno, nota_3, nota_4 = estudante
media_2 = (nota_3 + nota_4) / 2

print (f"{aluno} tem nota {nota_3} e a nota {nota_4} com a média {media_2}")