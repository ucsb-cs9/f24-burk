# Menu

This project will get you used to working with Python `class`es.  You'll write a
program that lets a user  order things off of a menu;  the main "objects" you're
working with, menus and orders, will be represented by the Python classes `Menu`
and `Order`.

This project has three parts, each one building off the previous parts:

- The `Menu` class and its helper class, `MenuItem`.
- The `Order` class and its helper class, `OrderItem`.
- A program that ties it all together.

You can (and should!) work on this program in stages. A soon as you're done with
your menu code, you can make sure it works on Gradescope by uploading `menu.py`.
You can verify your order code early by uploading both `menu.py` and `order.py`.
Finally, to test your entire program, upload all three files to Gradescope.


## The Menu

First, we'll need to be able to represent a menu.  Create the file `menu.py` and
write the following classes in that file.

The `MenuItem` class is a simple class that represents  a single item on a menu.
It has two attributes: `name` (a `str`) and `price` (a `float`).  The `MenuItem`
constructor takes those two arguments (`name` and `price`) in that order.

The `Menu` class stores a list of `MenuItem`s,  and has some member functions to
make working with menus easier:

- `__init__()` takes no arguments, and creates an empty menu.
- `add(name, price)`  takes two arguments:  a name and a price.  If an item with
  that name is not already present in the menu, it adds a new `MenuItem` for the
  new item to the end of the menu.  If an item with that name already exists, it
  updates the item's price.
- `find(name)` takes one argument: a name.  It tries to find a `MenuItem` in the
  menu with that name.  If it exists, it returns that `MenuItem`.  Otherwise, it
  returns `None`.
- `print()` takes no arguments, and prints the menu as shown below.

```
TODAY'S MENU:
  Burger                       $5.50
  Double Burger                $6.75
  Cheeseburger                 $8.00
  Double Cheeseburger         $10.00
  Fountain Drink               $3.10
```

The first line has a newline immediately after the colon. Then, for each item on
the menu (in the order it was added), it prints:

- Two spaces.
- Twenty-four characters for the item name, aligned left.
- Two spaces.
- Eight characters for the price, aligned right.
- A newline.


## The Order

The next step is to be able to represent what a user orders off of a menu.  Make
a file called `order.py`, and in this file, write the following classes.  You'll
want to `import menu` at the top of this file so you can access the menu classes
you wrote in the first step.

The `OrderItem` class is  similar to the `MenuItem` class.  It's a simple helper
class for  storing information about  part of an order.  It has  two attributes:
`menuitem` (a `MenuItem`) and `quantity` (an `int`). Its constructor takes those
two arguments in that order; if `quantity` isn't specified, it defaults to one.

The `Order` class  stores a list of `OrderItem`s, and, like a `Menu`, has member
functions that handle common `Order` operations:

- `__init__()` takes no arguments, and creates an empty order.
- `add(menuitem, quantity)`  takes one or two arguments:  a `MenuItem` and maybe
  an `int`.  If the order doesn't contain any of  that menu item yet,  it adds a
  new `OrderItem`  to the end of the order.  If the order does contain that menu
  item,  it adjusts the  existing quantity.  If `quantity`  isn't specified,  it
  defaults to one.
- `total_price()` takes no arguments, and returns the total price of the order.
- `total_quantity()` takes no arguments, and returns the number of menu items in
  the order (an order item with a quantity of two counts as two menu items).
- `print()` takes no arguments, and prints the order as shown below.

```
YOUR ORDER:                 Qty     Price     Total
  Cheeseburger               17     $8.00   $136.00
  Fountain Drink              1     $3.10     $3.10
TOTAL                                       $139.10
```

For each order item in the order, it prints:

- Two spaces.
- Twenty four characters for the name, aligned left.
- Two spaces.
- Three characters for the quantity, aligned right.
- Two spaces.
- Eight characters for the price, aligned right.
- Two spaces.
- Eight characters for the line total, aligned right.
- A newline.


## The Program

Now that you have your menu and order types,  you can use them to make a program
that lets people order off a menu.  Write it in a file called `main.py`.

Your program should take exactly one command line argument. This argument is the
path to a TSV file (the format is described below).  When the program starts, it
should load the menu  described in this file,  print it (followed by a newline),
and then ask the user to order:

```
[dent@bistromath]$ python3 main.py data/cheese.tsv
TODAY'S MENU:
  Cheese                      $50.00

What would you like to order?

```

It should then wait for the user  to enter an order.  This will be any number of
lines of user input; each line will be the name of one menu item. Each line adds
one menu item  to the user's order.  A user who wants a  higher quantity of some
item will have to enter its name multiple times.

When your program reaches the end of its user input,  it should print a newline,
then print the user's order, then exit.

```
[dent@bistromath]$ python3 main.py data/example.tsv
TODAY'S MENU:
  Burger                       $5.50
  Double Burger                $6.75
  Cheeseburger                 $8.00
  Double Cheeseburger         $10.00
  Fountain Drink               $3.10

What would you like to order?
Cheeseburger
Cheeseburger
Burger
Fountain Drink
Cheeseburger
Fountain Drink

YOUR ORDER:                 Qty     Price     Total
  Cheeseburger                3     $8.00    $24.00
  Burger                      1     $5.50     $5.50
  Fountain Drink              2     $3.10     $6.20
TOTAL                                        $35.70
```


### Edge Cases

If your program isn't given exactly one command line argument, it should print a
usage message and exit immediately:

```
[dent@bistromath]$ python3 main.py
USAGE: main.py menu.tsv
```

If the user tries to order something that isn't on the menu, your program should
print an error message.  It should not exit in this case; it should keep waiting
for more user input.

```
[dent@bistromath]$ python3 main.py data/cheese.tsv
TODAY'S MENU:
  Cheese                      $50.00

What would you like to order?
Cheese
Wine
Sorry, "Wine" isn't on the menu.
```

There might be whitespace  (spaces, tabs, newlines,  etc.)  on either end of the
user input.  Use the `str` member function `strip()` to remove these spaces from
each line of input before processing it.  If the result is an empty string, your
program should ignore it and move on to the next line.

If the user  hasn't successfully ordered anything  by the time you reach the end
of the user input, your program should exit  without printing the order  (or the
preceding newline).


### The TSV File

A TSV file (short for tab-separated values)  is a simple way to store grid-based
data, like a spreadsheet.  Each line in the file is  one row in the spreadsheet,
and within a row, columns are separated with a tab character (`\t`).

Our data files will always contain  exactly two columns.  The first row contains
column headers, which will always be `Name` and `Price`.  The other rows contain
menu items:  the name column contains  an arbitrary string, and the price column
contains a number.

You don't need to worry about  invalid files.  If your program gets  exactly one
command line argument, you can assume that the file exists and is in the correct
format.


## Hints

- Functions that don't have a return value specified should return `None`.
- Prices should always print with exactly two decimal places.
- Names and numbers will always fit in the number of characters specified.
- See the global  `format()` function  and the `str`  member functions `ljust()`
  and `rjust()` for help with formatting your output.
- For even more formatting options, see <https://docs.python.org/3/tutorial/inputoutput.html>.
- For reference, the layouts of the menu and order lines:
  ```
    nnnnnnnnnnnnnnnnnnnnnnnn  pppppppp
    nnnnnnnnnnnnnnnnnnnnnnnn  qqq  pppppppp  tttttttt
  ```
- There are some sample TSV files in the `data` subfolder on GitHub. If you want
  to use these, I recommend downloading them, not copy-and-pasting: your browser
  or your your text editor might try to convert the tabs to spaces.
