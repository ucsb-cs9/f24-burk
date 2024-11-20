# Morse

[Morse code][morse]  is an old encoding scheme used  to send text over telegraph
lines and other one-bit channels.  Since these channels only have two states (on
and off), it uses time to encode extra information.  Every letter is represented
as a series of short and long signals,  with a pause between letters and an even
longer pause between words.

When transcribing Morse code, short signals (called dit or dot) are written with
a period (`.`),  while long signals (called dah or dash) are written with a dash
(`-`).  You can think of these signals as describing a path through a tree:

```
                              │
              ╭──────────────╴*╶──────────────╮               A .-    J .---  S ...
              │          ← .     - →          │               B -...  K -.-   T -
      ╭──────╴E╶──────╮               ╭──────╴T╶──────╮       C -.-.  L .-..  U ..-
      │               │               │               │       D -..   M --    V ...-
  ╭──╴I╶──╮       ╭──╴A╶──╮       ╭──╴N╶──╮       ╭──╴M╶──╮   E .     N -.    W .--
  │       │       │       │       │       │       │       │   F ..-.  O ---   X -..-
╭╴S╶╮   ╭╴U     ╭╴R     ╭╴W╶╮   ╭╴D╶╮   ╭╴K╶╮   ╭╴G╶╮     O   G --.   P .--.  Y -.--
│   │   │       │       │   │   │   │   │   │   │   │         H ....  Q --.-  Z --..
H   V   F       L       P   J   B   X   C   Y   Z   Q         I ..    R .-.
```

In a file named `morse.py`, write a program that encodes and decodes Morse code.
This program takes one or two command line arguments. The first is required, and
must be either `-e` (for encode) or `-d` (for decode).

The second argument  is optional.  Your program  should use  International Morse
Code  (shown above) by default.  But if the second argument is given, it will be
the path to  a tree file (see below) describing a different encoding scheme, and
your program should use that encoding instead.

### Encoding

In encode mode,  your program should loop over its input one line at a time.  It
should translate each line to Morse code (ignoring case) and print the result.

In  the input,  words will be  separated by  one or more  whitespace  characters
(spaces, tabs, etc.).  In the output,  separate Morse characters  with one space
and words with two spaces.

```
[dearheart@gtsc]$ python3 morse.py -e
SOS
... --- ...
```

The input may contain characters you can't translate.  Your output should be the
same as if these characters were not present in the input.

```
[dearheart@gtsc]$ python3 morse.py -e
"What hath God wrought?"
.-- .... .- -  .... .- - ....  --. --- -..  .-- .-. --- ..- --. .... -
```

### Decoding

In decode mode, your program should loop over its input one line at a time. Each
line should contain Morse code; decode it and print the result.  All the letters
in the output should be upper case.

In the input, Morse characters will be separated by single whitespace characters
(spaces, tabs, etc.),  and words  will be  separated by  two or more  whitespace
characters.  In the output, separate words with one space.

```
[dearheart@gtsc]$ python3 morse.py -d
-- --- .-. ... .  -.-. --- -.. .
MORSE CODE
```

The input may contain  "Morse characters"  that aren't entirely composed of dots
and dashes,  and some patterns of dots and dashes may not  map to any character.
Output these as question marks.

```
[dearheart@gtsc]$ python3 morse.py -d
..  ... .- .. -..  HI THERE  .....
I SAID ?? ?
```

### Tree Files

A valid tree file contains a single line of text.  This text is a binary tree in
tree notation, as described in the previous lab.

Tree nodes may only contain  capital letters, numbers, or the asterisk character
(`*`, which represents a node with no value). All characters except the asterisk
may appear in the tree  at most once;  not all characters must appear.  The root
node must exist, and must contain an asterisk (no value).

### Edge Cases

If given invalid command line arguments, print a usage message and exit:

```
USAGE: morse.py [-e or -d] [tree-file]
```

If given an invalid tree file, print an error message and exit:

```
ERROR: Invalid tree file.
```

Ignore any leading or trailing whitespace in the input lines. Your output should
never contain leading or trailing spaces.


[morse]: <https://en.wikipedia.org/wiki/Morse_code>
