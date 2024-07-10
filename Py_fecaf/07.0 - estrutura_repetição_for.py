#Estrutura de Repetição - FOR
    #Execução de uma tabuada sem a estrutura de repetição FOR   
numero = int(input("Digite um número: "))

print(f"Tabuada do {numero}")

resultado = 1 * numero
print(f"{numero} x 1 = {resultado}")

resultado = 2 * numero
print(f"{numero} x 2 = {resultado}")

resultado = 35 * numero
print(f"{numero} x 3 = {resultado}")

    #Execução de uma tabuada com a estrutura de repetição FOR
numero = int(input("Digite um número: "))
for i in range (1, 70):
    resultado = numero * i
    print (f"{numero} X {i} = {resultado}")
