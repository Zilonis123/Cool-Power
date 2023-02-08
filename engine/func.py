
import math

# These function names could be and should be changed to be more descriptive.





# this function is going to return a list of li
def by1(l: int=0) -> list:
    power = []
    for i in range(l):
        power.append(math.floor(math.pow(2, i)))
    return power


def by10(l: int=0) -> list:
    power = []

    numbers = []
    # make the numbers we will power
    # this loop could be converted to something else, but i have zero idea how to do that
    for i in range(l):
        num = int("1" + ("0"*i))
        numbers.append(num)

    for i in numbers:
        power.append(math.floor(math.pow(2, i)))

    return power


by1()