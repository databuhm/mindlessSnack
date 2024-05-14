# Let's play Rock, Paper, Scissors!

import os, time, random

def gameIntro():
    print("[&] Rock, Paper, Scissors Game! [&]")
    print("$-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+$")

def getName():
    userName = str(input("Name > "))
    return userName

def setUpIntro(userName):
    print(f"{userName}, best of luck!")
    print("Preparing the game.")
    time.sleep(1)

def screenClear():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Mac and Linux
        os.system('clear')

def initPlay(userName, initCoin):
    print("[User Info]")
    print(f"-- User Name: {userName}")
    print(f"-- User Coin: {initCoin}\n")
    print("[+] Menu")
    print("1: Play")
    print("0: Exit")

    while True:
        try:
            playChoice = int(input(">>> \n"))
            if playChoice in [0, 1]:
                return playChoice
            else:
                print("Please enter 0 or 1.\n")
        except ValueError:
            print("Please enter 0 or 1.\n")

def gameOutro():
    print("\n[&] Exiting the game. [&]")
    print("[&] Good Bye! [&]")
    print("$-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+$")

def userChoiceWay(userChoice):
    if userChoice == 0:
        gameOutro()
        exit()

def betCoin(initCoin):
    print(f"\nCurrent Coins: {initCoin}")
    print("Enter the number of coins to bet for this game.")
    while True:
        try:
            userBet = int(input(">>> \n"))
            if userBet <= initCoin and userBet > 0:
                return userBet
            elif userBet <= 0:
                print("The betting amount must be more than 0.\n")
            else:
                print("You do not have enough coins.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def getUserRPS(dictRPS):
    print("\n[-] Please choose one of the following.")
    for key, value in dictRPS.items():
        print(f"{key}: {value}")
    while True:
        try:
            userRPS = int(input(">>> \n"))
            if userRPS in dictRPS:
                return dictRPS[userRPS]
            else:
                print("Please select from 0, 1, 2.\n")
        except ValueError:
            print("Please enter a number.\n")

def getComputerRPS(dictRPS):
    computerRPS = random.choice(list(dictRPS.keys()))
    return dictRPS[computerRPS]

def showRPSAnimation(dictRPS):
    for key in sorted(dictRPS.keys()):
        screenClear()
        print(dictRPS[key], end="\r", flush=True)
        time.sleep(0.7)
        screenClear()

def showBothResult(userChoice, computerChoice):
    print(f"\n[$] User: {userChoice}")
    print(f"[$] Computer: {computerChoice}")

def determineWinner(userChoice, computerChoice, userBet, initCoin):
    showBothResult(userChoice, computerChoice)
    if userChoice == computerChoice:
        return initCoin, "[$] Game Result: It's a tie!"
    elif (userChoice == "Rock" and computerChoice == "Scissors") or \
         (userChoice == "Paper" and computerChoice == "Rock") or \
         (userChoice == "Scissors" and computerChoice == "Paper"):
        initCoin += userBet
        return initCoin, "[$] Game Result: Congratulations, you won!"
    else:
        initCoin -= userBet
        return initCoin, "[$] Game Result: Unfortunately, the computer won."

def playAgain(initCoin):
    if initCoin <= 0:
        print("[$] You have run out of coins. Exiting the game.")
        gameOutro()
        exit()
    else:
        print("\n[+] Would you like to play again?")
        print("1: Yes")
        print("0: No")
        while True:
            try:
                choice = int(input(">>> \n"))  
                if choice == 1:
                    return True
                elif choice == 0:
                    gameOutro()
                    exit()
                else:
                    print("Please choose between 0 and 1.\n")
            except ValueError:
                print("Please choose between 0 and 1.\n")

# Main Game Loop
gameIntro()
userName = getName()
initCoin = 1000
firstTime = True

while True:
    if firstTime:
        setUpIntro(userName)
        screenClear()
        userChoice = initPlay(userName, initCoin)
        userChoiceWay(userChoice)
        firstTime = False
    userBet = betCoin(initCoin)
    dictRPS = {0: "Rock", 1: "Paper", 2: "Scissors"}
    userChoice = getUserRPS(dictRPS)
    computerChoice = getComputerRPS(dictRPS)
    showRPSAnimation(dictRPS) # Show Animation
    initCoin, result = determineWinner(userChoice, computerChoice, userBet, initCoin)
    print(result)
    if not playAgain(initCoin):
        break
