# 🎯 Number Guessing Game

A simple Python terminal-based game where the user tries to guess a randomly generated number between 1 and 100.

---

## 🧠 What I Learned
- `random.randint()` for number generation
- `input()` for user interaction
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`)
- Counters and loop control

---

## 📌 How It Works

- The program generates a random number between 1 and 100.
- The user keeps guessing until they get the correct number.
- After each guess, the program provides feedback:
  - "Too High!" if the guess is higher than the target
  - "Too Low!" if the guess is lower than the target
  - On correct guess, shows the number of attempts

---

## 🧪 Sample Output
```
--------------- NUMBER GUESSING GAME ---------------
Enter a guess: 50
Too High!!
Enter a guess: 20
Too Low!!
Enter a guess: 35
Yay!, Your guess is correct number in 3 attempts.
```

---

## 🚀 Run This Program

```bash
python main.py
```

## Screenshot

![screenshot of terminal](https://github.com/user-attachments/assets/c13e3f0f-0355-4bf7-a28f-2dd6fda66460)


✅ Status
- ✔️ Project Complete

📝 Can be improved later with:

- Input validation

- Difficulty levels

- Limited attempts

- Restart option
