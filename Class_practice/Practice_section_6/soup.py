#import #1
from ingredients import ingredient_1

print(ingredient_1)

#import #2
import ingredients

print(ingredients.ingredient_2)
print(ingredients.ingredient_3)

#import #3
import ingredients as i
print(i.ingredient_4)
print(i.ingredient_5)


#import #4 DEEPER FOLDERS
import secret_ingredients.super_secret_ingredients as i
print(i.secret_1)
print(i.secret_2)
print(i.secret_3)
print(i.secret_4)
print(i.secret_5)

