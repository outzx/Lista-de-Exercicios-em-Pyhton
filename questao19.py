import requests
from bs4 import BeautifulSoup

# Define o alvo (BBC Brasil) e configura um User-Agent para o site não bloquear a requisição
url_alvo = "https://www.bbc.com/portuguese"
headers_navegador = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    # Dispara a requisição HTTP para puxar o HTML da página
    resposta = requests.get(url_alvo, headers=headers_navegador)
    resposta.raise_for_status()  # Força um erro caso o status HTTP não seja 200 (Sucesso)
    
    # Passa o HTML bruto recebido para o parser do BeautifulSoup
    sopa_html = BeautifulSoup(resposta.text, "html.parser")
    
    # Na BBC Brasil, as manchetes principais e secundárias usam a tag h2 ou h3
    # Buscamos todas essas tags para garantir que vamos pegar a maioria dos títulos da capa
    tags_titulos = sopa_html.find_all(['h2', 'h3'])
    
    # Filtra e limpa o texto das tags encontradas, removendo espaços em branco extras
    titulos_limpos = []
    for tag in tags_titulos:
        texto = tag.get_text().strip()
        # Evita adicionar textos vazios ou duplicados na lista final
        if texto and texto not in titulos_limpos:
            titulos_limpos.append(texto)
            
    # Salva o resultado final criando um arquivo txt limpo
    with open("titulos_noticias.txt", "w", encoding="utf-8") as arquivo_texto:
        for idx, titulo in enumerate(titulos_limpos, start=1):
            arquivo_texto.write(f"{idx}. {titulo}\n")
            
    print(f"Sucesso! {len(titulos_limpos)} títulos foram salvos em 'titulos_noticias.txt'.")

except requests.exceptions.RequestException as erro_rede:
    print(f"Falha ao conectar com o site: {erro_rede}")
except Exception as erro_geral:
    print(f"Ocorreu um erro inesperado: {erro_geral}")
