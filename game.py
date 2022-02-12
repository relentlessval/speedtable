import random, sys
from datetime import datetime

def game():
    print("Game Start!")
    start = input("Ready? (yes or no) ")
    if start.lower() == "yes":
        missedQuestion = False
        while missedQuestion == False:
            # base framework for questions
            factors = []
            ans = 0
            playerAns = 0
            factors.append(random.randint(0,12))
            factors.append(random.randint(0,12))
            ans = factors[0] * factors[1]
            presentQuestion = datetime.now()
            print("   "+str(factors[0]))
            print(" x "+str(factors[1]))
            print("--------")
            playerAns = int(input())
            if playerAns == ans:
                guessRight = datetime.now()
                result = guessRight - presentQuestion
                print(str(result.seconds)+"s")
                print("Correct!")
            elif playerAns != ans:
                missedQuestion = True
                print("Incorrect!")
                print("The answer was "+str(ans))
                print("Game Over!")
                print("Thanks for playing!")
                sys.exit()

