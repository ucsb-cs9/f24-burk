# List

In this lab, you'll write a classic container class: a linked list.

This particular linked list stores its items in sorted order.  The first item in
the list  is less than  or equal to  all the other items,  and the  last item is
greater than or equal to all the other items.  The user doesn't get (or need) to
specify an index  when adding items to the list;  the list class should  put the
new item in the correct place automatically.

Since Python is a dynamically typed language,  the list can store any value that
supports the standard comparison operators (`<`, `==`, etc.).  The user (and the
autograder)  will always use a single type of value  per list, so you won't have
to compare two values of different types.


## Required Classes

All of the required code for this lab goes in a file called `linkedlist.py`.  In
this file, you'll write two classes.

The `ListNode` class represents a single node in a linked list.  A list node has
two publicly accessible member variables: `value`, the data stored at that node,
and `next`, which is either the next node in the list, or `None`, if the current
node is the last node in the list.  It has one required function:

- The constructor takes one or two arguments. The first is the value to store at
  that node;  this is required.  The second is the next node,  which is optional
  and defaults to `None.`

The `LinkedList` class stores a sorted sequence of items, or values. Internally,
it uses the  `ListNode` class:  each list node stores one value  and a reference
to the next node in the list.  The `LinkedList`  only needs to store a reference
to the first node in the list, and to provide member functions for  manipulating
the list:

- The constructor takes no arguments and creates an empty list.
- `add(value)` inserts `value` at its correct position in the list.
- `count()` returns the number of values in the list.
- `get(index)`  returns the value  stored at `index`.  If `index` is invalid, it
  raises an `IndexError`.
- `head()`  returns the first `ListNode`  in the list,  or `None` if the list is
  empty.
- `print(reverse)`  prints the values stored in the list,  separated with commas
  and spaces and enclosed in square brackets,  with a newline after  the closing
  bracket.  If `reverse` is  `False`  (or not specified),  it prints the list in
  it's natural (ascending) order:
  ```
  [Aramis, Athos, Porthos]
  ```
  If `reverse` is `True`, it prints the list in descending order:
  ```
  [Porthos, Athos, Aramis]
  ```
- `remove(index)` removes the value stored at `index` and returns that value. If
  `index` is invalid, it raises an `IndexError`.
- `remove_all(value)`  removes all copies of `value` from the list.   It returns
  the number of values that were removed.

Your linked list should support  negative indices like Python `list`s do:  index
-1 refers to the  last item in the list,  index -2 refers to the  second-to-last
item,  and so on.  A list with three items has  three valid non-negative indices
(0, 1, and 2) and three valid negative indices (-1, -2, and -3).


## Exceptions

Sometimes the user will ask your code to do things that it can't do.  You need a
way to report that your code  wasn't able to complete the request.  Fortunately,
Python has an easy way to do this: you can report errors by raising exceptions.

To raise an exception,  use its constructor to create the exception object (most
exception constructors take an error message  as an argument),  then use `raise`
to activate Python's exception system.

```py
raise SomeExceptionType('Your error message here!')
```

Use useful error messages!  This will make debugging your code much easier.  The
autograder will always print a standard message when it sees an `IndexError`, so
you can use any messages you find helpful.

If the program doesn't have any code to handle exceptions,  raising an exception
will  crash the program.   This is a good thing!   It makes sure that you notice
errors as soon as they occur, instead of later on when the original cause of the
error would be much harder to determine.

It's possible to  "catch"  and handle exceptions  so that they don't  crash your
program  (see  `try` and `except`  if you're curious),  but you won't need to do
that for this lab.  We'll talk about that later.


## Hints

- Recursion works very nicely on linked lists.
- An empty list should print as empty square brackets: `[]`.
- Work on the `add()` `print()` (forward), and `head()` functions first.  You'll
  need `add()` and `print()` to test your code locally,  and the autograder will
  use `add()` and `head()` in almost all of the test cases.
- If you want to add test code,  do it in an `if __name__ == '__main__` block in
  `linkedlist.py`  so it doesn't run when the autograder imports your list code.
  Or write a separate test file that imports your list.
- The `head()`  function  is something you  wouldn't find  on a normal container
  class.  The `ListNode` class  is an  "implementation detail",  and wouldn't be
  exposed to the user.  But in this case, the autograder needs it to verify your
  list structure and provide a fallback print function.
