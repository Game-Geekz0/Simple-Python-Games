# Sammy Hummel
# connect four game
# jun 19 2025
import os
import random

# var's
a1 = "a1"
a2 = "a2"
a3 = "a3"
b1 = "b1"
b2 = "b2"
b3 = "b3"
c1 = "c1"
c2 = "c2"
c3 = "c3"

exit = False

# pick your poison, X or O
while True:
    op = input("would you like to be X's or O's? [X/O]: ")
    if op == "O" or op == "o" or op == "O's" or op == "o's" or op == "os" or op == "Os":
        op = "O"
        ai = "X"
        break
    if op == "x" or op == "X" or op == "xs" or op == "Xs" or op == "X's" or op == "x's":
        op = "X"
        ai = "O"
        break
    else:
        print("I dont know what that means")

# hope no ones using this on dos, idk dos commands. dir? thats about the extent of my knowledge
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

num = 0

# print the board
print(a1 + "|" + a2 + "|" + a3)
print("--+--+--")
print(b1 + "|" + b2 + "|" + b3)
print("--+--+--")
print(c1 + "|" + c2 + "|" + c3)

while True:
    num = num + 1

    # get player input
    while True:
        if num == 1:
            pl = input(f"where would you like to place your {num}'st {op}?: ")
        elif num == 2:
            pl = input(f"where would you like to place your {num}'nd {op}?: ")
        elif num == 3:
            pl = input(f"where would you like to place your {num}'rd {op}?: ")
        else:
            pl = input(f"where would you like to place your {num}'th {op}?: ")

        if pl == "a1" and a1 == "a1":
            break
        elif pl == "a2" and a2 == "a2":
            break
        elif pl == "a3" and a3 == "a3":
            break
        elif pl == "b1" and b1 == "b1":
            break
        elif pl == "b2" and b2 == "b2":
            break
        elif pl == "b3" and b3 == "b3":
            break
        elif pl == "c1" and c1 == "c1":
            break
        elif pl == "c2" and c2 == "c2":
            break
        elif pl == "c3" and c3 == "c3":
            break
        else:
            print("Please give me a spot on the board above that is empty")

    # this is so stupid but I'm too tired to do better
    if pl == "a1":
        a1 = " " + op
    if pl == "a2":
        a2 = " " + op
    if pl == "a3":
        a3 = " " + op
    if pl == "b1":
        b1 = " " + op
    if pl == "b2":
        b2 = " " + op
    if pl == "b3":
        b3 = " " + op
    if pl == "c1":
        c1 = " " + op
    if pl == "c2":
        c2 = " " + op
    if pl == "c3":
        c3 = " " + op

    # clear screen 
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(a1 + "|" + a2 + "|" + a3)
    print("--+--+--")
    print(b1 + "|" + b2 + "|" + b3)
    print("--+--+--")
    print(c1 + "|" + c2 + "|" + c3)

    # this is possibly the most bullshit unoptimized thing ive ever made but I rufuse to google how to fix it
    if a1 == " " + op and a2 == " " + op and a3 == " " + op:
        print(f"Congrats! You ({op}) won!")
        break
    if b1 == " " + op and b2 == " " + op and b3 == " " + op:
        print(f"Congrats! You ({op}) won!")
        break
    if c1 == " " + op and c2 == " " + op and c3 == " " + op:
        print(f"Congrats! You ({op}) won!")
        break
    if a1 == " " + op and b1 == " " + op and c1 == " " + op:
        print(f"Congrats! You ({op}) won!")
        break
    if a2 == " " + op and b2 == " " + op and c2 == " " + op:
        print(f"Congrats! You ({op}) won!")
        break
    if a3 == " " + op and b3 == " " + op and c3 == " " + op:
        print(f"Congrats! You ({op}) won!")
        break
    if a1 == " " + op and b2 == " " + op and c3 == " " + op:
        print(f"Congrats! You ({op}) won!")
        break
    if a3 == " " + op and b2 == " " + op and c1 == " " + op:
        print(f"Congrats! You ({op}) won!")
        break

    if a1 != "a1" and a2 != "a2" and a3 != "a3" and b1 != "b1" and b2 != "b2" and b3 != "b3" and c1 != "c1" and c2 != "c2" and c3 != "c3":
        print("Game over, it's a tie.")
        break

    # AI turn, slow as hell
    # (this is really dumb and not even finished)
    if b2 == "b2":
        ai_spot = "b2"
    else:
        empty = []
        if a1 == "a1":
            empty.append("a1")
        if a2 == "a2":
            empty.append("a2")
        if a3 == "a3":
            empty.append("a3")
        if b1 == "b1":
            empty.append("b1")
        if b2 == "b2":
            empty.append("b2")
        if b3 == "b3":
            empty.append("b3")
        if c1 == "c1":
            empty.append("c1")
        if c2 == "c2":
            empty.append("c2")
        if c3 == "c3":
            empty.append("c3")
        ai_spot = random.choice(empty)

    if ai_spot == "a1":
        a1 = " " + ai
    if ai_spot == "a2":
        a2 = " " + ai
    if ai_spot == "a3":
        a3 = " " + ai
    if ai_spot == "b1":
        b1 = " " + ai
    if ai_spot == "b2":
        b2 = " " + ai
    if ai_spot == "b3":
        b3 = " " + ai
    if ai_spot == "c1":
        c1 = " " + ai
    if ai_spot == "c2":
        c2 = " " + ai
    if ai_spot == "c3":
        c3 = " " + ai

    print(f"The AI put a {ai} at {ai_spot}")

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(a1 + "|" + a2 + "|" + a3)
    print("--+--+--")
    print(b1 + "|" + b2 + "|" + b3)
    print("--+--+--")
    print(c1 + "|" + c2 + "|" + c3)

    if a1 == " " + ai and a2 == " " + ai and a3 == " " + ai:
        print(f"The AI ({ai}) won!")
        break
    if b1 == " " + ai and b2 == " " + ai and b3 == " " + ai:
        print(f"The AI ({ai}) won!")
        break
    if c1 == " " + ai and c2 == " " + ai and c3 == " " + ai:
        print(f"The AI ({ai}) won!")
        break
    if a1 == " " + ai and b1 == " " + ai and c1 == " " + ai:
        print(f"The AI ({ai}) won!")
        break
    if a2 == " " + ai and b2 == " " + ai and c2 == " " + ai:
        print(f"The AI ({ai}) won!")
        break
    if a3 == " " + ai and b3 == " " + ai and c3 == " " + ai:
        print(f"The AI ({ai}) won!")
        break
    if a1 == " " + ai and b2 == " " + ai and c3 == " " + ai:
        print(f"The AI ({ai}) won!")
        break
    if a3 == " " + ai and b2 == " " + ai and c1 == " " + ai:
        print(f"The AI ({ai}) won!")
        break

    if a1 != "a1" and a2 != "a2" and a3 != "a3" and b1 != "b1" and b2 != "b2" and b3 != "b3" and c1 != "c1" and c2 != "c2" and c3 != "c3":
        print("Game over, it's a tie!")
        break

# Notes
# - should really finish those repeated blocks for all lines in ai_move
# - this code is a mess, but it works mostly
# - someday learn loops and arrays, just not today
