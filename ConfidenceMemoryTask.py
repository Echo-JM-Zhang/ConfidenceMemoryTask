import random
import time
import os
import pandas as pd
import csv

def buildArena():
    a = " "
    b = "□"
    ar = [a*2+b+a+b+a*2,b+a*5+b,b+a*5+b]
    return(ar)

def printArena(arena):
    for item in arena:
        print(item)

def changeLight(p: list, arena: list): 
    a = "■"
    b = "□"
    for i in p:
        if i==1:
            light = [2,0]
        elif i==2:
            light = [1,0]
        elif i==3:
            light = [0,2]
        elif i==4:
            light = [0,4]
        elif i==5:
            light = [1,6]
        else:
            light = [2,6]
        s = list(arena[light[0]])
        s[light[1]] = a
        s = "".join(s)
        arena[light[0]] = s

    printArena(arena)

    for i in p:
        if i==1:
            light = [2,0]
        elif i==2:
            light = [1,0]
        elif i==3:
            light = [0,2]
        elif i==4:
            light = [0,4]
        elif i==5:
            light = [1,6]
        else:
            light = [2,6]
        s = list(arena[light[0]])
        s[light[1]] = b
        s = "".join(s)
        arena[light[0]] = s


def portvisit(k: int, ports: list):
    for i in range(len(ports)):
        if ports[i] != 0:
            ports[i] = ports[i] + 1
    ports[k-1] = 1
    return(ports)

def balance(choice: bool, current, amount = 10):
    if choice:
        new = current + 2 * amount
    else:
        new = current - amount
    return(new)

def pseudotask(arena):
    currentBalance = 0
    reward = 10

    ports = [0,0,0,0,0,0]
    l = [1,2,3,4,5,6]
    k = [1,2,3,4,5,6]
    random.shuffle(l)
    random.shuffle(k)
    while l[len(l)-1] == k[0]:
        random.shuffle(l)
        random.shuffle(k)

    i = l+k

    print("Your current balance is: $", currentBalance)
    time.sleep(0.5)
    for items in i:
        changeLight([items], arena)
        select = int(input("Please select a port: "))
        while select != items:
            select = int(input("Wrong choice. Select again: "))
        currentBalance = currentBalance + reward
        time.sleep(0.5)
        print("Correct choice! Your got $10. Your new balance is: $", currentBalance)
        ports = portvisit(items, ports)
        
        time.sleep(0.5)

    return(ports)

def GenerateTaskPair(ports: list):
    correct = list()
    error = list()
    for i in ports:
        if i <= 3:
            error.append(ports.index(i)+1)
        else:
            correct.append(ports.index(i)+1)
    correctIndex = correct[random.randint(0, len(correct)-1)]
    errorIndex = error[random.randint(0, len(error)-1)]

    return([correctIndex, errorIndex])

def task(ports: list, arena: list, balance: int):
    

    pair = GenerateTaskPair(ports)

    print("Your current balance is: $", balance)
    time.sleep(1)
    print("Your game will start in 3 seconds. Good luck!")

    time.sleep(3)

    changeLight(pair, arena)
    select = int(input("Please make a choice: "))
    while not(select == pair[0] or select == pair[1]):
        select = int(input("Invalid choice. Try again: "))
    
    ports = portvisit(select, ports)
    
    time.sleep(0.5)

    wager = int(input("Please enter your wager amount: $"))
    balance = balance - wager

    if select == pair[0]:
        ch = 1
        balance = balance + wager * 2
        print("Correct choice! Your wager is doubled. Now your new balance is: $", balance)
    else:
        ch = 0
        print("Wrong choice. Your lost your wager. Now your balance is: $", balance)
    
    time.sleep(3)
    
    os.system("cls")

    return([balance, ch, wager])
    



if __name__ == "__main__":
    setup = buildArena()
    port = pseudotask(setup)
    myBalance = 120
    trials = list()

    wagerList = list()

    time.sleep(2)
    print("Congratulations! You have passed the tutorial. Now that you have money, we can start gambling. Here are the rules: ")
    time.sleep(5)
    print("1. There will be 2 ports light up. The port you chose long time ago is the correct one, while the port you choose recently is the wrong one")
    time.sleep(5)
    print("2. Correct choice will double your wager and returned to your account. If you make the wrong choice, you will lose your wager")
    time.sleep(5)
    print("3. You need to decide your wager after making a choice. The more you wager, the greater your potential earnings, but also the greater your potential loss.")
    time.sleep(5)
    print("Hope you still remember your choice sequence in the tutorial. Your will make choice for the first couple of trials based on the tutorial choice seqeuence. Good luck for you game!")
    time.sleep(5)
    print("Now you have 15s go back to review the sequence in the tutorial. Once time's up, we will start our game!")
    time.sleep(15)
    

    os.system("cls")

    for i in range(20):
        result = task(port, setup, myBalance)
        myBalance = result[0]
        trials.append(result[1])
        wagerList.append(result[2])

    print("Your total balance is: $", myBalance)
    pcorrect = sum(trials)/len(trials)
    print("Your percentage of correctness is: ", pcorrect)
    df = pd.DataFrame({"trial": range(20), "choice": trials, "wager": wagerList})
    df.to_csv("D://JingminZhang//test_result.csv", index=False)




 
    

