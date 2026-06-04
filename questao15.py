# Importa o módulo nativo do Python para manipulação de arquivos CSV
import csv

# Inicializa a variável numérica que vai acumular o valor total de todas as vendas
total_faturamento = 0.0

# Cria um dicionário vazio para rastrear a quantidade acumulada de itens vendidos por produto
quantidades_por_produto = {}

# Abre o arquivo 'vendas.csv' em modo de leitura ('r') garantindo a codificação UTF-8 contra erros de acentuação
with open('vendas.csv', mode='r', encoding='utf-8') as arquivo_csv:
    
    # Cria um leitor que transforma cada linha do arquivo em um dicionário baseado no cabeçalho
    leitor_dados = csv.DictReader(arquivo_csv)
    
    # Inicia um laço de repetição para processar uma linha (registro de venda) por vez
    for linha in leitor_dados:
        
        # Extrai o nome do produto da coluna correspondente na linha atual
        produto = linha['produto']
        
        # Converte o texto da coluna de quantidade para um número inteiro
        quantidade = int(linha['quantidade'])
        
        # Converte o texto da coluna de preço para um número decimal (float)
        preco = float(linha['preço'])
        
        # Calcula o subtotal da linha (quantidade * preço) e soma ao faturamento total acumulado
        total_faturamento += quantidade * preco
        
        # Recupera a quantidade já existente do produto no dicionário (ou zero se for novo) e soma a nova quantidade
        quantidades_por_produto[produto] = quantidades_por_produto.get(produto, 0) + quantidade

# Identifica a chave (nome do produto) dentro do dicionário que possui o maior valor de unidades vendidas
produto_mais_vendido = max(quantidades_por_produto, key=quantidades_por_produto.get)

# Exibe na tela o valor total faturado formatado com duas casas decimais após a vírgula
print(f"Faturamento Total das Vendas: R$ {total_faturamento:.2f}")

# Exibe na tela o nome do produto vencedor juntamente com a sua respectiva quantidade total de unidades saídas
print(f"Produto Mais Vendido: {produto_mais_vendido} ({quantidades_por_produto[produto_mais_vendido]} unidades)")


# Precisa de um arquivo 'vendas.csv' com as seguintes colunas: 'produto', 'quantidade', 'preço' para que o código funcione corretamente. O arquivo deve estar no mesmo diretório do script ou o caminho deve ser especificado corretamente.