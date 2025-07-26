
# 🗺️ U.S. States Game

A fun and educational geography quiz game built using Python and Turtle graphics. The goal is to correctly name all 50 U.S. states. Each correct guess is displayed on a map.

---

## 🎯 How It Works

- You are shown a blank map of the United States.
- Enter the name of a U.S. state in the input dialog.
- If correct, the state's name appears on the map at its appropriate location.
- The game ends when you guess all 50 states or type **"Exit"**.
- At the end, a `states_to_learn.csv` file is generated with any states you missed.

---

## 📂 Features

- Interactive turtle graphics with a map as background  
- Text input prompts for guessing states  
- Automatically displays guessed states on the map  
- Creates a `.csv` file of missed states for study  

---

## 🛠️ Tech Stack

- Python 3.x  
- Turtle (for graphics)  
- Pandas (for data handling)

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed.  
Download: https://www.python.org/downloads/

Install required libraries:

```bash
pip install pandas
```

### Required Files

- `main.py` (your script)
- `50_states.csv` — CSV file with columns: `state`, `x`, `y`
- `blank_states_img.gif` — Image of the U.S. map used as background

### Run the Game

```bash
python main.py
```

---

## 📦 CSV File Format (`50_states.csv`)

Ensure your CSV file looks like this:

| state     | x   | y   |
|-----------|-----|-----|
| Alabama   | 139 | -77 |
| Alaska    | -230| -210|
| ...       | ... | ... |

---

## 💾 Output

When you type **"Exit"**, a file named `states_to_learn.csv` is generated containing any states you didn’t guess.

---

## 📌 Tips

- Capitalization doesn't matter — inputs are automatically title-cased.
- You can exit anytime by typing `"Exit"` in the input box.
- Use the generated CSV file to study the states you missed.

---

## 📄 License

This project is open source and free to use for learning purposes.
