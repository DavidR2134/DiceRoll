import random
import pyfiglet
import os

def menu():
    t = pyfiglet.figlet_format("Dice Roller")
    print(t)
    print("\n1) Roll!")
    print("2) Generate Character Stats!")
    print("3) Quit")

def clear():
    os.system('clear')

def roll():
    dieType = int(input("What die do you need: > d"))
    dieCount = int(input("How many times would you like to roll: >"))

    dieTotal = 0

    print()
    for i in range(dieCount):
        roll = random.randint(1, dieType)
        dieTotal += roll
        print(f"Roll {i + 1}: {roll}")

    print(f"\nSum of die: {dieTotal}")
    input("\nPlease press enter to continue...")


def generate_character():
    stats = []

    for i in range(6):
        temp = []
        for j in range(4):
            r = random.randint(1,6)
            temp.append(r)
        temp.sort()
        print(temp)
        temp.pop(0)
        stats.append(sum(temp))
    
    print(stats)
    input()

def main():
    while True:
        clear()
        menu()
        choice = int(input("\n> "))

        if choice == 1:
            clear()
            roll()
        elif choice == 2:
            clear()
            generate_character()
        else:
            clear()
            break

if __name__ == "__main__":
    main()