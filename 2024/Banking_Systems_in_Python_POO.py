# User List
users = { 
    "Saulo Ferro Maciel": {"senha": "12345678"},
    "Jamilly Cunha da Silva": {"senha": "08052268"},
    "Marina Silva": {"senha": "07681155"},
    "Pedro Machado":{"senha": "48789818"},
}

dinheiro_dos_usuarios = {
    "Saulo Ferro Maciel": {"saldo":500,"numero_Saques":3,"valores_Sacados":[20,30,50]},
    "Jamilly Cunha da Silva": {"saldo":50,"numero_Saques":1, "valores_Sacados":[50]},
    "Marina Silva": {"saldo":5,"numero_Saques":0, "valores_Sacados":[]},
    "Pedro Machado": {"saldo": 1.5,"numero_Saques":1, "valores_Sacados":[20]},
}

# Bank System Menu
menu = '''
Como podemos ajudar você? 
Selecione alguma das opções abaixo:

[1] Depositar;
[2] Sacar;
[3] Extrato,
[0] Sair.
'''

# Bank System Config
LIMITE = 500
LIMITE_SAQUES = 3

def continuar(userName):
    while True:
        try:
            input_Continue = input("Deseja FINALIZAR o atendimento?\nResponda com SIM ou NÃO:\n")
            input_Continue = input_Continue[0].lower()

            if input_Continue == 's':
                sair(userName)
                break
            elif input_Continue == 'n':
                menu_Function(userName)
                break
            elif input_Continue not in ["s", "n"]:
                raise ValueError("Responda com SIM ou NÃO")
        except ValueError:
            print('''
            Responda com SIM ou NÃO
            ''')

def sair(userName):
    print(f'''
    Obrigado por escolher os nossos serviços, {userName}.
    O BSF agradeçe a preferência!

    👋 Até a próxima 👋
    ''')

def extrato(userName):
    print('''\n
    Extratos no Banco do Saulo Ferro (BSF)
    ''')
    print(f"\nNome do usuário: {userName}\nSaldo atual: {dinheiro_dos_usuarios[userName]['saldo']}\nQuantidade se saques:{numero_Saques}\nLista de saques feitos:")
    if len(dinheiro_dos_usuarios[userName]["valores_Sacados"]) == 0:
        print("Nenhum saque foi feito hoje!")
    else: 
        for saque in dinheiro_dos_usuarios[userName]["valores_Sacados"]:
                print(f'{dinheiro_dos_usuarios[userName]["valores_Sacados"].index(saque) + 1}º == {saque}')
    sair(userName)
    
def sacar(userName):
    while True:
        try:
            input_saque = input(f"\n\n{userName}, quantos reais você deseja sacar?\n")
            input_saque = input_saque.replace(",", ".")
            input_saque = float(input_saque)
            numero_Saques = dinheiro_dos_usuarios[userName]["numero_Saques"]

            if input_saque <= 0.0:
                raise ValueError("\nPor favor, insira um valor positivo maior que zero.\n")
            elif input_saque > LIMITE:
                raise ValueError("\nO teto máximo para saque é e 500 reais\n")
            elif numero_Saques >= LIMITE_SAQUES:
                raise ValueError("\nParece que você já efetuou o limite de saques diários,\npor favor espere 24 horas ou entre em contato com a gerencia!\n")
            elif input_saque > dinheiro_dos_usuarios[userName]["saldo"]:
                raise ValueError("\nVocê não tem saldo suficiente para sacar este valor.\n")
            elif dinheiro_dos_usuarios[userName]["saldo"] - input_saque < 0:
                raise ValueError("\nVocê não pode sacar um valor maior que seu saldo disponível.\n")
            else:           
                dinheiro_dos_usuarios[userName]["saldo"] -= input_saque
                dinheiro_dos_usuarios[userName]["numero_Saques"] += 1
                dinheiro_dos_usuarios[userName]["valores_Sacados"].append(input_saque)
                print(f'''Você acaba de efetuar um saque de {input_saque} reais\nSeu saldo atual é: {dinheiro_dos_usuarios[userName]["saldo"]}\n''')
                continuar(userName)
            break
        except ValueError as e:
            print(e)
            continuar(userName)

def depositar(userName):
    while True:
        try:
            input_deposito = input(f"\n\n{userName}, quantos reais você deseja depositar?\n")
            input_deposito = input_deposito.replace(",", ".")
            
            input_deposito = float(input_deposito)
            if input_deposito <= 0.0:
                raise ValueError("\nPor favor, insira um valor positivo maior que zero.\n")
            
            dinheiro_dos_usuarios[f"{userName}"]["saldo"] += input_deposito
            print(f'''Seu saldo atual é: {dinheiro_dos_usuarios[f"{userName}"]["saldo"]}\n''')
            break

        except ValueError:
            print('''
            Não entendemos!\nPor favor, coloque o valor em números que deseja depositar!
            ''')
    
    continuar(userName)

def menu_Function(userName):
    print(menu)
    while True:
        try:
            input_menu = input("\nDigite o serviço desejado de acordo com os códigos numéricos:\n")
            input_menu = str(input_menu)
            if not input_menu.isdigit():
                raise ValueError("\nOs códigos de serviços devem ser números, por favor, selecione um código válido!\n")
            else:
                if len(input_menu) != 1:
                    raise ValueError("\nOs códigos de serviços só possuem um algarismo, por favor, selecione um código válido!\n")
                else:
                    if "1" in input_menu:
                        depositar(userName)
                    elif "2" in input_menu:
                        sacar(userName)
                    elif "3" in input_menu:
                        extrato(userName)
                    elif input_menu not in ["1", "2", "3", "0"]:
                        raise ValueError('''\n\nCódigo inválido, acesse usando os códigos válidos!\n
                        [1] Depositar;
                        [2] Sacar;
                        [3] Extrato,
                        [0] Sair.''')
                    elif "0" in input_menu:
                        sair(userName)
            break
        except ValueError:
            print('''\n
            Use os códigos a seguir para acessar os serviços da instituição:

            [1] Depositar;
            [2] Sacar;
            [3] Extrato,
            [0] Sair.
            ''')

def login_In_Bank(users):
    input_user = input("Olá,\n\nDigite seu nome completo:\n")
        
    if input_user in users:
        while True:
            try:
                input_senha = input("\nDigite sua senha de 8 dígitos:\n")
                if len(input_senha) != 8:
                    raise ValueError("\nA senha deve ter exatamente 8 dígitos.")
                int(input_senha) 
                break
            except ValueError:
                print("Por favor, digite uma senha válida de 8 dígitos.")

        stored_senha = users[input_user]["senha"]
        if stored_senha == input_senha:
            print(f"\nLogin bem-sucedido!\nBem-vindo(a), {input_user}.")
            menu_Function(input_user)
        else:
            print("\nSenha incorreta. Tente novamente.")
    else:
        print("\nUsuário não encontrado.\nFaça o login novamente")


login_In_Bank(users)
