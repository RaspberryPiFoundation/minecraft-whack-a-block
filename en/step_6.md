## Challenge

Define a function called `pop_up()` that takes no arguments. Within the function, shuffle each row of the `board` list, and then shuffle the `board` itself. Once this has been completed, call the `draw_board()` function.

### Hint 1
{: .hint-heading #hint-5 }
1. First you'll need to use a `for` loop to iterate through `board` and shuffle each row.  
2. Then you can shuffle the board.  
3. Lastly you can call the `draw_board` function.  
{: .hint-content .hint-5 }

### Hint 2
{: .hint-heading #hint-6 }
To shuffle the board you can use the line:  
~~~ python
shuffle(board)
~~~
{: .hint-content .hint-6 }

### Hint 3
{: .hint-heading #hint-7 }
To shuffle each row you can use a `for` loop.  
~~~ python
for row in board:
    shuffle(row)
~~~
{: .hint-content .hint-7 }

### Hint 4
{: .hint-heading #hint-8 }
Have a look at the video below to see the function being written.  
{: .hint-content .hint-8 }
