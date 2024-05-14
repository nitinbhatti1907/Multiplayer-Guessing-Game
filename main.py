# Title :- Multiplayer Guessing Game
# Discription :- Players input range for the guessing game. Using Python's random module, a number is generated within the specified range. Players take turns guessing the number. If the guess is incorrect, players receive hints to adjust their next guess. The game continues until one player successfully guesses the number. Each player's number of attempts is tracked. Finally, the winner is declared based on the player with the fewest attempts, or in case of a tie, both players are congratulated.

import random
global i
i=0
p1 = input("Enter Player-1 Name : ")
p2 = input("Enter Player-2 Name : ")
while True:
    try:
        a = int(input("Enter The Starting Point : "))
        b = int(input("Enter The Ending Point : "))

    except ValueError:
        print("Enter a valid input!!!")
        continue

    else:
         break
if a >b or a==b:
    print("Enter Range Is Not Cosidered As Input")
    print("Game Over!!!")

def Guess_game():
    global count
    global guess
    try:

        lucky = random.randint(a, b)
        guess = int(input(f"Guess The Number Between {a} to {b}: "))
        count = 1
        while guess!=lucky:
            if guess<lucky:
                print("Wrong!!! Choose Greater Number.")
            else:
                print("Wrong!!! Choose Lesser Number.")
            guess = int(input(f"Guess The Number Between {a} to {b}: "))
            count+=1
        print(f"Good In {count} Attempts You Guess Correct...\n")

    except ValueError:
        print("Wrong Input... Play again!!!")
        if i==0:
            return player1()
        else:
            return player2()

def player1():
    print(f"Round-1 For {p1}...\n")
    return Guess_game()

def player2():
    global score
    i+=1
    score = count
    print(f"Round-2 For {p2}...\n")
    return Guess_game()

def result():
    if score<count:
       print(f"{p1} is Winner!!!")

    elif score>count:
        print(f"Congratulations,{p2} is Winner!!!")

    else:
        print("Congratulations,The match is tie!!!")

player1()
player2()
result()

