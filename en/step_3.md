## Build a Whack-A-Block game board

1.  You can now begin creating your game. You can start with a fresh new Python script. Save it as `whac_a_block.py`

1.  Next you want to import the neccessary module and create a connection to Minecraft

~~~ python
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
~~~

1.  To begin with you're going to need to know Steve's position in the game. If you don't know how to do this, then you can use the section below, or skip forward if you already know how to do this.

[[[minecraft-steves-position]]]

1.  Now that you know how to get Steve's position, you can begin your program by storing his poition as three variables. You can use `px`, `py`, and `pz`

~~~ python
px, py, pz = mc.player.getPos()
~~~
