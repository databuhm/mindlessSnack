# Let's play Rock, Paper, Scissors!

import os, time, random

def gameIntro():
    print("[&] 가위바위보 게임! [&]")
    print("$-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+$")

def getName():
    userName = str(input("이름 > "))
    return userName

def setUpIntro(userName):
    print(f"{userName} 님, 행운을 빕니다!")
    print("게임을 준비 중입니다.")
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
                print("0 또는 1을 입력해주세요.\n")
        except ValueError:
            print("0 또는 1을 입력해주세요.\n")

def gameOutro():
    print("\n[&] 게임을 종료합니다. [&]")
    print("[&] Good Bye! [&]")
    print("$-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+$")

def userChoiceWay(userChoice):
    if userChoice == 0:
        gameOutro()
        exit()

def betCoin(initCoin):
    print(f"\n현재 보유 코인: {initCoin}")
    print("이번 게임에 베팅할 코인을 입력해주세요.")
    while True:
        try:
            userBet = int(input(">>> \n"))
            if userBet <= initCoin and userBet > 0:
                return userBet
            elif userBet <= 0:
                print("베팅 금액은 0보다 커야 합니다.\n")
            else:
                print("당신의 코인이 충분하지 않습니다.\n")
        except ValueError:
            print("올바른 숫자를 입력해주세요.\n")

def getUserRPS(dictRPS):
    print("\n[-] 아래 선택지 중 하나를 선택해주세요.")
    for key, value in dictRPS.items():
        print(f"{key}: {value}")
    while True:
        try:
            userRPS = int(input(">>> \n"))
            if userRPS in dictRPS:
                return dictRPS[userRPS]
            else:
                print("0, 1, 2 중에 선택해주세요.\n")
        except ValueError:
            print("숫자로 입력해주세요.\n")

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
        return initCoin, "[$] Game 결과: 무승부!"
    elif (userChoice == "가위" and computerChoice == "보") or \
         (userChoice == "바위" and computerChoice == "가위") or \
         (userChoice == "보" and computerChoice == "바위"):
        initCoin += userBet
        return initCoin, "[$] Game 결과: 축하합니다, 당신이 이겼습니다!"
    else:
        initCoin -= userBet
        return initCoin, "[$] Game 결과: 안타깝지만, 컴퓨터가 이겼습니다."

def playAgain(initCoin):
    if initCoin <= 0:
        print("[$] 당신의 코인이 모두 소진되었습니다. 게임을 종료합니다.")
        gameOutro()
        exit()
    else:
        print("\n[+] 다시 플레이하시겠습니까?")
        print("1: 예")
        print("0: 아니요")
        while True:
            try:
                choice = int(input(">>> \n"))  
                if choice == 1:
                    return True
                elif choice == 0:
                    gameOutro()
                    exit()
                else:
                    print("0과 1중에 선택해주세요.\n")
            except ValueError:
                print("0과 1중에 선택해주세요.\n")

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
    dictRPS = {0: "가위", 1: "바위", 2: "보"}
    userChoice = getUserRPS(dictRPS)
    computerChoice = getComputerRPS(dictRPS)
    showRPSAnimation(dictRPS) # Show Animation
    initCoin, result = determineWinner(userChoice, computerChoice, userBet, initCoin)
    print(result)
    if not playAgain(initCoin):
        break
