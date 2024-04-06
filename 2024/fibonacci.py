exit = False

while not exit:
    quantidade = int(input("\nDigite a quantidade de números da Sequência de Fibonacci que deseja visualizar:\n"))
    sequencia = []
    contador = 0
    proximo = 1

    for _ in range(quantidade):
        sequencia.append(contador)
        contador, proximo = proximo, contador + proximo

    print(f"A sequência dos {quantidade} valores de Fibonacci solicitados é {sequencia}")
    
    opcao = input("\nDeseja sair? (s/n):\n")
    if opcao.lower() == 's':
        exit = True

