#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batch_by_ingred = []
    batches = 0
    # if ingredients is missing part of recipe return 0
    if len(recipe) != len(ingredients):
      return batches
    else:
      for i in recipe:
        #push amount of batches per ingredients to list
          batch_by_ingred.append(ingredients[i] // recipe[i])
          #find the minimum number of batches in list
      batches = min(batch_by_ingred)
      return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
  ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))