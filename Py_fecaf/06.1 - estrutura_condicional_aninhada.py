  #ESTRUTURA CONDICIONAL COMPLEXAS
        #ESTRUTURA ANINHADA
anos_experiencia = int(input('Dgite os anos de experiência:'))

if anos_experiencia == 0:
        nivel = "estagiário"
elif anos_experiencia <= 3:
        nivel = "Júnior"
elif anos_experiencia <= 8:
        nivel = "Pleno"
else:
        nivel = "Sênior"

print (f'Você é um desenvolvedor do nível {nivel}')