# Random Number Guessing Game
Welcome to the Random Number Guessing Game! This simple game challenges you to guess a number that the computer has randomly selected between 1 and 100. Can you guess it correctly?

## Features
- Interactive Gameplay: The computer selects a random number between 1 and 100, and you need to guess it.
- Feedback System: Receive helpful hints based on your guess:
  🌡️ Way too low/high: If you're significantly off from the target number.
  ⬆️ Too low/high: If you're close but need to adjust your guess.
  🔼 Slightly low/high: If you're very close to the target number.
- Reset Option: Start a new game at any time with the reset button.
- Attempt Counter: Keep track of how many guesses it takes you to find the correct number.

## Demo
You can see a live demo of the app [here].
![Home page](https://github.com/user-attachments/assets/eb91d8a8-4874-4139-9583-be1f8707f267)

## How to Run
1. Clone the Repository:
```
git clone https://github.com/your-username/random-number-guessing-game.git
cd random-number-guessing-game
```
2. Set Up Your Environment: It's recommended to use a virtual environment. You can create and activate one using:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install Dependencies:
```
pip install -r requirements.txt
```
4. Run the App:
```
streamlit run app.py
```
This command will open a new browser window with the game interface.
