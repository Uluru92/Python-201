# ingredients.py
def prepare(ingredient):
    return f"cooked {ingredient}"

carrot = "carrot"
salt = "salt"
potato = "potato"



from ingredients import ingredient_4

if __name__ == "__main__":
    print(prepare(potato))
    print(prepare(carrot))
    print(prepare(ingredient_4))