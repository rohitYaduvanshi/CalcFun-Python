# CalcFun - Python Calculator

A simple command-line calculator built with Python. This was one of my early Python projects where I learned how to use dictionaries to map operations to functions, handle user input in a loop, and display a fun ASCII art logo on startup.

---

## What it does

You enter two numbers and pick an operation (+, -, *, /). It shows the result, and then asks if you want to keep going with that result or start fresh. Pretty basic but it taught me a lot about how Python functions and dictionaries work together.

---

## Files

- `main.py` — all the calculator logic lives here
- `ascii_art.py` — just holds the big logo that prints at the top

---

## How to run

Make sure Python is installed, then just:

```bash
python main.py
```

No external libraries needed. Pure Python.

---

## How the code works

There are four functions — `add`, `subtract`, `multiply`, `divide` — each doing exactly what the name says. They're stored in a dictionary called `operations`:

```python
operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}
```

So when you pick `+`, it calls `operations["+"](num1, num2)` which runs the `add` function. This way I didn't need a bunch of if-else conditions.

The `calculator()` function runs a `while` loop. If you type `y`, the answer becomes the new first number and the loop continues. If you type `n`, it clears the screen and calls `calculator()` again to restart.

---

## Dry Run Example

Say you want to calculate `15 + 5`, then multiply that by `2`.

```
Program starts → ASCII logo prints

Prompt: What is the first number?
Input:  15

Available operations: + - * /
Prompt: Pick an operation
Input:  +

Prompt: What is the second number?
Input:  5

Output: 15.0 + 5.0 = 20.0

Prompt: Continue with 20.0? (y/n)
Input:  y  →  num1 is now 20.0

Pick an operation: *
Second number: 2

Output: 20.0 * 2.0 = 40.0

Prompt: Continue? (y/n)
Input:  n  →  screen clears, calculator restarts
```

---

## Flowchart

```
START
  |
  v
Print ASCII logo
  |
  v
Input: first number (num1)
  |
  v
[ LOOP STARTS ]
  |
  v
Show available operations
  |
  v
Input: operation symbol
  |
  v
Input: second number (num2)
  |
  v
Calculate: answer = operations[symbol](num1, num2)
  |
  v
Print result
  |
  v
Continue? (y/n)
  |
  +-- y --> num1 = answer --> back to top of loop
  |
  +-- n --> clear screen --> restart calculator()
```

---

## Bug fixes

These were fixed after the first version:

- `substract` typo corrected to `subtract`
- `divide()` now has a `try/except` block — dividing by zero prints an error message instead of crashing
- The continue prompt was missing an `f` prefix, so `{answer}` was printing literally. Fixed to `f"Type 'y' to continue calculating with {answer}..."`

## Still to fix

- If you type an invalid operation like `%` it throws a `KeyError` — no validation yet
- Calling `calculator()` recursively on restart could cause a stack overflow if someone restarts many times — better to use a loop

---

## What I learned from this

- Using dictionaries to store functions (higher-order functions concept)
- `while` loops with a flag variable
- Taking and converting user input with `float(input(...))`
- Importing from another file (`ascii_art.py`)
- Recursive function calls (and their limitations)
