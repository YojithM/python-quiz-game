import database

class Question:
    def __init__(self, question, answer, times_wrong = 0):
        self.question = question
        self.answer = answer
        self.times_wrong = times_wrong

    def ask_question(self):
        answer = input(self.question + " ")
        if answer.lower() == self.answer.lower():
            print("Correct! ✅")
            return True
        else:
            print("Incorrect! ❌")
            self.times_wrong += 1
            return False


class Person:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def add_point(self):
        self.score += 1

questions = [
    Question("What is 2 + 2?", "4"),
    Question("What is 5 + 3?", "8"),
    Question("What is 10 - 4?", "6"),
    Question("What is 3 x 3?", "9"),
    Question("What is 12 / 4?", "3"),
    Question("What is the capital of France?", "Paris"),
    Question("What color do you get mixing blue and yellow?", "green"),
    Question("How many continents are there?", "7")
]

conn = database.setup_database()
cursor = conn.cursor()
cursor.execute("SELECT * FROM history")
past_score = cursor.fetchall()

print("Past Scores:")
for record in past_score:
    print(f"Name: {record[0]}, Score: {record[1]}")

first_try_correct = 0
player = Person(input("Enter your name: "))
for question in questions:
    if question.ask_question():
        player.add_point()
        first_try_correct += 1

remaining = []
for question in questions:
    if question.times_wrong > 0:
        remaining.append(question)

while remaining:
    still_wrong = []
    for question in remaining:
        if question.ask_question():
            player.add_point()
        else:
            still_wrong.append(question)
    remaining = still_wrong
    if remaining:
        print("Let's try the questions you got wrong again!")
    else:
        print("Great job! You've answered all questions correctly!")

print(f"\nFirst-try correct: {first_try_correct} out of {len(questions)}")
print(f"Needed review: {len(questions) - first_try_correct}")

cursor.execute("INSERT INTO history (name, score) VALUES (?, ?)", (player.name, player.score))
conn.commit()
print(f"Great job, {player.name}! You got {player.score} out of {len(questions)} questions right!")

conn.close()