import database

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_question(self):
        answer = input(self.question + " ")
        if answer.lower() == self.answer.lower():
            print("Correct! ✅")
            return True
        else:
            print("Incorrect! ❌")
            return False


class Person:
    def __init__(self, name, score=0):
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

player = Person(input("Enter your name: "))
for question in questions:
    if question.ask_question():
        player.add_point()

cursor.execute("INSERT INTO history (name, score) VALUES (?, ?)", (player.name, player.score))
conn.commit()
print(f" Great job, {player.name}! You got {player.score} out of {len(questions)} questions right!")

conn.close()