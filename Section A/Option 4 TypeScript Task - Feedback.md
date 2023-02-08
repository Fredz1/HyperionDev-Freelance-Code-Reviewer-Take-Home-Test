# Section A

## Option 4 : TypeScript Task - Feedback

### Correctness

1. The code implements the Caesar Cipher correctly by shifting the alphabet to the right by the specified shift value, taking care of wrap-around which is well handled.
1. In TypeScript, you can't use angle brackets ``<T>`` to declare a type parameter. It is used to declare a type parameter in Java. Instead, type parameters are added to the function name, separated by angle brackets.
1. The second parameter passed to the function should be of type ``number``.
1. The variale ``Alphabet`` on line 1 was already been declared in the current scope. To fix this, you can rename the second instance of the identifier on line 7 to another name i.e. , for example: ``const alphabet: AlphabetType = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';``
1. The print statement on teh final line does not exist in TypeScript or JavaScript. Instead you should use the ```console.log()``` function.
1. The names for your variables are discriptive and easy to understand. Try to use one type of naming convention when naming variables. The function name is in snakeCase but the other variables are in camelCase.

### Efficiency

1. The code uses an iterative approach to shift each character of the input string.
1. The alphabet.indexOf method is used to find the index of each character in the alphabet. This is a linear search operation, so its time complexity is O(n), where n is the length of the alphabet. This could be improved to O(1) time complexity using an object to map each character to its index.

### Style

1. The code uses meaningful and descriptive variable names.
1. The code is indented correctly and uses appropriate whitespaces.
1. The code uses comments to explain important steps, which is good for readability.
1. The closing curly braces in your 1st ``if`` statement should be on a new line.  You can use an auto-formatting plugin to correct this when you save your code.

### Documentation

1. The code could use more documentation to explain the implementation details and the reasoning behind certain choices, such as the modulo operation to reduce the shift value if it's greater than 26.

### Improvements

1. Consider using an object to map each character to its index for improved time complexity.
1. Add more documentation to explain the implementation details and reasoning behind certain choices.
1. VScode will warn you of any faults with  your code.  Pay special attention to them as it can help you correct a mistake before you save or compile your code.
