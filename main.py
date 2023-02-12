MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

import os
import random
from clear import clear
money = 0
#def report():
is_on = True  

def check_ingredients(order_ingredient):
  for item in order_ingredient:
    print(item)
    print(drink.values())
  
      
        

  
  #make = True
  #while make:
    
        
while is_on:
  order = input("What would you like? (expresso/latte/cappuccino): ")
  
  if order == "off":
    is_on = False
  elif order == "report":
    print(f"Water is: {resources['water']} ml")
    print(f"Coffee is: {resources['coffee']} ml")
    print(f"Milk is: {resources['milk']} grams")
    print(f"Profit is {money}")
  else:
    drink = MENU[order]
    check_ingredients(drink["ingredients"]) 
    
                  
    

        
print(order)      
      
    
#check_ingredients(order["ingredients"])      
      
      
      
def make_drink(drink_resources,stock):
  for x in drink_resources:
    print(x) 
    for y in stock:
      print(y)
    
#make_drink(MENU[order],MENU[resources])  
  
  



    
  