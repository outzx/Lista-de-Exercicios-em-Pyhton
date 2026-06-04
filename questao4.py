#Recebe o número
numero = int(input("Insira um número para ver a tabuada: "))

#Tabuada do número
print(">>>>>>>>>>>>>Tabuada<<<<<<<<<<<<<") 
print(f"\nTabuada do {numero}:")

#"for in" para começar com 1 e parar antes de 11
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
