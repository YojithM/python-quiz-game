# Python Quiz Game

A desktop quiz app built with Python and Tkinter that adapts to how well you know
the material. Questions you get wrong keep coming back until you've mastered
them, and your scores are saved between sessions.

Built as a project to showcase my Python progression from the ground up: starting from basic
syntax and working up through object-oriented design, persistent storage, GUI
programming, and spaced-repetition logic.

## Features

- **Interactive GUI** — built with Tkinter, no terminal required
- **Spaced repetition** — questions you miss are automatically re-asked until
  you get them right, instead of just moving on
- **Persistent history** — scores are saved to a local SQLite database and
  shown at the start of each session, so you can track improvement over time
- **Content loaded from JSON** — questions live in `questions.json`, so the
  quiz content can be swapped out (currently: core Python/CS concepts) without
  touching any code

## How it works

- `main.py` — the game itself: `Question` and `Person` classes, the Tkinter
  GUI, and the game loop logic (scoring, review rounds, timed feedback)
- `database.py` — handles all SQLite setup and connections, kept separate from
  the game logic
- `questions.json` — the question bank; edit this file to quiz yourself on
  anything else

## Running it

**Requirements:** Python 3.10+ with Tkinter support (on some systems you may
need to install it separately, e.g. `brew install python-tk` on macOS with
Homebrew).

```bash
python3 main.py
```

Enter your name when prompted in the terminal, then the quiz window will open.
Answer each question in the text box and hit Submit — you'll see live
feedback, and any missed questions will resurface for review before the quiz
ends.

## What's next

- Multiple-choice support (the JSON format already has room for it)
- More content packs
- Difficulty levels / timed rounds