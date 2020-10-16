#Name: AppUI
#Used as the main app control and user interface.
#Team Members: Bryce Benjamin, Cliff Rosenberg, Jordan Christan, Aarush Gupta

from os import system, name #this import is needed to get access to the clear screen function 
from time import sleep 
import pandas as pd
import sqlite3

#clearScreen function used to reset screen after selection to prevent a wall of text as selections are made and data is displayed
def clearScreen(): 

    if name == 'nt': 
        _ = system('cls') 
   
    else: 
        _ = system('clear')

def printWelcome():

    print(r' __  __         ______          _              _____      _')
    print(r'|  \/  |       |  __  \        (_)            |  __ \    | |')
    print(r'| \  / |_   _  | |__) |___  ___ _ _ __   ___  | |__) |_ _| |')
    print(r'| |\/| | | | | |  _  // _ \/ __| |  _ \ / _ \ |  ___/ _` | |')
    print(r'| |  | | |_| | | | \ \  __/ (__| | |_) |  __/ | |  | (_| | |')
    print(r'|_|  |_|\__, | |_|  \_\___|\___|_| .__/ \___| |_|   \__,_|_|')
    print(r'         __/ |                   | |')
    print(r'        |___/                    |_|')
    print('\nThe recipe app that gets you the lowest price for your favorite meals!')

def mainMenu():
    while True:
        try: 
            clearScreen()
            print("\n\t\t\tWelcome\n\t\t\t  to")
            printWelcome()
            print("\nPlease select which meal type you want to cook:\n")
            
            #this for loop displays the menu options. The i variable is used to create a newline space between the last item 
            i = 0
            for key, value in mealTypes.items(): 
                
                if i == 3: print("\n[" + str(key) + "] " + value)
                else: print("[" + str(key) + "] " + value)
                i += 1
            
            selection = input("\n>")
            selection = int(selection)
        except ValueError:
            clearScreen()
            printWelcome()
            print("\nSorry, your input of " + '\"' + selection + '\"' " was an invalid input. Please enter the corresponding number for the meal type you want.")
            sleep(5)
            continue

        if selection >= 1 and selection <= 4: break
        else:
            clearScreen()
            printWelcome()
            print("\nSorry, your selection of " + '\"' + str(selection) + '\"' " was invalid. You must select an option from the list.")
            sleep(5)
            continue
    
    return selection

#function to display menu options and collect user selection
def mealRecipes(mealType):
    
    while True:
        clearScreen()
        printWelcome()
        print("\n--" + mealType.upper() + " RECIPES--\n\nPlease select which recipe you want to cook:\n")
        
        if mealType == "breakfast": mealRecipes = breakfastRecipes.items()
        if mealType == "lunch": mealRecipes = lunchRecipes.items()
        if mealType == "dinner": mealRecipes = dinnerRecipes.items()
            
        i = 0
        for key, value in mealRecipes: 
               
            if i == 2: print("\n[" + str(key) + "] " + value)
            else: print("[" + str(key) + "] " + value)
            i += 1
        
        recipeSelection = input("\n>")
        
        try:
            recipeSelection = int(recipeSelection)
        except ValueError:
            clearScreen()
            printWelcome()
            print("\n--" + mealType.upper() + " RECIPES--\n")
            print("\nSorry, your input of " + '\"' + recipeSelection + '\"' " was an invalid input. Please enter the corresponding number for the recipe you want.")
            sleep(5)
            continue
        
        #ensures that an appropriate selection is made
        if mealType == "breakfast" and recipeSelection >= 1 and recipeSelection <= 3: break
        elif mealType == "lunch" and recipeSelection >= 1 and recipeSelection <= 3: break
        elif mealType == "dinner" and recipeSelection >= 1 and recipeSelection <= 3: break
        else:
            clearScreen()
            printWelcome()
            print("\n--" + mealType.upper() + " RECIPES--\n")
            print("\nSorry, your selection of " + '\"' + str(recipeSelection) + '\"' " was invalid. You must select an option from the list.")
            sleep(5)
            continue
    
    return recipeSelection

#function of retrieve requested scraped data from database
def getPrices (meal, ingredientList):
    
    #sets up sqlite3 database connection
    conn = sqlite3.connect('stores.db')
    c = conn.cursor()
    
    #creates empty dictionary for prices and store key/value pairs
    dictPrices = {}
    
    for store in stores:
        
        #creates empty list to store individual item prices
        listPrices = []
        for row in c.execute('SELECT Product_Price FROM ' + meal + ' WHERE Store=?', (store,)):
            
            #if the price in the DB is less than a dollar, format the price in dollar format and convert to float
            if (len(row[0])) == 3: listPrices.append(float("0." + row[0][:2]))
            #remove dollar sign and convert to float
            else: listPrices.append(float(row[0].split('$')[1]))        
        
        #sum prices in the list
        total = sum(listPrices)
        
        #ensures proper dollar format for display and adds the dollar sign back in after conducting mathematical operations
        if len(str(total).split(".")[1]) > 2: dictPrices[store] = "${:.2f}".format(total)
        else: dictPrices[store] = "$" + str(total)
    
    #displays list of ingredients for selected recipe
    print("\n Ingredients list:\n")
    for ingredient in ingredientList:
        print("\t- " + ingredient)
    print("\n")
    
    #converts dictionary of prices to dataframe for better display of data
    dataframePrices = pd.DataFrame(dictPrices, index = ["Price For Meal"])
    print(dataframePrices)

#function to prompt user if they want to continue to select recipes        
def userContinue():
    
    while True:
        userContinue = str(input("\nDo you want to get prices for another recipe? (Y/N): "))        
        
        if userContinue.upper().strip() == "Y" or userContinue.upper().strip() == "YES":
            return True
        
        if userContinue.upper().strip() == "N" or userContinue.upper().strip() == "NO":
            return False
        else:
            print("\nSorry, your input of " + '\"' + userContinue + '\"' " was an invalid input. Please answer yes or no.")
            
stores = ("Wal-Mart","Target","Giant Eagle")
omeletteRecipe = ("Eggs", "Tomatoes", "Onions", "Mushrooms", "Cheese")
pancakeRecipe = ("Pancake Mix", "Syrup", "Eggs")
tunaRecipe = ("Bread", "Mayonnaise", "Tuna", "Pickles")
burgerRecipe = ("Ground Beef", "Hamberger Buns", "Mayonnaise", "Lettuce", "Onions", "Pickles", "French Fries")
spaghettiRecipe = ("Spaghetti Noodles", "Spaghetti Sauce", "Ground Beef", "Parmesan Cheese")
tacoRecipe = ("Lettuce", "Cheese", "Ground Beef", "Tomatoes", "Taco Shells", "Sour Cream")

mealTypes = {1:"Breakfast", 2:"Lunch", 3:"Dinner", 4:"Quit"}
breakfastRecipes = {1:"Pancakes and Eggs", 2:"Omelette", 3:"Back to main menu"}
lunchRecipes = {1:"Burger and Fries", 2:"Tuna Sandwich", 3:"Back to main menu"}
dinnerRecipes = {1:"Tacos", 2:"Spaghetti and Meatballs", 3:"Back to main menu"}

#main loop for controlling the program
while True: 
    
    mealSelection = mainMenu()
    
    if mealSelection == 1:
        selectionResult = mealRecipes("breakfast")
        if selectionResult == 3: continue
        else: 
            if selectionResult == 1: recipePrice = getPrices("pancake", pancakeRecipe)
            if selectionResult == 2: recipePrice = getPrices("omelette", omeletteRecipe)
            
    if mealSelection == 2: 
        selectionResult = mealRecipes("lunch")
        if selectionResult == 3: continue
        else: 
            if selectionResult == 1: recipePrice = getPrices("burger", burgerRecipe)
            if selectionResult == 2: recipePrice = getPrices("tuna", tunaRecipe)
            
    if mealSelection == 3: 
        selectionResult = mealRecipes("dinner")
        if selectionResult == 3: continue
        else: 
            if selectionResult == 1: recipePrice = getPrices("taco", tacoRecipe)
            if selectionResult == 2: recipePrice = getPrices("spaghetti", spaghettiRecipe)
    
    if mealSelection == 4: 
        print("\nThank you for using My Recipe Pal! Goodbye.")
        sleep(4)
        break
    
    answer = userContinue()
    if answer: continue
    else: 
        print("\nThank you for using My Recipe Pal! Goodbye.")
        sleep(4)
        break
