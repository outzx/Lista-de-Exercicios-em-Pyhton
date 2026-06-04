import datetime

# Define a função que estrutura e grava as mensagens de eventos do sistema
def registrar_log(mensagem, tipo="INFO", nome_arquivo="sistema.log"):

    # Captura a data e a hora atual exata do computador
    agora = datetime.datetime.now()
    # Formata o objeto de tempo para o padrão textual Ano-Mês-Dia Hora:Minuto:Segundo
    fmtempo = agora.strftime("%Y-%m-%d %H:%M:%S")

    # Monta a string da linha do log padronizando o tipo de aviso em letras maiúsculas
    entrada = f"[{fmtempo}] {tipo.upper()}: {mensagem}\n"

    # Espaço que abre ou cria o arquivo em modo append ('a') para adicionar texto ao final sem apagar o existente
    with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
        # Grava a linha de log estruturada dentro do arquivo de texto
        arquivo.write(entrada)

# Chamadas de teste simulando diferentes níveis de ocorrências no sistema
registrar_log("Sistema iniciado", "INFO")
registrar_log("Atenção", "WARNING")
registrar_log("Erro", "ERROR")

# Informa no terminal que a gravação dos dados foi finalizada
print("Logs salvos no arquivo 'sistema.log'.")
