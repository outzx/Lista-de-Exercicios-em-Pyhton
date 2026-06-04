lista_compras = []
#while true para repetição
while True:
#Apresentar as opções da Lista de compras
    print(">>>>>>>>Lista de compras<<<<<<<<")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista")
    print("4. Sair")
#Solicitar a escolha do usuário
    opçao = input("Escolha uma opção: ")

#Executar ação referente a escolha
    if opçao == "1":
        item = input("Digite o nome do item adicionado: ")
        lista_compras.append(item)
        print(f"Item '{item}' adicionado à lista de compras.")
    elif opçao == "2":
        item = input("Digite o nome do item a ser removido: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"Item '{item}' removido da lista de compras.")
        else:
            print(f"Item '{item}' não encontrado na lista de compras.")
    elif opçao == "3":
        if lista_compras:
          print("Lista de compras:")
          for item in lista_compras:
            print(f"- {item}")
        else:         
            print("A lista de compras está vazia.")
    elif opçao == "4":
        print("Saindo do programa. Até mais!")
        break
