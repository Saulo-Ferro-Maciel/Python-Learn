import time as tm

def count_seconds():
    count = int(input("Quantos minutos devo contar?\nResposta: "))
    start = input(f"Devo começar a contagem de {count} minuto(s)? [s/n] ").strip().lower()
    
    if start[0] == 's':
        print("Iniciando a contagem...\n")
        total_seconds = count * 60
        for i in range(1, total_seconds + 1):
            tm.sleep(1)
            print(f"Já se passaram {i} segundo(s).")
        print(f"\nJá passou {count} minuto(s).")
    else:
        print(f"Contagem de {count} minuto(s) cancelada.")

if __name__ == "__main__":
    count_seconds()
