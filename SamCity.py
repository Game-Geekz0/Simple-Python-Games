# sammy hummel
# jun-15
# 2025

#add money system %
#fix day number so it resets %
#fix tax system %
#kill my self %
#todo Leaderboard
#todo Fix formatting %
#Remove fucking stupid way im resseting the progress at restart
#mk csv file to keep leaderboard status
#make way to pick multiple thing at once per day (llike by 3 houses)
#this is the worst optimized code ive ever fucking made


# for random number
import random
# For clear screen
import os
#for sleep so I can make text readable
import time


os.system('cls' if os.name == 'nt' else 'clear')

print("This is a city management game, try not to run out of money. You start with 1000$, Try to make it to day 100")
#for leaderboard
end = False
#was yesterday bad
bad_day = False
#lower tax
tax_reset = True
#make first run
is_first_run = True
#diffuculty for 100+ days
dif = 1
# Money
mon = 1000
#population
pop = 100
#starting tax 
tax = 20
#day 1 start
day = 0
#starting homes 
homes = 0
#name the city
name = input("what do you want to call your city?: ")
os.system('cls' if os.name == 'nt' else 'clear')
#allows me to cheat :)
if name in ["geekz", "Geekz", "Geekzville", "geekzville"]:
    mon = mon + 5000
    tax = tax + 500
#2nd cheat
if name in ["Admin", "admin"]:
    day = day + 95
    mon = mon + 10000
    pop = pop + 10000
    tax = tax + 5000
# while loop
while True:
    #make it so num cant be too big
    if mon > 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368:
        mon = 50000000000000
    if pop > 17976931348623157081452742373170435679807056752584499659891747680315726078002853876058955863276687817154045895351438246423432132688946418276846754670353751698604991057655128207624549009038932894407586850845513394230458323690322294816580855933212334827479782620414472316873817718091929988125040402618412485836:
        pop = 5000000000000000000000
    if tax > 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368:
        tax = 500000000000000
    tax = int(tax)
    pop = int(pop)
    mon = int(mon)
    os.system('cls' if os.name == 'nt' else 'clear')
    day += 1
    ########### RANDOM NUMBER FUNCTION ###########
    danger = random.random() ** 2
    ########### Event ############################
    event = 0
    ###########calculate new stuff daily ##################
    pop1 = int(mon / 60)
    pop2 = int(pop1 / 3)
    tax = tax +  int(pop2 * 0.2)
    tax = tax + 1
    tax1 = int(tax)
    event_score = 0
    pop = int(pop)
    pop = pop + 5
    if bad_day == True:
        pop = pop + 10
        tax = tax + 10
    else:
        homes = int(homes)
    home = int(homes)
    #I NEED TO STOP COMMENTING OUT THIS LINE
    bad_day = False
    #more money = more bad
    if day > 100:
        danger = danger + .8
    if mon > 400000:
        danger = danger + .7
    if mon > 30000:
        danger = danger + .2
        mon = mon + 500
    if mon < 1500:
        danger = danger - .2
    #event trigger
    if danger > 0.75:
        event = 1
    #dont allow bad events to happen for the first 5 days
    if day < 5:
        event = 0

    #population
    pop += pop1
    #total money
    mon += tax
    total = mon

    #BAR
    print(f"###################### day {day} ################################") 
    print(f"Welcome back to {name}!")
    print(f"{name} made {tax1}$ today, not bad.")
    print(f"your current population is {int(pop)}")
    print(f"you now have {int(total)}$ to your name")

    #make event do bad stuff
    if event == 1:
        event_score = random.random() ** 2
        if mon > 50000:
            event_score = event_score + .4
        if day > 100:
            event_score = event_score + .1
        if event_score < 0.6:
            verb = random.choice(["stabbing", "robbery", "gas leak", "escaped clown"])
            print(f" ")
            print(f"OH NO! There was a {verb}! You lost 25% of your money and some people left.")
            mon -= int(mon * 0.25)
            pop -= int(pop * 0.10)
            mon = mon - 150
            pop = pop - 10
            tax = tax - 10
            bad_day = True
            if mon > 10000000000000000:
                mon = mon / 100
        else:
            verb = random.choice(["fire", "flood", "tornado", "giant duck attack"])
            print(" ")
            print(f"DISASTER! A {verb} hit. You lost 95% of your money and a ton of people.")
            mon = mon - (mon * .95)
            pop = pop - int(pop * .75)
            if mon < 1000:
                bad_day = True
            else:
                mon = mon - 250
                pop = pop - 30
                tax = tax / 1.5
                tax = tax - 20
                bad_day = True
            if mon > 1000000000000000000:
                mon = mon / 100


    #failure code
    if pop < 50:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("#### GAME OVER!! ####")
        print("your population went below 50. it's a ghost town now.")
        print(f"final population {int(pop)}, final money {int(mon)}, made it to day {day}")
        if day > 100:
            score = mon + pop + (homes * 100)
            score = int(score)
            print(f" your final score was {score}")
            end = True
        else: 
            ex = input("Would you like to play again? [Y/N]: ")
            if ex in ["Y", "y", "yes", "Yes"]:
            
                #this is a fucking stupid way to do this yet I am too lazy to do it the better way
            
                # Money
                mon = 1000
                #population
                pop = 100
                #starting tax 
                tax = 20
                #day 1 start
                day = 0
                #starting homes 
                homes = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                #name the city
                name = input("what do you want to call your city?: ")
                continue
            else:
                break

    if mon < 0:
        print("#### GAME OVER!! ####")
        print("you went bankrupt and the town fell apart.")
        print(f"final money {int(mon)}, population {int(pop)}, made it to day {day}")
        if day > 100:
            score = mon + pop + (homes * 100)
            score = int(score)
            print(f" your final score was {score}")
            end = True    
        else: 
            ex = input("Would you like to play again? [Y/N]: ")
            if ex in ["Y", "y", "yes", "Yes"]:
            
                #this is a fucking stupid way to do this yet I am too lazy to do it the better way
            
                # Money
                mon = 1000
                #population
                pop = 100
                #starting tax 
                tax = 20
                #day 1 start
                day = 0
                #starting homes 
                homes = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                #name the city
                name = input("what do you want to call your city?: ")
                continue
            else:
                break
    #show leaderboard
    if day > 100 and is_first_run == False and end == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        score = mon + pop + (homes * 100)
        score = int(score)
        print(f"your final score was {score}")
        print(f"but you made it to day {day}")
        pname = input("what is your name?: ")
        #this is a horrid way to do this but I dont want to keep trying to get it to go off a csv file, im sorry future me if im looking at this. please dont cry
        if day > 150:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("#### Leader Board ####")
            print(f"##(1). {pname} {{Day: {day}}} [Score: {score}]")
            print("(2). Lily {Day: 140} [Score: 273249872432453]")
            print("(3). Wyatt {Day: 120} [Score: 174]")
            print("(4). Keaton {Day: 112} [score: 2647]")
        elif day > 140:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("#### Leader Board ####")
            print("(1). Sammy {Day: 150} [Score: 78922342345433]")
            print(f"##(2). {pname} {{Day: {day}}} [Score: {score}]##")
            print("(3). Lily {Day: 140} [Score: 27453]")
            print("(4). wyatt {Day: 120} [score: 174]")
        elif day > 120:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("#### Leader Board ####")
            print("(1). Sammy {Day: 150} [Score: 7892334354345]")
            print("(2). Lily {Day: 140} [Score: 27453]")
            print(f"##(3). {pname} {{Day: {day}}} [Score: {score}]##")
            print("(4). wyatt {Day: 120} [score: 174]")
        elif day > 112:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("#### Leader Board ####")
            print("(1). Sammy {Day: 150} [Score: 789234354356]")
            print("(2). Lily {Day: 140} [Score: 274534663]")
            print("(3). Wyatt {Day: 120} [Score: 174]")
            print(f"##(4). {pname} {{Day: {day}}} [score: {score}]##")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("#### Leader Board ####")
            print("(1). Sammy {Day: 150} [Score: 789243535433]")
            print("(2). Lily {Day: 140} [Score: 274553243453463]")
            print("(3). Wyatt {Day: 120} [Score: 174]")
            print("(4). Keaton {Day: 112} [score: 2647]")
            print(f"##(12). {pname} {{Day: {day}}} [score: {score}]##")  

        break

    

# Options
    print(" ")
    print("### heres what you can do today ###")
    print("1 - build more houses         (500$)  [+2.5% population]")
    print("2 - buy more land             (600$)  [+1% tax income]")
    print("3 - build infrastructure     (1000$) [+5% tax income]")
    print("Q - retire from office")
    print("anything else - skip day")

    cmd = input("what would you like to do?: ").strip().lower()
    all = False
    if cmd in ["1", "2", "3"]:
        much = input(f"how many would you like to buy?(use A for all): ")
        if much in ["A", "a", ""]:
            all = True
        if much.isdigit(): 
            much = int(much)
        else:
            if not all:
                much = 1

    if cmd == "1":
        if all == True:
            num = mon // 500
            num = int(num)
            much = num
        pop = pop + (pop * .025 * much)
        mon = mon - (500 * much)
        homes = homes + (1 * much)
    elif cmd == "2":
        if all == True:
            num = mon // 600
            num = int(num)
            much = num
        tax = tax + (tax * .01 * much)
        mon = mon - (600 * much)
    elif cmd == "3":
        if all == True:
            num = mon // 1000
            num = int(num)
            much = num
        tax = tax + (tax * .05 * much)
        mon = mon - (1000 * much) 


######dev_tools(ish)
    #print(f"danger level = {danger}")
    #print(f"money = {mon}$")
    #print(f"bad event? {event}")
    #print(f"tax = {tax}")
    #print(f"event score is {event_score}")
    #print(f"you have {homes} homes")
    print(f" dif is {dif}")

    if day >= 100 and is_first_run == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("### YOU WIN! ###")
        print("you made it to day 100! nice.")
        print(f"you had {int(mon)}$, {int(pop)} population, and {homes} homes.")
        score = mon + pop + (homes * 100)
        score = int(score)
        print(f"your final score was {score}")
        pl = input("Would you like to keep playing? your tax will be lowered [Y/N]: ")
        if pl in ["Y", "y", "yes", "Yes", " ", ""]:
            is_first_run = False
        else:
             break
    #make game harder after day 100
    if is_first_run == False:
        dif = dif - .03
        mon = mon * dif
        pop = pop * dif
        if tax_reset == True:
            tax = tax / 4
            tax_reset = False

    os.system('cls' if os.name == 'nt' else 'clear')
    if cmd in ["q", "Q"]:
        print("thanks for playing, mayor.")
        break
