#cria duas variavéis e solicita os números ao usuário
numero = float(input("Insira um número:"))
num2= float(input("Insira outro número:"))

#faz as contas
soma = num2 + numero
sub = numero - num2
mult = numero * num2

#Evita erros na divisão
if num2 != 0:
    div = numero/num2
else:
    div = "Erro, não é possível dividir por zero"

#Apresenta os resultados
print(f"A soma é igual a: {soma}")
print(f"A subtração é igual a: {sub}")
print(f"A multiplicação é igual a: {mult}")
print(f"A divisão é igual a: {div}")
