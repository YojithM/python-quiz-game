score = 0
questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What is 10 - 4?", "answer": "6"},
    {"question": "What is 3 x 3?", "answer": "9"},
    {"question": "What is 12 / 4?", "answer": "3"},
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What color do you get mixing blue and yellow?", "answer": "green"},
    {"question": "How many continents are there?", "answer": "7"}
]
def ask_question(question):
    answer = input(question["question"] + " ")
    if answer.lower() == question["answer"].lower():
        print("Correct! ✅")
        return True
    else:
        print("Incorrect! ❌")
        return False

for question in questions:
    if ask_question(question):
        score += 1

print(f"You got {score} out of {len(questions)} questions right!")
