import random
from questions import questions

score = 0
count = 0


def random_question():
    q = random.choice(questions)
    return q


while count < 3:
    qu = random_question()
    print(qu["ques"])
    for i in qu["options"]:
        print(qu["options"].index(i) + 1, i)
    a = int(input("Select the option: "))
    try:
        if qu["options"][a-1] == qu["correct"]:
            score += 1
            print("Correct answer!!!\nYour score is ", score)
        else:
            print(f"OOPS Wrong!!\nThe correct answer is {qu['correct']} \nYour score is", score)
    except IndexError:
        print(f"Invalid input!!\nThe correct answer is {qu['correct']} \nYour score is ", score)
    finally:
        count += 1
print("Quiz Ended!!")
print("Your Final Score is: ", score)
