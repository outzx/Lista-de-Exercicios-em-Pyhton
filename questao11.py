# Define a função responsável pela leitura e impressão do arquivo
def ler_arquivo(nome_arquivo):
    
    # Espaço de tratamento para evitar que o script quebre se o arquivo falhar ao abrir
    try:
        # Abre o arquivo em modo leitura ('r') garantindo o padrão de codificação UTF-8
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # Transforma todo o texto do arquivo em uma única variável de texto
            conteudo = arquivo.read()
            print(">>>>>>>>>Conteudo do Arquivo<<<<<<<<<")
            # Exibe o conteúdo completo extraído na tela
            print(conteudo)
            print(">>>>>>>>>Fim do Arquivo<<<<<<<<<")

    # Tratamento específico para o erro de arquivo ausente ou caminho incorreto
    except FileNotFoundError:
        print(f"O arquivo: {nome_arquivo} não foi encontrado ou não existe.")
    # Tratamento geral para capturar qualquer outra falha inesperada do sistema
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Captura o nome ou o caminho do arquivo digitado pelo usuário no terminal
nome_do_arquivo = input("Digite o nome do arquivo que deseja ler: ")
# Executa a função passando a string recebida como parâmetro
ler_arquivo(nome_do_arquivo)
