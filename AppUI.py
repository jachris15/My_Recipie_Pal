from os import system, name
from time import sleep
import numpy as np
import pandas as pd
#import db_tables as dbtables
import re


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

omeletteRecipe = ("Eggs", "Tomatoes", "Onions", "Mushrooms", "Cheese")
pancakeRecipe = ("Pancake Mix", "Syrup", "Eggs")
tunaRecipe = ("Bread", "Mayonnaise", "Tuna", "Pickles")
burgerRecipe = ("Ground Beef", "Hamberger Buns", "Mayonnaise", "lettuce", "Onions", "Pickles", "French Fries")
spaghettiRecipe = ("Spaghetti", "Sauce", "Ground Beef", "Parmesan")
tacoRecipe = ("Lettuce", "Cheese", "Ground Beef", "Tomatoes", "Taco Shells", "Sour Cream")

mealTypes = {1:"Breakfast", 2:"Lunch", 3:"Dinner", 4:"Quit"}
breakfastRecipes = {1:"Pancakes and Eggs", 2:"Omelette", 3:"Back to main menu"}
lunchRecipes = {1:"Burger and Fries", 2:"Tuna Sandwich", 3:"Back to main menu"}
dinnerRecipes = {1:"Tacos", 2:"Spaghetti and Meatballs", 3:"Back to main menu"}

while True: 
    
    mealSelection = mainMenu()
    
    if mealSelection == 1:
        selectionResult = mealRecipes("breakfast")
        if selectionResult == 3: continue
        else: 
            if selectionResult == 1: recipePrice = dbtables.get_Pancakes()
            if selectionResult == 2: recipePrice = dbtables.get_Omelette()
            
    if mealSelection == 2: 
        selectionResult = mealRecipes("lunch")
        if selectionResult == 3: continue
        else: 
            if selectionResult == 1: recipePrice = dbtables.get_Burger()
            if selectionResult == 2: recipePrice = dbtables.get_Tuna()
            
    if mealSelection == 3: 
        selectionResult = mealRecipes("dinner")
        if selectionResult == 3: continue
        else: 
            if selectionResult == 1: recipePrice = dbtables.get_Taco()
            if selectionResult == 2: recipePrice = dbtables.get_Spaghetti()
    
    if mealSelection == 4: 
        print("\nThank you for using My Recipe Pal! Goodbye.")
        sleep(4)
        break
    
    print(recipePrice)