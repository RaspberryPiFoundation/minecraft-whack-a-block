## Challenge

Create a function called `draw_board`, that takes no arguments. In the function you will need two nested `for` loops to `enumerate` through the 2d board list.
The loops should set blocks, 3 spaces away from the player's `z` position, and a number of spaces away from the player's `x` and `y` postion equal to the indices in the list. The block should correspond to the values in the lists.

So for instance:
- the first block would be placed 0 spaces away from the player on both `x` and `y`.
- the second block would be placed 1 spaces away from the player on the `x` and 0 spaces away on the `y`
- the third block would be placed 2 spaces away from the player on the `x` and 0 spaces away on the `y`
- the fourth block would be placed 0 spaces away from the player on the `x` and 1 space away on the `y`

### Hint 1
{: .hint-heading #hint-1 }
Here's what the code would look like in structured English.  
1. Define the function `draw_board`  
2. Enumerate over each row in the `board`  
3. Enumerate over each block in the `row`  
4. Set a block adding the index of the block to Steve's `px` position, and the index of the row to Steve's `py` position. You should always add 3 to Steve's `pz` position.
{: .hint-content .hint-1 }

### Hint 2
{: .hint-heading #hint-2 }
To enumerate over the board, your first `for` loop would look something like this:  
~~~ python
for y, row in enumerate(board):
~~~
{: .hint-content .hint-2 }

### Hint 3
{: .hint-heading #hint-3 }
Your final line within the nested `for` loops should look something like this:  
~~~ python
mc.setBlock(px+x, py+y, pz + 3, block)
~~~
{: .hint-content .hint-3 }

### Hint 4
{: .hint-heading #hint-4 }
Have a look at this video of the code being written and run if you are completely stuck.  
![challenge1](images/challenge1.gif)
{: .hint-content .hint-4}
