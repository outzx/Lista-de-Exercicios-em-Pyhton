# Define a função que processa e valida a regra matemática do CPF
def validar_cpf(cpf):
    # Remove a formatação de pontos e traços deixando apenas a string numérica
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Valida se a string tem o tamanho exato de 11 caracteres e se contém apenas números
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    # Espaço que valida matematicamente o primeiro e o segundo dígito verificador
    for i in range(9, 11):
        # Multiplica os dígitos anteriores por pesos decrescentes e soma os resultados
        soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))

        # Calcula o resto da divisão por 11 seguindo a regra da Receita Federal
        digito_verificador = (soma * 10) % 11

        # Caso o resto seja 10, o dígito esperado por padrão vira zero
        if digito_verificador == 10:
            digito_verificador = 0

        # Compara o dígito calculado com o dígito real presente na string
        if digito_verificador != int(cpf[i]):
            return False # Retorna falso imediatamente se houver divergência
            
    return True # Retorna verdadeiro se passar em todas as checagens do laço
            
# Captura o CPF digitado pelo usuário no terminal
cpf_input = input("Digite um CPF (formato: XXX.XXX.XXX-XX): ")
# Espaço condicional que chama a função de validação e exibe o resultado final
if validar_cpf(cpf_input):
    print("CPF válido.")
else:
    print("CPF inválido.")
