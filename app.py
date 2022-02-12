import time, sys, os
from game import game

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
    print("3) --==[ Exit ]==--")
    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input("Please select an option:\n>>> "))
        if choice != 1 and choice != 2 and choice != 3:
            print("That's not a valid option! Please enter 1, 2, or 3!")
    if choice == 1:
        while quit != True:
            game()
    elif choice == 2:
        credits()
    elif choice == 3:
        print("See you later!")
        sys.exit()
def credits():
    print("This game was created entirely by @simplesentai (on GitHub).")
    launch()

launch()