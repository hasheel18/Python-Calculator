# Python Calculator 🧮

A simple command-line calculator built with Python. It supports basic arithmetic operations as well as power and remainder calculations.

## Features ✨

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Power (`^`)
- Remainder (`%`)
- Input validation for numbers
- Handles division by zero
- Reset and terminate options

## Tech Stack 💻

- Python 3

## How It Works ⚙️

- The program shows a menu of available operations.
- Users select an operation by entering the corresponding symbol.
- The calculator prompts for two numbers.
- It performs the chosen calculation and displays the result.
- Users can reset the calculator or terminate the program at any time.

## Project Structure 📁

```bash
python-calculator/
│
├── calculator.py
└── README.md
```

## Usage 🚀

Run the program using:

```bash
python calculator.py
```

Then follow the on-screen menu to choose an operation and enter numbers.

## Example 🧠

```text
Select operation.
1.Add      : +
2.Subtract : -
3.Multiply : *
4.Divide   : /
5.Power    : ^
6.Remainder: %
7.Terminate: #
8.Reset    : $

Enter choice(+,-,*,/,^,%,#,$): +
Enter first number: 10
Enter second number: 5
10.0 + 5.0 = 15.0
```

## Notes 📝

- Division by zero is not allowed.
- Enter `#` to terminate the program.
- Enter `$` to reset the calculator.
