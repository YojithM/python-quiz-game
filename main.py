import database
import tkinter as tk

class Question:
    def __init__(self, question, answer, times_wrong = 0):
        self.question = question
        self.answer = answer
        self.times_wrong = times_wrong

    def check_answer(self, typed_answer):
        if typed_answer.lower() == self.answer.lower():
            return True
        else:
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

player = Person(input("What is your name? "))

conn = database.setup_database()
cursor = conn.cursor()
cursor.execute("SELECT * FROM history")
past_results = cursor.fetchall()

print("Past Results:")
for result in past_results:
    print(f"Name: {result[0]}, Score: {result[1]}")

current_index = 0

def clear_feedback():
    feedback_label.config(text="")

def submit_answer():
    typed_answer = entry.get()
    global current_index
    current_question = questions[current_index]

    if current_question.check_answer(typed_answer):
        player.add_point()
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text=f"Incorrect! The correct answer is: {current_question.answer}", fg="red")
    
    entry.delete(0, tk.END)
    current_index += 1

    if current_index < len(questions):
        label.config(text=questions[current_index].question)
        window.after(1500, clear_feedback)
    else:
        cursor.execute("INSERT INTO history (name, score) VALUES (?, ?)", (player.name, player.score))
        conn.commit()
        feedback_label.config(text=f"Hooray! You've completed the quiz with a score of {player.score}/{len(questions)}", fg="yellow")

window = tk.Tk()
window.title("Quiz Game")

label = tk.Label(window, text=questions[current_index].question)
label.pack()

entry = tk.Entry(window)
entry.pack()

feedback_label = tk.Label(window, text="")
feedback_label.pack()

button = tk.Button(window, text="Submit", command=submit_answer)
button.pack()

window.mainloop()
conn.close()