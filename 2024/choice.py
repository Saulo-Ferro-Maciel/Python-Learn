from random import shuffle

off = False
while not off:
    lista_de_Grupos, grupos = [],0

    try:
        grupos = int(input("Quantos grupos ou temas serão sorteados?\n"))
    except:
        print("\nPor favor, coloque apenas valores numericos\n")
        continue

    for i in range(grupos):
        nome = input(f'Adicione o nome do {i+1}º Grupo/Tema:\n')
        lista_de_Grupos.append(nome.upper())

    shuffle(lista_de_Grupos)

    print("\nOrdem aleatória dos grupos/temas:")
    for i, grupo in enumerate(lista_de_Grupos, 1):
        print(f"Item {i}: {grupo}")

    resposta = input("\nDeseja sortear novamente? (s/n)\n").lower()
    if resposta[0] != 's':
        off = True
