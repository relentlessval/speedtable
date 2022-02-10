import random, time, json, os, sys

def delay(sec):
    time.sleep(sec)

class App:
    def __init__(self, score, player):
        self.score = score
        with json.load(open("player.json", 'w')) as pf:
            # i really like the abbreviation of [pf], as not only is that the first two letters in the name of an AMAZING restaurant, but it's also a lot simpler than writing
            # [player] or [playerfile] and i can use it practically anywhere
            self.player = pf
            if self.player.name == "":
                self.player.name = input("What do you want to be called? ")
                pf.name = self.player.name
                json.dump(pf)

            
    def launch(self):
        print("Hi, " + self.player.name + "!")
        if self.player.hasPlayed == True:
            pass
        else:
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
        while choice != 1 or 2 or 3 or 4:
            os.system('clear')
            print("--==[ Menu ]==--")
            print("----------------")
            print("--==[ Game ]==--")
            print("--==[Thanks]==--")
            print(" --==[ HSL ]==--")
            
