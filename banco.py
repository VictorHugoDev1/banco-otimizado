# Menu principal
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar usuário
[b] Criar conta bancária
[q] Sair
=> """

# Dados iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []  
agencia = '0001'
numero_conta = 1

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
    global saldo, extrato, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

def exibir_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario():
    global usuarios
    nome = input("Nome do usuário: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("CPF (somente números): ")
    endereco = input("Endereço (logradouro . nro - bairro - cidade/sigla estado): ")

    # Verificar se CPF já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado. Cadastro falhou.")
            return

    # Adicionar usuário à lista
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário cadastrado com sucesso.")

def criar_conta_bancaria():
    global contas, numero_conta
    cpf = input("Informe o CPF do usuário para criar a conta: ")

    # Buscar usuário pelo CPF
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        # Criar e adicionar nova conta
        contas.append({
            'agencia': agencia,
            'numero_conta': numero_conta,
            'usuario': usuario_encontrado
        })
        print(f"Conta criada com sucesso. Número da conta: {numero_conta}")
        numero_conta += 1
    else:
        print("Usuário não encontrado. Cadastro de conta falhou.")

# Loop principal
while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "c":
        cadastrar_usuario()

    elif opcao == "b":
        criar_conta_bancaria()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
