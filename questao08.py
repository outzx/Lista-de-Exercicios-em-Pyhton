lista_contatos = []

# Loop infinito para manter o menu rodando até o usuário decidir sair
while True:
    print(">>>>>>>>>>>>Lista de Contatos<<<<<<<<<<<<")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Exibir contatos")
    print("4 - Buscar contato")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    # Fluxo para cadastrar um novo contato
    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        tele = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        # Monta o dicionário com as informações coletadas
        contato = {"nome": nome, "telefone": tele, "email": email}
        # Insere o dicionário no final da lista global
        lista_contatos.append(contato)
        print(f"Contato '{nome}' adicionado com sucesso.")
        
    # Fluxo para deletar um contato pelo nome
    elif opcao == "2":
        nome = input("Insira o nome do contato que deseja remover: ")
        contato_encontrado = False
        # Varre a lista procurando o nome correspondente
        for contato in lista_contatos:
            if contato["nome"] == nome:
                # Remove o elemento encontrado da lista
                lista_contatos.remove(contato)
                print(f"Contato '{nome}' removed.")
                contato_encontrado = True
                break # Para o laço assim que remove o primeiro encontrado
        # Validação caso o loop termine e a flag continue falsa
        if not contato_encontrado:
            print(f"Contato '{nome}' não encontrado.")
            
    # Fluxo para listar todos os contatos salvos
    elif opcao == "3":
        # Verifica se a lista não está vazia
        if lista_contatos:
            print("Lista de contatos: ")
            # Percorre a lista e exibe os dados formatados de cada dicionário
            for contato in lista_contatos:
                print(f"Nome: {contato['nome']} \n Telefone: {contato['telefone']} \n Email: {contato['email']}\n")
        else:
            print("A lista de contatos está vazia.")

    # Fluxo para pesquisar um contato específico por nome
    elif opcao == "4":
        nome = input("Digite o nome do contato que deseja buscar: ")
        contato_encontrado = False
        # Percorre a lista testando a chave 'nome'
        for contato in lista_contatos:
            if contato["nome"] == nome:
                print(f"Contato encontrado: \n Nome: {contato['nome']} \n Telefone: {contato['telefone']} \n Email: {contato['email']}\n")
                contato_encontrado = True
                break # Encerra a busca ao encontrar a correspondência
        # Validação para quando o nome digitado não existe no sistema
        if not contato_encontrado:
            print(f"Contato '{nome}' não existe na lista.")
            
    # Opção de saída do sistema
    elif opcao == "5":
        print("Encerrando programa. Obrigado!")
        break # Quebra o loop while e finaliza o script
