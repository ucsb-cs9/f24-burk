# Welcome

Welcome to CS 9!  This assignment will make sure  you're able to run Python code
locally and are able to submit your programs to Gradescope.


## The Program

Create a file named `welcome.py`.  In this file,  write a program that takes two
command line arguments, which should be the same length. It then reads its input
one line at a time, replaces any characters found in the first argument with the
corresponding character from the second argument, and prints the result.

For example,  to use your program to capitalize its input  (note that user input
is mixed with the program's output on the command line):

```
[ee@howtown]$ python3 welcome.py abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
and this is the wonder that's keeping the stars apart
AND THIS IS THE WONDER THAT'S KEEPING THE STARS APART
```

Or to censor all lower case vowels:

```
[ee@howtown]$ python3 welcome.py aeiou -----
What I propose, then, is this: that you give Mr. Cummings enough rope.
Wh-t I pr-p-s-, th-n, -s th-s: th-t y-- g-v- Mr. C-mm-ngs -n--gh r-p-.
He may hang himself; or he may lasso a unicorn.
H- m-y h-ng h-ms-lf; -r h- m-y l-ss- - -n-c-rn.
```


## Edge Cases

If your program doesn't get exactly two command line arguments,  it should print
a usage message and exit immediately:

```
[ee@howtown]$ python3 welcome.py oops
USAGE: welcome.py characters replacements
```

If your program is given two command line arguments that aren't the same length,
it should print an error message and exit immediately:

```
[ee@howtown]$ python3 welcome.py hi bye
ERROR: Arguments must be the same length.
```

If the same character appears multiple times in the first command line argument,
your program should use its _last_ occurrence to determine how to replace it:

```
[ee@howtown]$ python3 welcome.py aaa xyz
with up so floating many bells down
with up so flozting mzny bells down
```


## Submission

Test your program  manually!  When you're confident  that it works  as intended,
upload `welcome.py` to Gradescope.  If you pass all the test cases, you're done.
If not, fix the bugs and re-upload your file.  You can resubmit as many times as
you like before the deadline.


## Hints

- Error messages should be followed by exactly one newline.
- There will most likely be newlines in your input. Add the `end=''` argument to
  the `print()` function to keep it from adding more.
- If there are no errors,  your program should only stop when it reaches the end
  of its input.  On Linux and Mac, use `Ctrl+D` to send an "end of input" signal
  to your program while testing; on Windows, use `Ctrl+Z` and then `Enter`.
- On Gradescope, you'll only be able to see your program's output; you can't see
  the input like you can when running locally.
- Make sure you only replace each character once.  If you're replacing `ab` with
  `bc`,  your program should turn `cat` into `cbt`;  it should _not_ replace the
  new `b` with a `c` and print `cct`.
- Your output must match the expected output _exactly_. Case and spacing matter!
