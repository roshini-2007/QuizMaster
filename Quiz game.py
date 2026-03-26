quiz = { 
    "Capital of India": "delhi", 
    "2 + 2": "4", 
    "Color of sky": "blue" 
}

questions = list(quiz.keys())

hints = (
    "Think about general knowledge", 
    "Simple math", 
    "Look at the sky"
)

answered = set()
score = 0

for i in range(len(questions)):
    print("\nQuestion:", questions[i])
    print("Hint:", hints[i])

    user = input("Your answer: ").lower()
    answered.add(questions[i])

    if user == quiz[questions[i]]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nAnswered Questions:", answered)
print("Your Score:", score)
