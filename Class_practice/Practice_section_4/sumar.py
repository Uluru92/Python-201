def get_life_points (life_points: int)-> int:
    """Get an extra +1 life point.
    Args:
        Actual life points (int): Initial life points
    Returns:
        Final life points int(): Total life points
    """
    total_life_points = life_points + 1
    return total_life_points

life_points = 1
total_life_points = get_life_points(life_points)
print(total_life_points)

def sumar_1 (numero):
    suma = numero +1
    return suma


cantidad = 5
suma = sumar_1(cantidad)
print(suma)
