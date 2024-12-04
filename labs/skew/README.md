# Skew

You can think of splay trees as  carefree AVL trees.  AVL trees are meticulously
self-balancing,  and guarantee O(log n) runtimes for all tree operations.  Splay
trees just rotate and hope for the best. Perhaps surprisingly, this works almost
as well: they provide amortized O(log n) runtimes for all tree operations.

There's an equivalent pairing  of heaps.  Leftist heaps keep track of the height
or weight of each node and perform careful swaps to make sure that left children
are always taller or heavier than their right siblings.  Skew heaps always swap.
And like with splay trees,  this works,  and they end up with amortized runtimes
of O(log n) for both `push()` and `pop()`.


## The Program

In `main.py`,  write a program that lets you interact with  a skew min heap that
holds  strings.  It reads its input one  line at a time, and removes leading and
trailing whitespace.  The result  will either be  an empty line, which it should
ignore, or one the following commands.

- `count` prints the number of items in the heap.
- `pop` removes the smallest string from the heap and prints it.
- `print` prints the heap in tree notation, as in the previous labs.
- `push some string` adds `some string` to the heap. Note that `some string` may
  contain internal whitespace.
- `top` prints the smallest string in the heap.

```
[king@hill]$ python3 main.py
push A
push B
push C
print
(B A C)
count
3
pop
A
print
(- B C)
```

Commands that don't work on empty heaps should print an error message instead of
their normal output when the heap is empty:

```
ERROR: Heap is empty.
```

The `push` command  is separated from its argument by at least one (and possibly
multiple) whitespace characters, which are not part of the argument. If there is
no argument, it should print an error message:

```
ERROR: No argument.
```

Only the required commands will be tested. You're encouraged to add commands (or
aliases that are easier to type) to make your testing easier.


### Merge

Like with leftist heaps,  push and pop  are implemented as heap merges.  A merge
happens between two heaps, which we'll call "left" and "right."  To merge, first
find the "spine" that runs down the left side of each heap. Merge the two spines
like  you would merge  two sorted linked lists  (if two nodes hold equal values,
give priority to the node from the left heap). Then swap the children of all the
nodes in the spine of the resulting heap.

```
    A             B              A              A
   / \           / \            / \            / \
  B   D    +    F   M    =>    B   D    =>    D   B
 / \   \       /   / \        / \   \          \  |\
E   Q   S     G   X   Z      B   Q   S          S Q B
                            / \                    / \
                           E   M                  M   E
                          /   / \                / \   \
                         F   X   Z              X   Z   F
                        /                                \
                       G                                  G
```

When pushing a value,  the singleton heap holding the new value should always be
the right heap.  When popping,  the left and right heaps are  the left and right
children, respectively, of the old root.


## Hints

- The "smallest" string is the one that comes first "asciibetically" (characters
  are compared by their  [ASCII values][ascii]).  You don't  have to do anything
  special  to implement this:  this is how Python compares strings  when you use
  the standard comparison operators.


[ascii]: <https://en.wikipedia.org/wiki/ASCII>
