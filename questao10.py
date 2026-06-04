# Inicializa a lista (pode ser usada futuramente para salvar o histórico de conversões)
convertor_temp = []

# Loop infinito para manter o menu ativo até o usuário encerrar
while True:
    print(">>>>>>>>>>>>Convertor de Temperatura<<<<<<<<<<<<")
    print("1 - Converter Celsius para Fahrenheit")
    print("2 - Converter Fahrenheit para Celsius")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")
    
    # Espaço para conversão de Celsius para Fahrenheit
    if opcao == "1":
        # Recebe o valor em float(ponto flutuante)
        celsius = float(input("Digite a temperatura em Celsius: "))
        # Aplica a fórmula matemática de conversão para Fahrenheit
        fah = (celsius * 9/5) + 32
        # Exibe o resultado limitando o Fahrenheit em duas casas decimais
        print(f"{celsius} graus Celsius equivalem a {fah:.2f} graus Fahrenheit.")
        
    # Espaço para conversão de Fahrenheit para Celsius
    elif opcao == "2":
        # Recebe o valor em float
        fah = float(input("Digite a temperatura em Fahrenheit: "))
        # Aplica a fórmula matemática correta para Celsius
        celsius = (fah - 32) * 5/9
        # Exibe o resultado limitando o Celsius em duas casas decimais
        print(f"{fah} graus Fahrenheit equivalem a {celsius:.2f} graus Celsius.")
        
    # Opção de saída do sistema
    elif opcao == "3":
        print("Encerrando programa. Obrigado!")
        break # Quebra o loop while e finaliza o script
