## Turn the blocks on

To begin the next part of the program, you'll need to create two new variables and set them both to the value of `0`. `blocks_lit` stores the number of blocks that have been "lit-up". `points` will store the number of blocks that the player has managed to hit.

~~~ python
blocks_lit = 0
points = 0
~~~

You now need to write your main game loop. To start off with, you'll need to know a little bit about how you can generate random numbers in Python. Skip down to the section below, if you are already familiar with this.

[[[python-random]]]
