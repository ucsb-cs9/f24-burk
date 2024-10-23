# Calculate

In this lab, you'll use stacks and queues to implement a simple calculator.

Parsing standard (infix) mathematical notation can be difficult,  so you'll work
with two other notations instead: prefix and postfix. These are a lot easier for
computers  (and programmers) to deal with, and a lot of the earliest calculators
used postfix notation as an input format.  Some people even prefer this, and you
can still find calculators that support it today.

Your calculator will operate in two steps.  The first step is to take user input
(a big string)  and break  it into  meaningful pieces:  these pieces  are called
tokens,  and this process is called tokenization.  The second step is to perform
the operations described by the tokens and determine the result.  This is called
evaluation.

During evaluation,  it's useful to treat the input as a queue of tokens.  You'll
use Python's built-in [deque][deque] type (short for double-ended queue) as your
token queue; import `deque` from the `collections` module to access it. To use a
`deque` like a regular queue, call `append()` to push and `popleft()` to pop.


## The Library

First,  create  a file  named  `calculate.py`.  In this file,  you'll  write the
functions that perform the individual  steps needed to evaluate a string of user
input.  You'll combine these functions into a program later.


### Tokenization

The first step is to chop a string of input into individual tokens.  Since we're
writing a calculator,  there are  two types of  token we care about: numbers and
operators.  In the input, each number will appear as:

- Optionally, a sign (`+` or `-`).
- One or more decimal digits.
- Optionally, a decimal point (`.`) followed by one or more decimal digits.

And each operator will be one of the following:

- `+` adds its two operands.
- `-` subtracts its right operand from its left operand.
- `*` multiplies its two operands.
- `/` divides its left operand by its right operand.
- `%` gives the remainder after dividing its left operand by its right operand.
- `^` raises its left operand to the power of its right operand.
- `~` takes one operand and negates it.

In `calculate.py`,  write a `tokenize()` function that  takes a single string as
an  argument.  This  string  will  contain  zero  or more  tokens,  separated by
whitespace (spaces, tabs, newlines, etc.), and possibly with  more whitespace on
either end.  Return a `deque`  containing these tokens  in their original order;
store numbers as `float`s, and operators as `str`s.

If you encounter  a token  that is  neither  a number nor  an operator,  raise a
`RuntimeError` with the message `Invalid token: "XXX"`  (where `XXX` is the text
of the invalid token).


### Evaluation

The final step is to evaluate  the expressions described by the tokens.  Add two
evaluation functions to `calculate.py`:  `prefix()` and `postfix()`.  These will
evaluate expressions  in prefix and postfix notations,  respectively.  See below
for details on these formats.

Both of these functions should take one argument: a `deque` of tokens containing
the  expression to be  evaluated.  Each  function  should return a `float`:  the
result of evaluating the input expression.


### Prefix Notation

[Prefix notation][prefix] (also known as Polish notation)  is a different way to
write  mathematical expressions.  Instead of putting the operators between their
operands like in normal (infix) notation,  prefix notation puts the operators in
front:

| Infix Notation             | Prefix Notation         |
|:---------------------------|:------------------------|
| `42`                       | `42`                    |
| `-13`                      | `-13`                   |
| `1 + 2`                    | `+ 1 2`                 |
| `3 * 4 + 5`                | `+ * 3 4 5`             |
| `6 - 7 / 8`                | `- 6 / 7 8`             |
| `9 * (10 + 11)`            | `* 9 + 10 11`           |
| `(10 - 3) ^ -(17 % 4) + 1` | `+ ^ - 10 3 ~ % 17 4 1` |

This  might look unfamiliar,  but it's actually a lot simpler to work with.  You
don't need to worry about order of operations  any more,  and parentheses are no
longer necessary.

You can evaluate prefix notation recursively. If you see a number, simply return
that value.  If you see an operator, recursively evaluate its operands,  perform
the operation, and return the result.  The value of the entire expression is the
result of evaluating its first token.


### Postfix Notation

[Postfix notation][postfix]  (also known as  reverse Polish notation)  is  a lot
like prefix notation, but the operators come after their operands:

| Infix Notation             | Postfix Notation        |
|:---------------------------|:------------------------|
| `42`                       | `42`                    |
| `1 + 2`                    | `1 2 +`                 |
| `3 * 4 + 5`                | `3 4 * 5 +`             |
| `6 - 7 / 8`                | `6 7 8 / -`             |
| `9 * (10 + 11)`            | `9 10 11 + *`           |
| `(10 - 3) ^ -(17 % 4) + 1` | `10 3 - 17 4 % ~ ^ 1 +` |

You can evaluate  postfix notation using a stack.  If you see a number,  push it
onto  the stack.  If you see  an operator,  pop  its operands  off of the stack,
perform the operation,  and push the result onto the stack.  If everything  goes
well, there should be exactly one value on the stack when you finish reading the
input; this is the final result.


### Edge Cases

The only error that can happen  during tokenization  is the unknown token error,
as described above.  But there are several things that can go wrong while you're
evaluating  the inputs.  If you encounter  any of these,  raise a `RuntimeError`
with the appropriate error message:

- If the deque is initially empty, say `No input.`
- If there aren't enough operands for an operator, say `Not enough operands.`
- If there are extra tokens in the deque passed to `prefix()`, say `Too much input.`
- If there are multiple values left on the stack in `postfix()`, say `Too many operands.`
- If you try to divide by (or take the remainder after dividing by) zero, say `Division by zero.`


## The Program

In `main.py`, write a program that acts as an interactive calculator.  It should
take zero or one command line arguments. If there are no command line arguments,
it should run in  prefix mode;  if the only  command line argument is the string
`-r`, it should run in postfix mode.  In any other case, it should print a usage
message and exit immediately:

```
[ljs@hispaniola]$ python3 main.py -arrrrrrrr
USAGE: main.py [-r]
```

If given  valid command line arguments,  the program should  read its user input
one line at a time. It should tokenize each line, pass the tokens to the correct
evaluation function, and print the result prefixed with the string `"= "`.  When
it reaches the end of its input, it should exit.  For example, in prefix mode:

```
[ljs@hispaniola]$ python3 main.py
42
= 42.0
* + 1 2 3
= 9.0
```

And in postfix mode:

```
[ljs@hispaniola]$ python3 main.py -r
42
= 42.0
1 2 - 3 /
= -0.3333333333333333
4 1 ~ ^
= 0.25
```

If you see an empty line or a line containing entirely whitespace, ignore it and
move on to the next line.  If an exception gets raised while you're processing a
line, print the error message and move on to the next line of input.

```
[ljs@hispaniola]$ python3 main.py -r

1 0 /
Division by zero.
1 2 ~
Too many operands.
```


### Handling Exceptions

The functions  in `calculate.py`  will raise exceptions if anything  goes wrong,
but you don't want these exceptions  to crash your program.  Fortunately, Python
provides a way to "catch" exceptions and handle them manually.

You can do this with a  `try`/`except`  block.  Put the code that might raise an
exception in the `try` section,  and put the error handling code in the `except`
block.

```py
try:
    # Code that might raise SomeExceptionType...
except SomeExceptionType as error:
    print(error)
```

This will catch any  `SomeExceptionType` that gets raised inside the `try` block,
even  if it happens inside a  function call  (even several levels deep).  If you
need to catch  multiple  types of exceptions,  you can attach  multiple `except`
blocks to  one `try` block.  If you want to raise a different type of exception,
you can `raise` a new exception from an `except` block.


## Hints

- The functions  listed above  are the only required functions,  but it might be
  helpful to define a few additional helper functions.
- The `float()` constructor accepts more formats than the (rather strict) number
  format described above.  You can accept these or not; they won't be tested.
- When evaluating binary (two-operand) operators in postfix notation,  the first
  operand you pop off the stack will be the right hand operand.
- When printing a `float` in `main.py`,  the `str()` constructor will give you a
  string in the correct format.  Or you can `print()` the number directly.
- Passing a string that isn't a number to the `float()` constructor will raise a
  `ValueError` by default;  trying to `pop()` or `popleft()` from an empty deque
  will raise an `IndexError`.
- Python has a standard `queue` module,  but it's kinda complicated  (it's meant
  for multi-threading).  That's why we're using deques instead.
- <https://xkcd.com/645/>


[deque]: <https://docs.python.org/3/library/collections.html#collections.deque>
[prefix]: <https://en.wikipedia.org/wiki/Polish_notation>
[postfix]: <https://en.wikipedia.org/wiki/Reverse_Polish_notation>
