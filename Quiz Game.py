# Project 7 - Quiz Game

questions = ("How many elements are in the periodic table", 
             "What is the fruit with the most recorded nutrients ?", 
             "What is the vegetable with the most recorded nutrients ?", 
             "What is the result of 5 + 5 x 5 ?", 
             "How many humans are there on earth today approximately ?")

options = (("A. 116", "B. 176", "C. 98", "D. 118"), 
           ("A. Apple", "B. Watermelon", "C. Pineapple", "D. Kiwi"), 
           ("A. Onion", "B. Green Beans", "C. Carrot", "D. Broccoli"), 
           ("A. 25", "B. 45", "C. 15", "D. 30"), 
           ("A. 7b", "B. 6.5b", "C. 8.1b", "D. 8.5b"))

answers = ("D", "C", "D", "D", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D: )").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct !")
    else:
        print("Incorrect !")
        print(f"{answers[question_num]} is the correct answer !")
    question_num += 1

print("--------------------")
print("      RESULTS       ")
print("--------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}% correct !")
