"""
Phase 1: Core Game Loop
------------------------
A terminal-based quiz game. Loads questions from questions.json,
asks them one at a time, and tracks your score.

This phase is all about re-learning basic Python: variables, loops,
functions, lists, dicts, and reading/writing files.

Run it with:  python main.py
"""

import json
import random


def load_questions(filepath):
    """Read the questions.json file and return it as a Python list of dicts."""
    with open(filepath, "r") as f:
        questions = json.load(f)
    return questions


def ask_question(question_data):
    """
    Show one question with lettered options, get the player's answer,
    and return True if they got it right, False if wrong.
    """
    print("\n" + question_data["question"])

    options = question_data["options"]
    letters = ["A", "B", "C", "D"]

    # Print each option next to its letter, e.g. "A) def"
    for letter, option in zip(letters, options):
        print(f"  {letter}) {option}")

    # Keep asking until we get a valid letter
    while True:
        guess = input("Your answer (A/B/C/D): ").strip().upper()
        if guess in letters:
            break
        print("Please type A, B, C, or D.")

    # Turn the chosen letter back into the actual answer text
    chosen_index = letters.index(guess)
    chosen_answer = options[chosen_index]

    is_correct = chosen_answer == question_data["answer"]

    if is_correct:
        print("Correct! ✅")
    else:
        print(f"Nope — the correct answer was: {question_data['answer']}")

    return is_correct


def run_game():
    """The main game loop."""
    questions = load_questions("questions.json")
    random.shuffle(questions)  # mix up the order each run

    score = 0
    streak = 0
    best_streak = 0

    print("=" * 40)
    print("  PYTHON QUIZ GAME — Phase 1")
    print("=" * 40)
    print(f"You'll be asked {len(questions)} questions. Good luck!\n")

    for question_data in questions:
        correct = ask_question(question_data)

        if correct:
            score += 1
            streak += 1
            best_streak = max(best_streak, streak)
        else:
            streak = 0  # reset streak on a wrong answer

    # Final results
    print("\n" + "=" * 40)
    print("  GAME OVER")
    print("=" * 40)
    print(f"Final score: {score} / {len(questions)}")
    print(f"Best streak: {best_streak} 🔥")

    percentage = (score / len(questions)) * 100
    print(f"Accuracy: {percentage:.0f}%")


if __name__ == "__main__":
    run_game()
