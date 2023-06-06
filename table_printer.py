# Program Start.

import os
import colorama

from colorama import Fore, Back, Style

print("***Welcome To Table Printer!***")
print("> You can print the table of any number.")
print("> It should not contain any string or operator.")
print("> Decimal is not supported!\n")

while True:
    try:
        tbn = int(input("Enter a Number: "))
        

        print(f"\n| Table Of {tbn}\n")
        for i in range(1, 11):
            print("|", tbn, "x", i, " =", tbn*i)
        print("\n")

    except KeyboardInterrupt:
        print("\n[Keyboard Interrupt] ~ Exit")
        exit(0)
    
    except:
        print("Please Enter a Number, Not a char")
# Program End.
