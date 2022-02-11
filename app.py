import random, time, json, os, sys
from game.py import game
from lead.py import showLeaderboard

def delay(sec):
    time.sleep(sec)

def launch():
    choice = input("Have you played before? (type yes or no) ")
    choice = choice.lower()
    if choice == "yes":
        pass
    elif choice == "no":
        print("Okay, then!")
        delay(1.25)
        print("This game is surprisingly easy, considering it's made for review! All you have to do is put in the correct answer to the question provided as fast as possible!")
        delay(1.25)
        print("If your keyboard has a keypad (there's a square of numbers), be sure to turn on [NumLock]!")
        delay(1.25)
        print("The faster you answer, the more points you'll get!")
        delay(1.25)
        print("However, the moment you get one wrong, everything is over, and you'll have to restart!")
        choice = input("Press enter to continue...")
    os.system('clear')
    print("   --==[ Menu ]==--")
    print("   ----------------")
    print("1) --==[ Game ]==--")
    print("2) --==[Thanks]==--")
    print("3) --==[ High ]==--")
    print("4) --==[ Exit ]==--")
    while choice != '1' or '2' or '3' or '4':
        choice = input("Please select an option:\n>>> ")
        if choice != '1' or '2' or '3' or '4':
            print("That's not a valid option! Please enter 1, 2, 3, or 4!")
    if choice == '1':
        while quit != True:
            game()
    elif choice == '2':
        credits()
    elif choice == '3':
        showLeaderboard(file)
    elif choice == '4':
        print("See you later!")
        sys.exit()
def credits():
    print("This game was created entirely by @simplesentai (on GitHub).")
    launch()
