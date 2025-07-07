#sammy hummel
#6-jul-25
#wordle like game
import random
import os
import time
os.system('cls' if os.name == 'nt' else 'clear')
print("Choose your diffuculty")
dif = input("(1-3): ")
while True:
    if dif in ["1", "2", "3"]:
        print("")
        break
    else:
        print("choose either a 1, 2, 3 with one being easy and 3 being hard")
        dif = input("(1-3): ")
#List of words/pick diffucuty
with open("usablewords.txt", "r") as file:
    wordle_words = file.read().splitlines()
with open("easywords.txt", "r") as file:
    easy_words = file.read().splitlines()
with open("mediumwords.txt", "r") as file:
    medium_words = file.read().splitlines()



#set everything blank
v = " "
s1 = s2 = s3 = s4 = s5 = v
line1 = line2 = line3 =line4 = line5 = line6  = "[ ][ ][ ][ ][ ]"
#instructions/first print
os.system('cls' if os.name == 'nt' else 'clear')

print ("type {HELP} for instructions")
print("type {EXIT} to exit")
print (" ")
#make it randomize
RESET = True
round = 0
while True:
    # randomizer
    if RESET == True:
        if dif == "3":
            rnd = random.choice(wordle_words)
        elif dif == "2":
            rnd = random.choice(easy_words)
        elif dif == "1":
            rnd = random.choice(medium_words)
        else:
            break
        line1 = line2 = line3 =line4 = line5 = line6  = "[ ][ ][ ][ ][ ]"
        round = 0
        RESET = False
    #cheat
    #print(rnd)
    print("   Wordle")
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    #letters
    letter1 = rnd [0]
    letter2 = rnd [1]
    letter3 = rnd [2]
    letter4 = rnd [3]
    letter5 = rnd [4]
    #get user input
    usr = input ("")
    # is the word 5 letters?
    if len(usr) != 5:
        print ("Please enter a 5 letter word:")
        usr = input ("")
        if len(usr) != 5:
            print("what did I JUST say?")
            usr = input("")
            if len(usr) != 5:
                print("LAST CHANCE")
                use = input("")
                if len(usr) != 5:
                    print("...okay, you asked for this")
                    time.sleep(.5)
                    break
    # is it in list?
    if usr in wordle_words:
        print("")
    else:
        while True:
            if len(usr) == 5:
                usr = input("Not In Word List: ")
                if usr in wordle_words:
                    print("")
                    break
            else:
                print("Please enter a 5 letter word:")
                usr = "fhdjr"

    #Help Menu
    if usr in ["HELP", "help", "Help", "{Help}", "{HELP}", "{help}"]:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("Wordle is a guessing game with words.\n")
        print("You have 6 tries to guess a secret 5-letter word.\n")
        print("Each time you guess, the game tells you if your letters are right or wrong:\n")
        print("     If a letter is green, \nit means that letter is correct and in the right spot.\n")
        print("     If a letter is yellow, \nit means the letter is in the word but in a different spot.\n")
        print("     If a letter is red, \nit means the letter is not in the word at all.\n")
        print("Use the clues to guess the word correctly before you run out of tries!\n")
        input("Press Enter To Play: ")
        usr = "     "
        RESET = True
    #exit
    if usr in ["EXIT", "Exit", "exit", "{EXIT}", "{Exit}", "exit"]:
        break
    #not commit die when I accidentally type a 4 letter word
    if len(usr) < 5:
        print ("Please enter a 5 letter word:")
        usr = input ("")
        if len(usr) < 5:
            print("what did I JUST say?")
            usr = input("")
            if len(usr) < 5:
                print("LAST CHANCE")
                use = input("")
                if len(usr) < 5:
                    print("...okay, you asked for this")
                    time.sleep(.5)
                    break
    #decode user input
    use1 = usr [0]
    use2 = usr [1]
    use3 = usr [2]
    use4 = usr [3]
    use5 = usr [4]
    #Correct
    if use1 == letter1:
        s1 = "\033[32m" + use1 + "\033[0m"
        d1 = True
    #yellow
    elif use1 in rnd:
        s1 = "\033[33m" + use1 + "\033[0m"
        d1 = False
    #red
    else:
        s1 = "\033[31m" + use1 + "\033[0m"
        d1 = False

    if use2 == letter2:
        s2 = "\033[32m" + use2 + "\033[0m"
        d2 = True
    elif use2 in rnd:
        s2 = "\033[33m" + use2 + "\033[0m"
        d2 = False
    else:
        s2 = "\033[31m" + use2 + "\033[0m"
        d2 = False

    if use3 == letter3:
        s3 = "\033[32m" + use3 + "\033[0m"
        d3 = True
    elif use3 in rnd:
        s3 = "\033[33m" + use3 + "\033[0m"
        d3 = False
    else:
        s3 = "\033[31m" + use3 + "\033[0m"
        d3 = False

    if use4 == letter4:
        s4 = "\033[32m" + use4 + "\033[0m"
        d4 = True
    elif use4 in rnd:
        s4 = "\033[33m" + use4 + "\033[0m"
        d4 = False
    else:
        s4 = "\033[31m" + use4 + "\033[0m"
        d4 = False

    if use5 == letter5:
        s5 = "\033[32m" + use5 + "\033[0m"
        d5 = True
    elif use5 in rnd:
        s5 = "\033[33m" + use5 + "\033[0m"
        d5 = False
    else:
        s5 = "\033[31m" + use5 + "\033[0m"
        d5 = False


    round = round + 1

    
    #print line
    if round == 1:
        line1 = "[" + s1 + "][" + s2 + "][" + s3 + "][" + s4 + "][" + s5 + "]"
    if round == 2:
        line2 = "[" + s1 + "][" + s2 + "][" + s3 + "][" + s4 + "][" + s5 + "]"
    if round == 3:
        line3 = "[" + s1 + "][" + s2 + "][" + s3 + "][" + s4 + "][" + s5 + "]"
    if round == 4:
        line4 = "[" + s1 + "][" + s2 + "][" + s3 + "][" + s4 + "][" + s5 + "]"
    if round == 5:
        line5 = "[" + s1 + "][" + s2 + "][" + s3 + "][" + s4 + "][" + s5 + "]"
    if round == 6:
        line6 = "[" + s1 + "][" + s2 + "][" + s3 + "][" + s4 + "][" + s5 + "]"
        time.sleep(0.1)
    #losing screen
    if round == 6 and (d1 != True or d2 != True or d3 != True or d4 != True or d5 != True):

        os.system('cls' if os.name == 'nt' else 'clear')
        RED = "\33[91m"
        BOLD = "\033[1m"
        RESET = "\033[0m"

        lines = [
        "",
        f"{BOLD}{RED}{'*' * 40}{RESET}",
        f"{BOLD}{RED}{'YOU LOST':^40}{RESET}",
        f"{BOLD}{RED}{'*' * 40}{RESET}",
        "",
        f"{BOLD}{'The word was ' + rnd :^40}{RESET}",
        ""
        ]
 
        for line in lines:
            print(line)  
        again = input ("would you like to play again? [Y/N]: ")
        if again in ["Yes", "YES", "Y", "y", "ye", "Ye", "yes"]:
            RESET = True
            os.system('cls' if os.name == 'nt' else 'clear')
            
        else:
            break
 

    os.system('cls' if os.name == 'nt' else 'clear')
    #winning screen
    if d1 and d2 and d3 and d4 and d5 == True:
        round = str(round)
        os.system('cls' if os.name == 'nt' else 'clear')
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        BOLD = "\033[1m"
        RESET = "\033[0m"

        lines = [
        "",
        f"{BOLD}{YELLOW}{'*' * 40}{RESET}",
        f"{BOLD}{GREEN}{'YOU WIN!':^40}{RESET}",
        f"{BOLD}{YELLOW}{'*' * 40}{RESET}",
        "",
        f"{BOLD}{'You Got ' + rnd + ' in '  + round :^40}{RESET}",
        ""
        ]

        for line in lines:
            print(line)  
        again = input ("would you like to play again? [Y/N]: ")
        if again in ["Yes", "YES", "Y", "y", "ye", "Ye", "yes"]:
            RESET = True
            os.system('cls' if os.name == 'nt' else 'clear')
            
        else:
            break
        
