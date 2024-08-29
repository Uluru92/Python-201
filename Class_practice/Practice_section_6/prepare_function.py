# ingredients.py
def prepare(ingredient):
    return f"cooked {ingredient}"

carrot = "carrot"
salt = "salt"
potato = "potato"

print(prepare(potato))

from ingredients import ingredient_4

print(prepare(ingredient_4))
print(prepare(carrot))