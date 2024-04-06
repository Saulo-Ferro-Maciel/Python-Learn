from time import sleep as slp
# Timer for Isometric Push-up
off = True
while off != False:
    cont, name = 0, str(input("What should I call you?\n")).upper()
    if name.strip() == "":
            name = "gym member".upper()

    try:
        record_time =  int(input(f"What is your record time in seconds, {name}?\n"))
        training_time = int(input(f"What is your training time in seconds, {name}?\n"))
    except:
        print("Your record time and training time must be integers!\n")
        continue

    print(f"\nLet's go, {name}!!!\n")

    for _ in range(0, training_time):
        slp(3)
        cont += 1

        print(f"{cont} seconds have passed.\nHang in there, {name}!\n")
        if cont == record_time+1:
            print(f"You've beaten your record, {name}!!")
        if cont >= training_time:
            print(f"\nCongratulations, {name}!\n")

    exit = str(input("You need to leave?\n")).strip().lower()
    if exit in "s":
            off = False