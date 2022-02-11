import random
from datetime import datetime

print("Game Start!")
start = input("Ready? (yes or no) ")
if start.lower == "yes":
    score = 0
    while missedQuestion == False:
        question = {
            "factors": [],
            "ans": 0,
            "playerAns": 0
        }
        question.factors.append(random.randint(0,12))
        question.factors.append(random.randint(0,12))
        question.update({"ans": factors[0] + factors[1]})
        presentQuestion = datetime.now()
        print("   "+question.factors[0])
        print(" x "+question.factors[1])
        print("--------")
        question.update({"playerAns": int(input())})
        if question.playerAns == question.ans:
            guessRight = datetime.now()
            result = guessRight - presentQUestion
            if result < 5000:
                score = score + 1
