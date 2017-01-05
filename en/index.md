# Minecraft Whack A Block

Minecraft is a popular sandbox open-world building game. A free version of Minecraft is available for the Raspberry Pi; it also comes with a programming interface. This means you can write commands and scripts in Python code to build things in the game automatically. It's a great way to learn Python!

## Whack-a-Block

The game you are going to create is called "Whack-a-Block", inspired by the original arcade game ["Whac-a-Mole"](http://en.wikipedia.org/wiki/Whac-A-Mole). The objective of the game is to whack (or hit with a sword) the blocks that light up as glowstone, and turn them back to stone. You will earn points for each block you turn back to stone and the game is over when all the blocks have been turned into glowstone.

![Minecraft Whac-a-Block](images/minecraft-whac-a-block.png)

To create this game you're going to need to use Minecraft Pi Edition on the Raspberry Pi, and the Python 3 programming environment IDLE.

[[[idle-opening]]]

[[[minecraft-opening]]]

[[[minecraft-testing]]]

## Build a Whac-A-Block game board

Now that you are all set-up and ready to go, you can begin creating your game. You can start with a fresh new Python script. Save it as `whac_a_block.py`

1.  The first thing to do is to import the neccessary modules for your game

	~~~ python
	from mcpi.minecraft import Minecraft
	import mcpi.block as block
	from random import randint
	from time import sleep
	~~~

  - `Minecraft` is needed to interact with Minecraft: Pi Edition
  - `mcpi.block` is needed to refer to blocks by name rather than ID
  - `randint` is used to create random intgerst (whole numbers)
  - `sleep` is used to put delays into your program

1.  Below your imports you can create a connection to Minecraft: Pi Edition.

	~~~ python
	mc = Minecraft.create()
	~~~

1.	The next step is to create the game board; this consists of 3x3 stone blocks, which will randomly turn into glowstone and light up.

	The game board will be created just in front of the player, so the first step is to get the player's position using `player.getTilePos()`:  

	~~~ python
	pos = mc.player.getTilePos()
	~~~
	
1.  You can now run this program, although nothing will happen yet. If you now switch over to the IDLE shell, you can try and type the following line of code:

	~~~ python
	print(pos)
	~~~

1.  You should see some something like the following printed out in the shell.

	~~~python
	>>> Vec3(-76,31,-42)
	~~~
	
## Challenge.

> Do you think this means?

### Hint 1
{: .hint-heading #hint-1 }
The first part of the line is `Vec3` which basically means the three numbers after it represent a vector. In geometry a vector is a quantity with both magnitude and direction.
{: .hint-content .hint-1 }

### Hint 2
{: .hint-heading #hint-2 }
The three numbers are often given the symbols of `x`, `y` and `z` in both mathematics and computer games. The `x`, `y` and `z` are directions and the value of the three numbers are their magnitude.
{: .hint-content .hint-2 }
### Hint 3
{: .hint-heading #hint-3 }
Have a look at this image and see if it any help to you.
![x y z](https://commons.wikimedia.org/wiki/File:Coord_system_CA_0.svg#/media/File:Coord_system_CA_0.svg)
{: .hint-content .hint-3 }
### Hint 4
{: .hint-heading #hint-4 }
Have a look a this video that explains how these three values can be used to locate your plaing character in the Minecraft world.
<iframe width="560" height="315" src="https://www.youtube.com/embed/dd_tMc455Rc" frameborder="0" allowfullscreen></iframe>
{: .hint-content .hint-4}






	The player's position is then used with the `setBlocks()` function to create the game board out of stone:

	~~~ python
	mc.setBlocks(pos.x - 1, pos.y, pos.z + 3,
				 pos.x + 1, pos.y + 2, pos.z + 3,
				 block.STONE.id)
	~~~

	![Whac-a-block game board](images/minecraft-game-board.png)

To give the player a warning that the game is about to start, post a couple of messages to the chat window and put a delay into the program using `sleep(seconds)`:

~~~ python
mc.postToChat("Get ready ...")
sleep(2)
mc.postToChat("Go")
~~~

Run the program again. You should see the game board appear directly in front of the player, and the messages "Get ready ..." and "Go".

## Turn the blocks on

Next, you are going to create the code which will turn the stone blocks to glowstone and light them up. The blocks will turn on randomly; you will use the `randint(start, end)` function to pick the random block on the game board.

Create a variable called `blocksLit`; this will hold the number of blocks which are currently lit (i.e. turned into glowstone). Next, create a variable called `points` which will hold how many points the player has scored. As it's the start of the game, set them both to 0:

~~~ python
blocksLit = 0
points = 0
~~~

Your program will need to loop until the game is over, or in this case until all the blocks are lit.

Create a `while` loop which will continue until the `blocksLit` variable is 9 (i.e. all the blocks are turned to glowstone). Next, put a small delay of 0.2 seconds into the program; otherwise it will run so fast, you won't be able to whack any blocks!

~~~ python
while blocksLit < 9:
    sleep(0.2)
~~~

From now on, the code will be indented under this `while` loop.

The next step is to randomly turn a block into glowstone. This is more difficult than it sounds: what happens if the block you randomly choose is already glowstone? Your code needs to be able to deal with this. 

The method you will use is a really simple one. The code creates a random position, checks to see if that block is stone, and if it isn't (i.e. it's glowstone), it tries again and creates a new random position. The code will continue to do this until it finds a block which is still unlit.

Create a variable called `lightCreated` then set it to `False`; next, create a `while` loop which will continue until `lightCreated` is set to `True`. You should also increase the number of `blocksLit` by 1, to show that another block will be lit:

~~~ python
    blocksLit = blocksLit + 1
    lightCreated = False
    while not lightCreated:
~~~

Once a block is successfully turned to glowstone, `lightCreated` will be set to `True` and the loop will exit. 

Inside this loop use `randint(start, end)` to create a random `x` (between -1 and 1) and `y` (between 0 and 2) position on the game board:  

~~~ python
        xPos = pos.x + randint(-1,1)
        yPos = pos.y + randint(0,2)
        zPos = pos.z + 3
~~~

![A random block lit up](images/minecraft-random-block.png)

Use `getBlock(x,y,z)` and an `if` statement to check if the block at the random position is STONE. If it is, set it to glowstone using `setBlock(x,y,z,blockId)` and make `lightCreated = True`; if this is not changed, the code will go back to the start of the loop and find another random position.

~~~ python
        if mc.getBlock(xPos, yPos, zPos) == block.STONE.id:
            mc.setBlock(xPos, yPos, zPos, block.GLOWSTONE_BLOCK.id)
            lightCreated = True
~~~

**Note**: Rather than using the ID numbers of blocks (e.g. stone = 1, glowstone = 89), you can use the `block` module, which holds all the block IDs and their names (e.g. `block.STONE.id`).

Run the program by clicking `Run > Run Module` in IDLE or by pressing F5; you should see the game board appear. The stone blocks should then, one by one, turn into glowstone and the program should end when all nine are lit.

## Whack blocks

The player will whack blocks by hitting them (right-clicking) while holding a sword. The Minecraft API has functions which allow you to find out what blocks were hit; these are known as block hit *events*. Using the function `events.pollBlockHits()` you can get a list of the events that have occurred since it was last called, such as blocks which were hit.

You will use events to find out the position of the block which was hit, before using `getBlock(x,y,z)` to see if the block hit was glowstone. If it was, you will then use `setBlock(x,y,z,blockId)` to turn it back to stone, before reducing the number of blocks lit and increasing the player's score.

Indented under the `while blocksLit < 9` loop, create the following code to loop through the block hit events list:

~~~ python
    for hitBlock in mc.events.pollBlockHits():
~~~

**Note**: The `hitBlock` variable holds the *event* which has happened. It contains lots of information, including which block was hit, what face was hit and who hit it. You can see this information in the Python shell by using `print hitBlock`.

Use `getBlock(x,y,z)`, the `hitBlock` event data and an `if` statement to see if the block hit was glowstone. If it was, use `setBlock(x,y,z,blockId)` to set it back to stone before reducing the `blocksLit` variable and adding 1 to the player's `points`:

~~~ python
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.GLOWSTONE_BLOCK.id:
            mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, block.STONE.id)
            blocksLit = blocksLit - 1
            points = points + 1 
~~~

Run the program. The game board should appear and this time when the blocks are lit, if you hit them by right-clicking with a sword, they should turn off.

**Hint: Click here to see the full code**
{: .hint-heading #hint-20 }

~~~ python
from gpiozero import MotionSensor

pir = MotionSensor({var1} 

pir.wait_for_motion() 
print('Motion detected!') 
~~~
{: .hint-content .hint-20 }


## Game over

The last step in the game is to let the player know it's "Game Over" and to tell them how many points they scored. The very last line of the program should be:

~~~ python
mc.postToChat("Game Over - points = " + str(points))
~~~

![Game over](images/minecraft-game-over.png)
