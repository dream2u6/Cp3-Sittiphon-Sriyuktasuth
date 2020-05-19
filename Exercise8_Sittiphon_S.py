usernameInput = input("Username : ")
passwordInput = input("password : ")
if usernameInput == "admin" and passwordInput == "1234" :
    print("Done !")
    print("*********Welcome Bkk Service*********")
    print("1. ram")
    print("2. mouse")
    print("3. monitor")
    print("4. keyboard")
    print("5. loudspeaker")
    item = int(input("select number item :"))
    quantity = int(input("how many item :"))
    ram = 50
    mouse = 20
    monitor = 100
    keyboard = 20
    loudspeaker = 10
    print("------------------------------------")
    if item == 1:
        print("TOTAL : ", ram*quantity)
    elif item == 2:
        print("TOTAL : ", mouse*quantity)
    elif item == 3:
        print("TOTAL : ", monitor*quantity)
    elif item == 4:
        print("TOTAL : ", keyboard*quantity)
    elif item == 5:
        print("TOTAL : ", loudspeaker*quantity)

    print("------------------------------------")

    print("****Thank you ples visit us again****")
else:
    print("Error")




