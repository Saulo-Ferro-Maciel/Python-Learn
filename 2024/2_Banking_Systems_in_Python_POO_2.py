class User:
    def __init__(self, nome, senha):
        self._nome = nome
        self._senha = senha
        self._saldo = 0
        self._numero_saques = 0
        self._valores_sacados = []

    def get_nome(self):
        return self._nome

    def verificar_senha(self, senha):
        return self._senha == senha

    def get_saldo(self):
        return self._saldo

    def get_numero_saques(self):
        return self._numero_saques

    def get_valores_sacados(self):
        return self._valores_sacados

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            raise ValueError("O valor de depósito deve ser positivo.")

    def sacar(self, valor, limite, limite_saques):
        if valor <= 0:
            raise ValueError("O valor de saque deve ser positivo.")
        if valor > limite:
            raise ValueError("O teto máximo para saque é de 500 reais.")
        if self._numero_saques >= limite_saques:
            raise ValueError("Limite de saques diários excedido.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente para o saque.")
        
        self._saldo -= valor
        self._numero_saques += 1
        self._valores_sacados.append(valor)

    def extrato(self):
        return {
            "nome": self._nome,
            "saldo": self._saldo,
            "numero_saques": self._numero_saques,
            "valores_sacados": self._valores_sacados
        }


class Banco:
    LIMITE_SAQUE = 500
    LIMITE_SAQUES_DIARIOS = 3

    def __init__(self):
        self._usuarios = {}

    def adicionar_usuario(self, nome, senha):
        if nome not in self._usuarios:
            self._usuarios[nome] = User(nome, senha)

    def autenticar_usuario(self, nome, senha):
        if nome in self._usuarios and self._usuarios[nome].verificar_senha(senha):
            return self._usuarios[nome]
        else:
            raise ValueError("Nome de usuário ou senha incorretos.")

    def menu(self, usuario):
        while True:
            print('''\n
            Como podemos ajudar você?
            Selecione alguma das opções abaixo:
            
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [0] Sair
            ''')
            opcao = input("Digite o serviço desejado: ")
            if opcao == '1':
                self.depositar(usuario)
            elif opcao == '2':
                self.sacar(usuario)
            elif opcao == '3':
                self.extrato(usuario)
            elif opcao == '0':
                self.sair(usuario)
                break
            else:
                print("Opção inválida, tente novamente.")

    def depositar(self, usuario):
        try:
            valor = float(input(f"\n{usuario.get_nome()}, quantos reais você deseja depositar?\n").replace(",", "."))
            usuario.depositar(valor)
            print(f"Depósito realizado com sucesso. Saldo atual: {usuario.get_saldo()}\n")
        except ValueError as e:
            print(e)
        self.continuar(usuario)

    def sacar(self, usuario):
        try:
            valor = float(input(f"{usuario.get_nome()}, quantos reais você deseja sacar?\n").replace(",", "."))
            usuario.sacar(valor, self.LIMITE_SAQUE, self.LIMITE_SAQUES_DIARIOS)
            print(f"Saque realizado com sucesso. Saldo atual: {usuario.get_saldo()}\n")
        except ValueError as e:
            print(e)
        self.continuar(usuario)

    def extrato(self, usuario):
        dados_extrato = usuario.extrato()
        print(f"\nExtrato de {dados_extrato['nome']}")
        print(f"Saldo atual: {dados_extrato['saldo']}")
        print(f"Número de saques: {dados_extrato['numero_saques']}")
        print(f"Valores sacados: {dados_extrato['valores_sacados']}")
        self.sair(usuario)

    def continuar(self, usuario):
        while True:
            opcao = input("\nDeseja finalizar o atendimento? (s/n): ").strip().lower()
            if opcao == 's':
                self.sair(usuario)
                break
            elif opcao == 'n':
                self.menu(usuario)
                break
            else:
                print("Responda com 's' ou 'n'.")

    def sair(self, usuario):
        print(f"Obrigado por escolher nossos serviços, {usuario.get_nome()}. Até a próxima!")

    def login(self):
        nome = input("Digite seu nome completo: ")
        senha = input("Digite sua senha de 8 dígitos: ")

        try:
            usuario = self.autenticar_usuario(nome, senha)
            print(f"\nLogin bem-sucedido! Bem-vindo(a), {nome}.")
            self.menu(usuario)
        except ValueError as e:
            print(e)


def main():
    banco = Banco()

    banco.adicionar_usuario("Saulo Ferro Maciel", "12345678")
    banco.adicionar_usuario("Jamilly Cunha da Silva", "08052268")
    banco.adicionar_usuario("Marina Silva", "07681155")
    banco.adicionar_usuario("Pedro Machado", "48789818")

    while True:
        print('''\nBem-vindo ao BSF (Banco do Saulo Ferro)\n\nSelecione uma das opções para continuar:
        [1] Criar conta\t[2] Fazer login em conta
        ''')
        opcao = input("Digite o valor: ").strip()
        if opcao == '1':
            print("\nDesculpa, ainda estamos desenvolvendo esta funcionalidade.")
        elif opcao == '2':
            banco.login()
        else:
            print("Opção inválida, tente novamente.\n")


if __name__ == "__main__":
    main()
