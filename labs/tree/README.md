# Tree

In this lab, you'll write a binary search tree: a tree in which each node has at
most two children, and the items are stored in the tree in order.  A node's left
subtree stores  only values that are  less than  the value at that node, and its
right subtree stores only values that are greater. For simplicity, this tree can
hold at most one instance of any value.

This tree  is _not_ self-balancing.  There will be cases when it has poor (O(n))
performance.


## The `Tree` Class

Write a class called `Tree` in `tree.py`. It should support the following member
functions.  You'll probably want a node class and some helper functions as well,
but only the required `Tree` functions will be tested.

- The constructor creates an empty tree.
- `clear()` removes all items from the tree. It returns the number of items that
  were removed.
- `insert(item)` adds an item to the tree.  If the item is already present, this
  function  does nothing;  otherwise,  it adds the item  in a new leaf node.  It
  returns the number of items that were added.
- `remove(item)`  removes an item from the tree  and returns the number of items
  that were removed.
  - If the item to remove is on a node with fewer than two children,  it removes
    that node.  If the node had a child, the child takes its place.
  - If the item is  on a node  with two children,  it finds the largest item `x`
    that is present in the tree but smaller than `item`. It then copies `x` into
    the node containing `item` and removes the node that originally held `x`.
  - If the item isn't present in the tree, it doesn't remove anything.

In addition to providing the member functions described above, your `Tree` class
should also support some standard Python operations:

- Calling `len(tree)` should return the number of items in the tree.
- Converting a tree to a `str` should produce Tree Notation, as described below.
- The expression `item in tree` should evaluate to `True` if `item` is indeed an
  item in `tree`; if not, it should evaluate to `False`.
- The tree should support  item lookup  with square brackets.  Calling `tree[n]`
  with a  non-negative `n` should return `item`  such that there are exactly `n`
  items smaller than `item`  in the tree.  It should accept  negative indices as
  well; the item at index -1 is the largest item in the tree.
  - Indices must be `int`s.  Other types should trigger a `TypeError`.
  - If an index is out of range, raise an `IndexError`.


### Tree Notation

A binary tree might look something like this:

```
    d
   / \
  b   e
 / \   \
a   c   f
```

But we need an easy way  to print a tree to the console.  So we'll define a tree
notation that lets us write a tree structure as a single line. In this notation,
the tree pictured above would look like this:

```
((a b c) d (- e f))
```

More formally:
- The tree notation for a leaf node is simply its value.
- The tree notation for a non-existent node is a hyphen (`-`).
- The tree notation for a non-leaf node is:
  - A left parenthesis, followed by
  - the tree notation for its left subtree, followed by
  - a space, followed by
  - the node's value, followed by
  - a space, followed by
  - the tree notation for its right subtree, followed by
  - a right parenthesis.
- The tree notation for an empty tree is `-`.


## Hints

- Recursion works very well with trees!
- The `insert()` and `remove()` functions will always return one or zero.
- The autograder will use `insert()` to build trees,  then `print()` them to see
  how they look.  If you  haven't implemented  `insert()` or  tree notation, you
  won't get useful test results.
- I've added a tree notation visualizer to the class repo.  It's an HTML file in
  the `docs` folder.  You can run it locally, or you can access it online at:\
  <https://ucsb-cs9.github.io/f24-burk/tree-viewer.html>
