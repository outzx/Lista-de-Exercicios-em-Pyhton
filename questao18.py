import pandas as pd 
import matplotlib.pyplot as plt

# Puxa a base de dados direto do CSV
df_vis = pd.read_csv('dados_clientes.csv') 
  
# --- GRÁFICO 1: CLIENTES POR CIDADE ---
plt.figure(figsize=(10, 6)) 

# Conta os registros por cidade e plota em barras (azul claro)
df_vis['Cidade'].value_counts().plot(kind='bar', color='skyblue') 

# Ajustes de legenda e títulos do gráfico de barras
plt.title('Número de Clientes por Cidade') 
plt.xlabel('Cidade') 
plt.ylabel('Número de Clientes') 
plt.xticks(rotation=45)                  # Rotaciona o texto do eixo X para não encavalar
plt.grid(axis='y', linestyle='--')       # Linhas de grade apenas na horizontal
plt.tight_layout()                       # Evita que o corte de textos nas bordas

# Exporta e renderiza a imagem das cidades
plt.savefig('clientes_por_cidade.png') 
plt.show() 
  
# --- GRÁFICO 2: DISTRIBUIÇÃO DE IDADES ---
plt.figure(figsize=(10, 6)) 

# Monta o histograma dividindo as idades em 5 faixas (bins)
plt.hist(df_vis['Idade'], bins=5, color='lightcoral', edgecolor='black') 

# Ajustes visuais do histograma
plt.title('Distribuição de Idades dos Clientes') 
plt.xlabel('Idade') 
plt.ylabel('Frequência') 
plt.grid(axis='y', linestyle='--') 
plt.tight_layout() 

# Exporta e renderiza a imagem das idades
plt.savefig('distribuicao_idades.png') 
plt.show() 
  
print("Gráficos 'clientes_por_cidade.png' e 'distribuicao_idades.png' gerados com sucesso.")
