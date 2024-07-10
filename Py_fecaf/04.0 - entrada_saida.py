 #ENTRADA E SAÍDA DE DADOS
nome="Nicolas"
Tamanho= 167

#No caso abaixo o PRINT tem uma situação específica que a vírgula faz a separação entre váriavel e texto
print("olá meu nome é", nome,"e meu tamanho é", Tamanho)

#Abaixo se coloca a variável entre chaves e ápos o igual se coloca "f" para demonstrar que essa linha é diferenciada "F-STRING", aceita diversas variáveis
mensagem= f"olá meu nome é {nome}e meu tamanho é {Tamanho}"

print(mensagem)

#ENTRADA DOS DADOS COM INPUT
nomempessoa= input("digite seu nome: ")
filho= input("digite nome do filho: ")

mensagem_input= f"olá meu nome é {nomempessoa} e o nome do meu filho é {filho}"

print(mensagem_input)
 