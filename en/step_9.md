## Challenge

You can being your main loop by making a random block change from stone to glowstone.
1. Use a `while` loop that continues so long as `blocks_lit` is less than 9
2. Within the loop,

	Create a `while` loop which will continue until the `blocks_lit` variable is 9 (i.e. all the blocks are turned to glowstone). Next, put a small delay of 0.2 seconds into the program; otherwise it will run so fast, you won't be able to whack any blocks!

	From now on, the code will be indented under this `while` loop.

1.  The next step is to randomly turn a block into glowstone. This is more difficult than it sounds: what happens if the block you randomly choose is already glowstone? Your code needs to be able to deal with this.

	The method you will use is a really simple one. The code creates a random position, checks to see if that block is stone, and if it isn't (i.e. it's glowstone), it tries again and creates a new random position. The code will continue to do this until it finds a block which is still unlit.

	Create a variable called `lightCreated` then set it to `False`; next, create a `while` loop which will continue until `lightCreated` is set to `True`. You should also increase the number of `blocks_lit` by 1, to show that another block will be lit:

	~~~ python
		blocks_lit = blocks_lit + 1
		lightCreated = False
		while not lightCreated:
	~~~

	Once a block is successfully turned to glowstone, `lightCreated` will be set to `True` and the loop will exit.

1.  Inside this loop use `randint(start, end)` to create a random `x` (between -1 and 1) and `y` (between 0 and 2) position on the game board:  

	~~~ python
			xPos = pos.x + randint(-1,1)
			yPos = pos.y + randint(0,2)
			zPos = pos.z + 3
	~~~

	![A random block lit up](images/minecraft-random-block.png)

1.  Use `getBlock(x,y,z)` and an `if` statement to check if the block at the random position is STONE. If it is, set it to glowstone using `setBlock(x,y,z,blockId)` and make `lightCreated = True`; if this is not changed, the code will go back to the start of the loop and find another random position.

	~~~ python
			if mc.getBlock(xPos, yPos, zPos) == 1:
				mc.setBlock(xPos, yPos, zPos, 89)
				lightCreated = True
	~~~

	**Note**: Rather than using the ID numbers of blocks (e.g. stone = 1, glowstone = 89), you can use the `block` module, which holds all the block IDs and their names (e.g. `1`).

1.  Run the program by clicking `Run > Run Module` in IDLE or by pressing F5; you should see the game board appear. The stone blocks should then, one by one, turn into glowstone and the program should end when all nine are lit.
