# Text

In this lab, you'll write  a `Text` class that provides something Python doesn't
have natively: a mutable string type.

This is also a look into how  standard Python types are designed.  The interface
for the `Text` class will be very similar to the interface for Python's built-in
`list` type,  and you'll also implement some  "magic" functions that enable your
`Text` class to work with Python features (like square brackets and `for` loops)
the same way that built-in classes do.


## The Classes

You'll have  a total of  three classes  by the end of the lab.  Implement all of
these in a file named `text.py`.

The most important class is the `Text` class. It holds a sequence of characters,
like a `str`,  but you can modify it.  Implement `Text` as a doubly linked list.
Since Python doesn't have  a character type,  each list node will store a string
of length one.

To do this, you'll need a list node class.  You can call this whatever you like,
but it needs to have member variables named `prev`, `next`, and `char` that hold
the previous node  (or `None`), the next node (or `None`), and the character.

Finally, when you implement iteration, you'll need to add an iterator class.  It
too can be called anything you like;  the only requirement is that it provides a
`__next__()` function as described (far) below.


## Member Functions

The `Text` class should implement the following regular member functions.

- The constructor  takes one optional argument.  If this isn't given, it creates
  an empty `Text` object.  If an argument is given, it must be either a `str` or
  another `Text` object, and the constructor initializes the current text with a
  copy of the argument.
- `append()` takes one argument, which must be a `str` of length one. It appends
  that character to the text.
- `clear()` takes no arguments and removes all characters from the text.
- `copy()` takes no arguments and returns a copy of the current text.
- `extend()`　takes one argument, which must be a `str` or a `Text`. It adds all
  the characters in the argument to the end of the current text.
- `insert()` takes two arguments:  an `int` index and a `str` of length one.  It
  inserts the character at the given index.
- `pop()` takes an optional argument: an `int` index.  If an index is specified,
  it removes and returns  the character at that index; otherwise, it removes and
  returns the last character in the text.

It'll also need some helper functions so the autograder can validate your list
structure:

- `head()` returns the first node in the list, or `None`.
- `tail()` returns the last node in the list, or `None`.


## Python Magic

To interoperate  nicely with  the rest of Python,  the `Text` class  should also
implement some special  member functions.  As with the constructor, the names of
these functions start and end with two underscores.

### Length

The normal way to get  the length of a sequence  in Python  is to use the global
`len()` function on it. To support this, add a member function named `__len__()`
that returns the length of the text.

### To String

You can control how your class  is converted to a `str` by writing a `__str__()`
member function.  This is used by the built-in `print()` function,  for example,
or when you pass your class to the `str()` constructor. The `__str__()` function
should simply return the text as a `str`.

### Item Lookup

The normal way to look up characters in a string (or, more generally, items in a
sequence)  is to use  square  brackets.  To support this,  add a member function
named  `__getitem__()`  that  takes an  `int`  as an  argument  and  returns the
character at that index.

### Item Assignment

Changing  the value  at an  existing  index is  also typically  done with square
brackets.  To support assignment, though, you'll need a separate member function
named `__setitem__()`.  This function takes two arguments:  an `int` and a `str`
(that must be of length one).  It sets the value at the given index to the given
character.

### Concatenation

It's convenient to  concatenate strings with the `+` operator.  To support this,
add two member functions: `__add__()` and `__iadd__()`. The `__add__()` function
implements the `+` operator,  and the `__iadd__()` function  implements the `+=`
operator.  Both functions take one argument,  a `str` or a `Text`,  and add that
text to the current text.  The difference is that `__add__()` creates a new text
to hold the result, while `__iadd__()` modifies the current text in place.

### Substring

The standard way to see if a string contains a substring is to use `in`.  To
support this, add a member function named `__contains__()`. This function should
take one argument: a `str` or a `Text`, and return a `bool` indicating whether
the argument is a substring of the current text.

### Iteration

To work with a Python `for` loop,  a class needs to have a member function named
`__iter__()`.  This function  should return an instance of  an "iterator" class,
which must have a member function named `__next__()`.

An iterator is a helper class that "points" to an item in a sequence. Initially,
it points at the first item.  Calling `__next__()` returns the item the iterator
is currently pointing at,  and updates the iterator to point to the next item in
the sequence.  If there are no more items, it throws a special type of exception
called `StopIteration`.

As a concrete example, this `for` loop:

```py
for thing in things:
    do_stuff_with(thing)
```

Is a much prettier way to write this:

```py
iterator = things.__iter__()
try:
    while True:
        thing = iterator.__next__()
        do_stuff_with(thing)
except StopIteration:
    pass
```

### Slicing

The  normal way to extract  a substring  from a string  (or a subsequence from a
sequence),  is to use a  [slice][slice] inside square brackets.  Square brackets
are implemented  by the `__getitem__()` member function,  so to support slicing,
you'll need to update your `__getitem__()` function. If its argument is a slice,
it should return a new `Text` containing only the characters that were selected.

Working with slices can be tricky,  because any of their  three member variables
might be `None`.  Here are some guidelines on  how to turn a slice into a set of
indices.

- First, determine the direction of the slice. Slices prefer to be forward (with
  a positive `step`), and are only backward if `step` is explicitly negative. If
  `step` is `None`, it defaults to `1`
- If `start` and `stop` are `None`, fill them in with the indices of the ends of
  the sequence.  If they're negative, convert them to positive indices.
- Clamp `start` and `stop` to the ends of the sequence.
- Select indices  `start`, `start + step`, `start + step + step`,  and so on, up
  to, but not including, `stop`.

The resulting `Text` should contain the characters at those indices, in the same
order.  For example:

```
"abcdef"[:]      => "abcdef"
"abcdef"[:3]     => "abc"
"abcdef"[3:]     => "def"
"abcdef"[:-3]    => "abc"
"abcdef"[::2]    => "ace"
"abcdef"[1::2]   => "bdf"
"abcdef"[::-1]   => "fedcba"
"abcdef"[4:1:-1] => "edc"
```


## Edge Cases

Like with `list`s, indices can be negative,  with index `-1` being the last item
in the sequence, `-2` being the second-to-last, and so on. If an index is out of
bounds, raise an `IndexError`.

Most of these functions only accept arguments  of certain types.  If you receive
an argument of the wrong type, raise a `TypeError`.

If you receive  an argument  of the correct type  but that is  otherwise invalid
(like a string of the wrong length), raise a `ValueError`.


## Notes

- There are a lot of functions here, but how many of them are really distinct?
  See how much you can reuse!
- On a similar note, look for common tasks that you can pull out into helper
  functions.
- When raising exceptions, the error messages can be anything you find helpful.
  The autograder will only look at the exception type.
- If you're not sure what a slice should do, try it with a `str`.


[slice]: <https://docs.python.org/3/library/functions.html#slice>
