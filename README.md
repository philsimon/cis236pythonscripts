# CIS 236 Python Scripts

Python scripts written for a CIS 236 course. The scripts cover core beginner topics: conditionals, loops, error handling, and simple input/output. Several scripts pair a broken version with a fixed version to illustrate common Python errors.

## Requirements

- Python 3.

## Usage

Run any script directly:

```bash
python3 loops.py
```

Scripts that prompt for input display instructions in the terminal.

## Scripts

### Conditionals

| Script | Description |
|---|---|
| `ifthen.py` | Charges a luggage fee if the input weight exceeds 50 pounds. |
| `ifthen_else.py` | Variant of `ifthen.py` with a different message. |
| `ifthen_else2.py` | Checks whether an input last name reaches 12 characters. |
| `elif_example_work.py` | Prints a different message for each day of the week using `elif`. |

### Loops

| Script | Description |
|---|---|
| `loops.py` | Four loop examples: summing a list, printing a range, iterating over a list, and summing a range. |
| `loop2.py` | Sums a list of numbers with a `for` loop. |
| `loop3.py` | Sums a list that includes negative numbers. |
| `loop4.py` | Sums the integers between 1 and an input value, `n`. |
| `loop_beersong.py` | Prints the "99 Bottles of Beer" lyrics, starting from 5. |
| `loop_for_simpl1.py` | Prints each name in a list of Rush band members. |
| `loop_for_simpl2_diehard.py` | Prints a list of *Die Hard* characters, with a second version that stops at a matching name using `break`. |
| `while.py` | A number-guessing game that loops until the player guesses correctly. |
| `while2.py` | Counts from 0 to 18 with a `while` loop. |
| `say_my_name.py` | A *Breaking Bad*-themed guessing game that counts attempts with a `while` loop. |

### Errors

Each pair below shows a broken script and its corrected version.

| Broken | Fixed | Bug |
|---|---|---|
| `album_picker_error.py` | `album_picker_fixed.py` | `random.randint` includes the list length as a valid index, causing an out-of-range error; the fix subtracts 1 from each bound. |
| `say_my_name_error.py` | `say_my_name.py` | Uses assignment (`=`) instead of comparison (`==`) in an `if` statement. |

Standalone error examples:

| Script | Error type |
|---|---|
| `error_logic.py` | Logic error: the comparison message contradicts the actual condition. |
| `error_runtime.py` | Runtime error: a missing closing parenthesis. |
| `error_runtime2.py` | Runtime error: references an undefined variable. |
| `error_runtime3.py` | Runtime error: accesses a list index beyond its bounds. |

### Simple Input and Output

| Script | Description |
|---|---|
| `simple_prompt.py` | Prompts for text and prints it back. |
| `simple_calcs.py` | Demonstrates arithmetic operators: addition, subtraction, multiplication, division, modulo, floor division, and exponentiation. |
| `simple_avg.py` | Averages three input numbers and flags whether the average exceeds 12. |
| `simple_avg_threshhold.py` | Averages three input numbers and compares the result against an input threshold. |
| `random.py` | Prints a random integer between 1 and 2112. |

## License

GNU General Public License v3.0. See `LICENSE`.
