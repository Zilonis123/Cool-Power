
from engine.func import *
import colorama
colorama.init()

leng = int(input("How far do you want to go?" + colorama.Fore.RED + " Going to far may crash the program. " + colorama.Fore.RESET + " (int) "))

a = by1(leng)

colors = input("Do you want to colored numbers? (y/N) ").lower() == "y"
dictionary = {"0":colorama.Fore.LIGHTBLACK_EX, "1": colorama.Fore.YELLOW, "2": colorama.Fore.CYAN, "3": colorama.Fore.BLUE, "4": colorama.Fore.GREEN, "5": colorama.Fore.MAGENTA,
"6":colorama.Fore.RED, "7":colorama.Fore.LIGHTRED_EX, "8": colorama.Fore.LIGHTMAGENTA_EX, "9": colorama.Fore.LIGHTYELLOW_EX}

# modify the result
first = 0
res = []
for r in a[::-1]:
    p = (" " * (len(str(first))-len(str(r)))) + str(r)
    if colors:
        fixed = ""
        for i in range(len(p)):
            fixed += dictionary.get(p[i], "") + p[i]
        p = fixed
    res.insert(0, p)
    if first == 0:
        first = r
    


for r in res:
    print(r)