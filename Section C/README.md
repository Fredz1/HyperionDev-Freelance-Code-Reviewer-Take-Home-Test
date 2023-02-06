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
git clone https://github.com/<username>/say-number.git
```
<!-- The text you want to ignore -->
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

## Built With

Python - The programming language used

## Versioning

I use SemVer for versioning.

## Authors

Frederick Williams

## License

This project is licensed under the MIT License.

## Acknowledgments

I would like to thank me.