from math import factorial
def lattice_root(width, height):
    answer = (factorial(width + height))/(factorial(width) * factorial(height))
    return answer

print(int(lattice_root(20,20)),"root")
