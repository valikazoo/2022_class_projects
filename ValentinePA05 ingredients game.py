# Jonah Valentine
# jonahfordvalentine@gmail.com
# Programming Assignment PA 5 - Game
#North Seattle College CSC110

import random


def main():
#Storytime prologue
    name = input("Please type in your name: ")
    animal = input("Please input your favorite animal (plural): ")
    fave = input("Type your favorite food (plural): ")
    try:
        number = int(input("Type your favorite number(between 1 and 10): "))
    except ValueError:
        print("numbers invalid. please type in integer form instead of text.")
        number = int(input("Type your favorite number: "))
    holiday= input("Type your favorite holiday: ")
#put error validation here for fave number lol, so it is a NUMBER

#output intro
    print("Welcome.")
    print("Today is the first day of", holiday, ".")
    print("Every year, for three months, it will remain the holiday of", holiday,", regardless of season.")
    print("You,", name,", are tasked with the holy title of cook.")
    print("You hate it, but the Cook is a honored, sacred duty.")
    print("Or so you've been told.")
    print("The", animal, "needs to be present on the first major ceremony.")
    print("Usually the", animal,"get to eat", fave,".")
    print("You need to go out to grab ingredients to cook", fave,"to feed to the holy", animal, ".")
    print("Concentrate on collecting all the supplies and doing all the duties of holy cook, and stay out of trouble.")
    print("Make sure to be prepped for the first ceremony, which is in", number,"day(s). That should be enough time. Definitely.")

#list of ingredients but in library form
    list = ["tomatoes", "sauce", "onions", "garlic", "mushrooms", "broccoli", "carrots", "meat", "stock", "salt", "pepper", "mayonnaise", "beef", "bread buns", "chips","flour", "broth", "chicken", "turkey", "pasta noodles", "pasta", "cheese","beans", "burger patty", "potatoes", "plantains", "corn", "bread", "oregano","parsley", "basil", "thyme", "rosemary", "spices"]

#run first part
    LIST = ingredient_list(fave,list)
#BELOW is just a test that it actually will keep the returned values lol
    print(LIST, "This the list of your ingredients you need to cook", fave,".")

#market time
#it loops for the time of fave number (that is 'days')
    print("It's time to go to the market to search for your ingredients...")
    INGR_COLLECT = {}
    COLLECT = []
    ingr = ["tomatoes", "sauce", "onions", "garlic", "mushrooms", "broccoli", "carrots", "meat", "stock", "salt", "pepper", "mayonnaise", "beef", "bread buns", "chips","flour", "broth", "chicken", "turkey", "pasta noodles", "pasta", "cheese","beans", "burger patty", "potatoes", "plantains", "corn", "bread", "oregano","parsley", "basil", "thyme", "rosemary", "spices"]
    for i in range(int(number)):
        INGR_COLLECT = market(COLLECT, INGR_COLLECT,ingr)
        print("The next day, you go back to another market, again.")
        ingr = ["tomatoes", "sauce", "onions", "garlic", "mushrooms", "broccoli", "carrots", "meat", "stock", "salt", "pepper", "mayonnaise", "beef", "bread buns", "chips","flour", "broth", "chicken", "turkey", "pasta noodles", "pasta", "cheese","beans", "burger patty", "potatoes", "plantains", "corn", "bread", "oregano","parsley", "basil", "thyme", "rosemary", "spices"]
#ending time
    print("You have run out of days!! It is time to cook for the ceremony!...")
    total = []
    score = ending_calc(INGR_COLLECT, total, COLLECT)
#gotta put the BIGGEST ending first in order for it to work lol
    if score >= 2:
        print("you DEFINTELY win!!")
    elif score < 1:
        print("You didn't get enough good ingredients! you lose!")
    elif score >= 1:
        print("You got enough tasty ingredients! you win!")
    else:
        print("what did you even do????")


def ingre_list():
    print("we really don't have a lot.")
    print("list of all ingredients that exist in this world:")
    print("tomatoes sauce, onions, garlic, mushrooms, broccoli, carrots")
    print("stock, salt, pepper, mayonnaise, beef, meat, bread buns, chips")
    print("flour, broth, chicken, turkey, pasta noodles, pasta, cheese")
    print("beans, burger patty, potatoes, plantains, corn, bread, oregano")
    print("parsley, basil, thyme, rosemary, spices.")

 

def ingredient_list(fave,list):
    print("you need to cook", fave)
    print("hmm... what do you need to cook that, again?")
 #INGREDIENT TO LOOK FOR 1
    ingr1 = input("(Please input an ingredient used to make this dish): ")
    if ingr1 == "list":
        ingre_list()
    while ingr1 != list:
        if ingr1 in list:
            break
        elif ingr1 != list:
            print("I don't know what that is. Please try again.")
            print("(hint, if you would like a list of ingredients, type the word list)")
            ingr1 = input("(Please input an ingredient used to make this dish): ")
            if ingr1 == "list":
                ingre_list()
#INGREDIENT TO LOOK FOR 2
    ingr2 = input("(Please input another ingredient used to make this dish): ")
    if ingr2 == "list":
        ingre_list()
    while ingr2 != list:
        if ingr2 in list:
            break
        elif ingr2 != list:
            print("I don't know what that is. Please try again.")
            print("(hint, if you would like a list of ingredients, type the word list)")
            ingr2 = input("(Please input another ingredient used to make this dish): ")
            if ingr2 == "list":
                ingre_list()
#INGREDIENT TO LOOK FOR 3
    ingr3 = input("(Please input ANOTHER ingredient used to make this dish): ")
    if ingr3 == "list":
        ingre_list()
    while ingr3 != list:
        if ingr3 in list:
            break
        elif ingr3 != list:
            print("I don't know what that is. Please try again.")
            print("(hint, if you would like a list of ingredients, type the word list)")
            ingr3 = input("(Please input ANOTHER ingredient used to make this dish): ")
            if ingr3 == "list":
                ingre_list()
#INGREDIENT TO LOOK FOR 4 WHY
    ingr4 = input("(Please input an ingredient used to make this dish): ")
    if ingr4 == "list":
        ingre_list()
    while ingr4 != list:
        if ingr4 in list:
            break
        elif ingr4 != list:
            print("I don't know what that is. Please try again.")
            print("(hint, if you would like a list of ingredients, type the word list)")
            ingr4 = input("(Please input an ingredient used to make this dish): ")
            if ingr4 == "list":
                ingre_list()    
    LIST = []
    LIST.append(ingr1)
    LIST.append(ingr2)
    LIST.append(ingr3)
    LIST.append(ingr4)
#creating list of ingredients to find based on user input
    return LIST

#market collection time
def market(COLLECT, INGR_COLLECT,ingr):
    print("Good morning, welcome to the market!")
    while len(ingr) > 0:
        amount = int(random.randint(0, 11))
        guess = str(input("What are you looking for?: "))
        while guess not in ingr:
            print("I do not understand your response.")
            amount = int(random.randint(0, 11))
            guess = str(input("what u need?: "))
            if guess in ingr:
                print("I have", amount, "in stock: ")
                ingr2 = str(input("Do you want to take? put yes or no: "))
                if ingr2 == "yes":
                    COLLECT.append(guess)
                    INGR_COLLECT[guess] = int(amount)
                    ingr.remove(guess)
                    print("you have taken the ingredient.")
                    print(list(INGR_COLLECT.items()))
                    break
                elif ingr2 == "no":
                    ingr.remove(guess)
                    print("ah... alright then.")
                    break
#catches if first is gotten
        if guess in ingr:
            print("I have", amount, "in stock: ")
            ingr2 = str(input("Do you want to take? put yes or no: "))
            if ingr2 == "yes":
                COLLECT.append(guess)
                INGR_COLLECT[guess] = int(amount)
                ingr.remove(guess)
                print("you have taken the ingredient.")
                print(list(INGR_COLLECT.items()))
            elif ingr2 == "no":
                ingr.remove(guess)
                print("ah... alright then.")

        
#first check for if list is empty or not
            if len(ingr) == 0:
                print("you have run out of time today, next market tomorrow...")
                return INGR_COLLECT

    #this is to leave later
        leave = 'no'
        if leave == "yes":
            break
            return INGR_COLLECT
        leave = str(input("Do you want to try another market? Please type(yes or no): "))
        if leave == 'yes':
            return INGR_COLLECT
#market loop
        while leave != 'yes':
    #looping until choose ingredient
            while guess not in ingr:
                amount = int(random.randint(0, 11))
                guess = str(input("What are you looking for?: "))
                if guess in ingr:
                    print("I have", amount, "in stock: ")
                    ingr2 = str(input("Do you want to take? put yes or no: "))
                    if ingr2 == "yes":
                        COLLECT.append(guess)
                        INGR_COLLECT[guess] = int(amount)
                        ingr.remove(guess)
                        print("you have taken the ingredient.")
                        print(list(INGR_COLLECT.items()))
                        break
                    elif ingr2 == "no":
                        ingr.remove(guess)
                        print("ah... alright then.")
                        break
                    else:
                        print("I do not understand your response.")
    #the if below this is so it catches answer and doesn't go directly to leave market
            #2nd check if list empty
            if len(ingr) == 0:
                print("you have run out of time today, next market tomorrow...")
                return INGR_COLLECT
            amount = int(random.randint(0, 11))
            if guess in ingr:
                print("I have", amount, "in stock: ")
                ingr2 = str(input("Do you want to take? put yes or no: "))
                if ingr2 == "yes":
                    COLLECT.append(guess)
                    INGR_COLLECT[guess] = int(amount)
                    ingr.remove(guess)
                    print("you have taken the ingredient.")
                    print(list(INGR_COLLECT.items()))
                elif ingr2 == "no":
                        ingr.remove(guess)
                        print("ah... alright then.")
                else:
                    print("I do not understand your response.")
#3rd check if list empty
            if len(ingr) == 0:
                print("you have run out of time today, next market tomorrow...")
                return INGR_COLLECT
#ask to leave market after ingr
            leave = str(input("Do you want to try another market? (yes or no): "))
            if leave == 'yes':
                return INGR_COLLECT

#4th check if list is empty
            if len(ingr) == 0:
                print("you have run out of time today, next market tomorrow...")
                return INGR_COLLECT
#leave market
    print("you have run out of time today, next market tomorrow...")
    return INGR_COLLECT

def ending_calc(INGR_COLLECT, total, COLLECT):
    print("you have collected:")
    for k, v in INGR_COLLECT.items():
        print(k, v)
        print(v)
#put all the values into total
        total.append(v)
        
#try to integrate word endings with math
    tasty = ["tomatoes", "sauce", "onions", "garlic", "mushrooms", "broccoli",
             "carrots", "meat", "stock", "salt", "pepper",
             "beef", "chips","broth", "chicken", "turkey", "pasta noodles"]
    best = ["plantains", "oregano","parsley", "pasta","cheese", "basil"]
    okay = ["bread", "bread buns", "potatoes","thyme", "rosemary","burger patty", "flour", "spices"]
    trash = ["chips","mayonnaise", "beans", "corn"]

    check1 = any(item in COLLECT for item in trash)

    if check1 == True:
        print("ew...you chose to cook...this? These ingredients are not it.")
        return -20
    else:
        check2 = any(item in COLLECT for item in okay)
        if check2 == True:
            print("ah...quite an...interesting taste you have... I guess I'll take it...")
            #now add the values and print
            print("you have in total", sum(total), "of all ingredients.")
            score = (sum(total) / 20) - 1
            return score 
        else:
            check3 = any(item in COLLECT for item in tasty)
            if check3 == True:
                print("Ooooo, this looks delicious...")
                #now add the values and print
                print("you have in total", sum(total), "of all ingredients.")
                score = sum(total) / 20
                return score
            else:
                check4 = any(item in COLLECT for item in best)
                if check4 == True:
                    print("This looks like the best dish I've ever seen!")
                    #now add the values and print
                    print("you have in total", sum(total), "of all ingredients.")
                    score = sum(total) / 20
                    return score

#put all the values into total
        total.append(v)

#now add the values and print
    print("you have in total", sum(total), "of all ingredients.")
    score = sum(total) / 20
    return score



main()

