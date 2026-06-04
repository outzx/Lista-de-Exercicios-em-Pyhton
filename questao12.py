import random

# Recebe o tamanho que o usuário deseja para a senha final
limite = int(input("Digite o limite de caracteres para a senha: "))

# Definição dos grupos de caracteres válidos para a composição da senha
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
especial = "!@#$%&*_+-=" 

# Junta todas as strings em uma única base de dados de caracteres disponíveis
caracteres = letras + numeros + especial

# Espaço que monta a estrutura da senha escolhendo caracteres aleatórios um por um
senha = [random.choice(caracteres) for _ in range(limite)]

# Junta os elementos da lista gerada para transformar em uma única string de texto
lista = "".join(senha)

# Exibe a senha finalizada na tela do usuário
print(f"A senha gerada é: {lista}")
