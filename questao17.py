# Define a classe que representa e gerencia uma conta bancária individual
class ContaBancaria: 
    # Método construtor executado ao criar uma nova conta (o saldo padrão inicial é zero)
    def __init__(self, numero_conta, titular, saldo_inicial=0): 
        self.numero_conta = numero_conta # Armazena o identificador textual ou numérico da conta
        self.titular = titular           # Guarda o nome do cliente dono desta conta específica
        self.saldo = saldo_inicial       # Define a quantia em dinheiro disponível de partida
  
    # Método responsável por adicionar fundos à conta
    def depositar(self, valor): 
        # Garante que o valor enviado para depósito seja maior que zero
        if valor > 0: 
            self.saldo += valor # Soma a quantia informada ao saldo existente na conta
            # Informa o sucesso do depósito e exibe o saldo atualizado com duas casas decimais
            print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}") 
        # Caso o valor seja zero ou negativo, bloqueia a operação
        else: 
            print("Valor de depósito inválido.") 
  
    # Método responsável por retirar fundos da conta
    def sacar(self, valor): 
        # Verifica se a quantia é positiva e se a conta possui dinheiro suficiente para cobrir
        if valor > 0 and self.saldo >= valor: 
            self.saldo -= valor # Subtrai a quantia solicitada do saldo disponível
            # Exibe os dados do saque concluído e o saldo remanescente na conta
            print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}") 
            return True # Retorna verdadeiro indicando que a transação foi aprovada
        # Caso o valor solicitado seja estritamente maior que o saldo em conta
        elif valor > self.saldo: 
            print("Saldo insuficiente.") # Alerta sobre a falta de fundos
            return False # Retorna falso interrompendo a transação
        # Captura cenários de valores inválidos (como saques de valores negativos ou zero)
        else: 
            print("Valor de saque inválido.") 
            return False # Retorna falso interrompendo a transação
  
    # Método simples para consulta rápida do saldo disponível
    def verificar_saldo(self): 
        # Exibe uma mensagem amigável contendo o número da conta e o saldo atual
        print(f"Saldo atual da conta {self.numero_conta}: R$ {self.saldo:.2f}") 
        return self.saldo # Devolve o valor numérico do saldo para quem chamou o método
  
# Define a classe que representa um correntista do banco
class Cliente: 
    # Método construtor executado ao registrar um novo cliente no sistema
    def __init__(self, nome, cpf): 
        self.nome = nome     # Armazena o nome completo do cliente
        self.cpf = cpf       # Guarda o número de documento CPF do cliente
        self.contas = []     # Inicializa uma lista vazia para associar objetos da classe ContaBancaria 
  
    # Método para vincular uma nova conta criada ao perfil deste cliente
    def adicionar_conta(self, conta): 
        self.contas.append(conta) # Insere a conta recebida no final da lista de contas do cliente
        # Confirma na tela que a conta agora pertence a este titular
        print(f"Conta {conta.numero_conta} adicionada ao cliente {self.nome}.") 
  
    # Método para exibir no terminal todas as contas ativas vinculadas a este cliente
    def listar_contas(self): 
        # Avalia se a lista de contas não está vazia
        if self.contas: 
            print(f"\nContas de {self.nome}:") # Imprime o cabeçalho com o nome do cliente
            # Percorre cada objeto de conta guardado dentro da lista
            for conta in self.contas: 
                # Mostra o número identificador e o saldo de cada conta listada
                print(f"  Número: {conta.numero_conta}, Saldo: R$ {conta.saldo:.2f}") 
        # Executado caso o cliente não possua nenhuma conta aberta no sistema
        else: 
            print(f"O cliente {self.nome} não possui contas.") 
  
# Define a classe principal que gerencia o ecossistema de clientes e contas
class Banco: 
    # Método construtor para criar uma nova instituição bancária
    def __init__(self, nome): 
        self.nome = nome       # Armazena o nome fantasia ou razão social do banco
        self.clientes = []     # Inicializa uma lista vazia para armazenar os objetos da classe Cliente 
  
    # Método para registrar um cliente na base de dados geral do banco
    def adicionar_cliente(self, cliente): 
        self.clientes.append(cliente) # Adiciona o objeto cliente no final da lista do banco
        # Informa na tela que o cliente foi cadastrado na instituição
        print(f"Cliente {cliente.nome} adicionado ao banco {self.nome}.") 
  
    # Método de busca que localiza um cliente cadastrado através do seu CPF
    def buscar_cliente_por_cpf(self, cpf): 
        # Vasculha a lista de clientes cadastrados no banco linha por linha
        for cliente in self.clientes: 
            # Se encontrar um CPF que case perfeitamente com a busca
            if cliente.cpf == cpf: 
                return cliente # Devolve o objeto completo do cliente localizado
        return None # Caso encerre a busca e não ache ninguém, devolve um valor nulo
  
    # Método de busca profunda que varre os clientes para achar uma conta pelo número
    def buscar_conta_por_numero(self, numero_conta): 
        # Inicia um laço para navegar por cada cliente do banco
        for cliente in self.clientes: 
            # Inicia um segundo laço interno para olhar as contas daquele cliente específico
            for conta in cliente.contas: 
                # Compara se o número da conta atual é o mesmo que está sendo procurado
                if conta.numero_conta == numero_conta: 
                    return conta # Devolve o objeto completo da conta localizada
        return None # Caso varra todo o banco e não encontre o número, retorna nulo
  
# ----------------------------------------------------------------------------------
# Exemplo de uso prático do sistema bancário construído acima 
# ----------------------------------------------------------------------------------

# Cria uma instância da instituição bancária informando o seu nome
banco_digital = Banco("Meu Banco Digital") 
  
# Instancia a primeira cliente passando seu nome e documento
cliente1 = Cliente("Marcos Aurélio", "123.456.789-00") 
# Cria duas contas separadas que serão de propriedade da Maria (com saldos de 1000 e 500)
conta1_m = ContaBancaria("001-X", "Marcos Aurélio", 1000) 
conta2_m = ContaBancaria("002-Y", "Marcos Aurélio", 500) 
# Vincula formalmente as duas contas ao perfil do objeto cliente da Maria
cliente1.adicionar_conta(conta1_m) 
cliente1.adicionar_conta(conta2_m) 
# Cadastra o Marcos Aurélio (e consequentemente suas contas) na lista geral do banco digital
banco_digital.adicionar_cliente(cliente1) 
  
# Instancia o segundo cliente passando seu nome e documento
cliente2 = Cliente("Cristiano Ronaldo", "987.654.321-00") 
# Cria uma conta única para o Cristiano com saldo inicial de 2000
conta1_cristiano = ContaBancaria("003-Z", "Cristiano Ronaldo", 2000) 
# Vincula formalmente esta conta ao perfil do objeto cliente do Cristiano
cliente2.adicionar_conta(conta1_cristiano) 
# Cadastra o Cristiano na lista geral de clientes do banco digital
banco_digital.adicionar_cliente(cliente2) 
  
# --- Seção de Testes de Operações --- 

# Imprime o extrato de todas as contas que estão associadas ao Marcos Aurélio
cliente1.listar_contas() 
# Realiza um depósito de 200 reais na primeira conta do Marcos Aurélio (Saldo vai para 1200)
conta1_m.depositar(200) 
# Realiza um saque de 300 reais na primeira conta do Marcos Aurélio (Saldo cai para 900)
conta1_m.sacar(300) 
# Imprime o saldo final consolidado da primeira conta do Marcos Aurélio no terminal
conta1_m.verificar_saldo() 
  
# Executa a busca no sistema do banco utilizando o CPF cadastrado do Marcos Aurélio
cliente_encontrado = banco_digital.buscar_cliente_por_cpf("123.456.789-00") 
# Verifica se a função de busca retornou um cliente válido (não nulo)
if cliente_encontrado: 
    # Exibe no terminal o nome do cliente que foi localizado pelo CPF
    print(f"\nCliente encontrado: {cliente_encontrado.nome}") 
  
# Executa a busca no sistema procurando pela numeração da conta do Cristiano
conta_encontrada = banco_digital.buscar_conta_por_numero("003-Z") 
# Verifica se a função de busca profunda localizou a conta informada
if conta_encontrada: 
    # Exibe na tela os dados da conta localizada bem como o nome do seu titular
    print(f"Conta encontrada: {conta_encontrada.numero_conta} do titular {conta_encontrada.titular}")
