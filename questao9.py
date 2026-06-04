# Recebe a entrada do usuário e converte o texto para inteiro
num = int(input("Insira um número inteiro positivo: "))

# Validação matemática onde o fatorial de zero sempre é um
if num == 0:
    print("O fatorial de 0 é 1.")
# Alternativa para cálculo de números acima de zero
else:
    # Inicializa a variável acumuladora com o elemento neutro da multiplicação
    fatorial = 1
    # Laço que percorre de 1 até o número digitado
    for i in range(1, num + 1):
        # Multiplica o valor acumulado pelo número atual da iteração
        fatorial *= i
    # Exibe o resultado final calculado pelo laço
    print(f"O fatorial de {num} é {fatorial}.")
