## Whack blocks

The player will whack blocks by hitting them (right-clicking) while holding a sword. The Minecraft API has functions which allow you to find out what blocks were hit; these are known as block hit *events*. Using the function `events.pollBlockHits()` you can get a list of the events that have occurred since it was last called, such as blocks which were hit.

You will use events to find out the position of the block which was hit, before using `getBlock(x,y,z)` to see if the block hit was glowstone. If it was, you will then use `setBlock(x,y,z,blockId)` to turn it back to stone, before reducing the number of blocks lit and increasing the player's score.

1.  Indented under the `while blocks_lit < 9` loop, create the following code to loop through the block hit events list:

	~~~ python
		for hitBlock in mc.events.pollBlockHits():
	~~~

	**Note**: The `hitBlock` variable holds the *event* which has happened. It contains lots of information, including which block was hit, what face was hit and who hit it. You can see this information in the Python shell by using `print hitBlock`.

1.  Use `getBlock(x,y,z)`, the `hitBlock` event data and an `if` statement to see if the block hit was glowstone. If it was, use `setBlock(x,y,z,blockId)` to set it back to stone before reducing the `blocks_lit` variable and adding 1 to the player's `points`:

	~~~ python
			if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == 89:
				mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, 1)
				blocks_lit = blocks_lit - 1
				points = points + 1
	~~~

1.  Run the program. The game board should appear and this time when the blocks are lit, if you hit them by right-clicking with a sword, they should turn off.


## Game over

The last step in the game is to let the player know it's "Game Over" and to tell them how many points they scored. The very last line of the program should be:

~~~ python
mc.postToChat("Game Over - points = " + str(points))
~~~

![Game over](images/minecraft-game-over.png)
