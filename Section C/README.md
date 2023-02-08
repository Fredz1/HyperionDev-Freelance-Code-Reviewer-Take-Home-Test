# Say Number

This repository contains a Python function that takes a numeral (just digits without separators (e.g. 19093 instead of 19,093) and returns the standard way of reading a number, complete with punctuation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Python 3.5 or higher
1. virtualenv (optional)

### Installing

1. Clone the repository

```bash
git clone https://github.com/Fredz1/HyperionDev-Freelance-Code-Reviewer-Take-Home-Test.git
```

2. Change into the project directory

```bash
cd say-number
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment (on Linux/macOS)

```bash
source venv/bin/activate
```

Activate the virtual environment (on Windows)

```bash
venv\Scripts\activate
```

5. Install the required packages

```bash
pip install -r requirements.txt
```

6. Run the tests:

```bash
python test_say_number.py
```

7. If all tests pass, the solution is ready to use. To use the say_number function, run the following code in the Python interpreter

```bash
$ python
>>> from say_number import say_number
>>> say_number(123456789)
"One Hundred and Twenty Three Million, Four Hundred and Fifty Six Thousand, Seven Hundred and Eighty Nine."
```

## Space complexity justification

The worst-case space complexity of this function is O(n), where n is the number of digits in the input number. This is because the function creates several lists to store intermediate results, such as the list of groups, the list of words, and the final result. The size of these lists will depend on the number of digits in the input number. For example, if the input number has m digits, the list of groups will have m/3 elements (rounded up), the list of words will have at most 3m/3 elements (i.e., m elements), and the final result will have at most 3m/3 + m/3 elements (i.e., 4m/3 elements). Since the size of these lists is proportional to the number of digits in the input number, the space complexity is O(n).

## Built With

Python - The programming language used

## Versioning

I use SemVer for versioning.

## Authors

Frederick Williams

## License

This project is licensed under the MIT License.
