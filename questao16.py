# Carrega a biblioteca Pandas sob o apelido 'pd' para tratar tabelas e arquivos de dados
import pandas as pd

# Inicia um bloco de proteção para capturar falhas de leitura ou dados ausentes
try: 
    # Abre e lê o arquivo CSV, transformando as linhas e colunas em uma tabela (DataFrame)
    df = pd.read_csv('dados_clientes.csv') 
  
    # Exibe uma linha divisória estética no terminal antes de mostrar os resultados
    print("\n--- Análise de Dados de Clientes ---") 
    # Imprime um aviso indicando que a tabela inteira será exibida a seguir
    print("DataFrame Original:") 
    # Imprime na tela o conteúdo bruto carregado do arquivo CSV
    print(df) 
  
    # Acessa a coluna 'Idade' da tabela e calcula o valor médio aritmético dos registros
    media_idade = df['Idade'].mean() 
    # Acessa a coluna 'Renda' da tabela e calcula o valor médio aritmético dos faturamentos
    media_renda = df['Renda'].mean() 
    # Mostra a média de idade calculada, limitando a exibição em duas casas decimais
    print(f"\nMédia de Idade: {media_idade:.2f} anos") 
    # Mostra a média de renda calculada com formatação de moeda em duas casas decimais
    print(f"Média de Renda: R$ {media_renda:.2f}") 
  
    # Conta a frequência de cada município na coluna 'Cidade' e descobre o nome do mais repetido
    cidade_mais_clientes = df['Cidade'].value_counts().idxmax() 
    # Imprime no terminal o nome da cidade geográfica que concentra a maior base de usuários
    print(f"\nCidade com o maior número de clientes: {cidade_mais_clientes}") 
  
    # Solicita um valor de corte financeiro ao usuário no teclado e converte o texto para decimal
    renda_minima = float(input("\nDigite a renda mínima para filtrar clientes: R$ ")) 
    # Varre a tabela original e extrai apenas as linhas onde o salário supera o valor digitado
    clientes_alta_renda = df[df['Renda'] > renda_minima] 
    # Imprime um cabeçalho personalizado indicando o início da lista de pessoas filtradas
    print(f"\nClientes com renda acima de R$ {renda_minima:.2f}:") 
    # Exibe a nova tabela filtrada contendo apenas os perfis que atendem ao critério de renda
    print(clientes_alta_renda) 
  
# Captura o erro caso o arquivo especificado esteja na pasta errada ou não exista no computador
except FileNotFoundError: 
    # Avisa o usuário que o programa não pôde avançar devido à falta do arquivo físico
    print("Erro: O arquivo 'dados_clientes.csv' não foi encontrado.") 
# Captura o erro caso o script busque por 'Idade', 'Renda' ou 'Cidade' e o CSV use outros nomes
except KeyError as e: 
    # Mostra exatamente qual foi o nome da coluna que provocou a quebra do programa
    print(f"Erro: Coluna '{e}' não encontrada no arquivo CSV. Verifique o cabeçalho.") 
# Funciona como uma rede de segurança para qualquer outra falha não mapeada (ex: digitação de letras no input)
except Exception as e: 
    # Exibe a mensagem técnica gerada pelo próprio interpretador Python sobre o ocorrido
    print(f"Ocorreu um erro inesperado: {e}")

# Precisa de um arquivo 'dados_clientes.csv' com as seguintes colunas: 'Idade', 'Renda', 'Cidade' para que o código funcione corretamente. O arquivo deve estar no mesmo diretório do script ou o caminho deve ser especificado corretamente.