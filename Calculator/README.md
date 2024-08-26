# Simple Calculator Using Streamlit

A simple, interactive calculator built using Streamlit. This calculator supports basic arithmetic operations and provides a user-friendly interface to perform calculations.


## Features
- Basic Arithmetic Operations: Addition, subtraction, multiplication, and division.
- User-Friendly Interface: Simple and clean design with large buttons for ease of use.
- Error Handling: Displays "Error" if the expression is invalid.

## Demo

![Calculator home page](https://github.com/user-attachments/assets/936de9b1-bbe0-4294-9b70-8a820d735d97)
You can see a live demo of the app [here](https://qrcode-generat0r.streamlit.app/) (replace with your deployment link).

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple-calculator.git
   cd simple-calculator
   ```
2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv env
   env\Scripts\activate
   ```
3. Install the required packages:

4. Run the streanlit app:
   ```
   streamlit run app.py
   ```

## How It Works
### UI Elements:

The display area shows the current expression or result.
Buttons are used to input numbers and operations. Special symbols for division, multiplication, subtraction, and addition are used for better readability.

### Expression Evaluation:

HTML Entities: Buttons use HTML entities (&divide;, &times;, &minus;, &plus;) for symbols.
Evaluation Function: The expression is evaluated after converting HTML entities back to mathematical operators.

### Button Click Handling:

Updates the current expression based on the button clicked.
Handles special buttons for clearing the display and deleting the last character.

## Example
Here’s a quick example of how to use the calculator:

Click 7, +, 8, = to get the result of 7 + 8.
Click 5, ×, 6, = to get the result of 5 × 6.
Use the ← button to remove the last character of the current expression.
Use the C button to clear the display.
