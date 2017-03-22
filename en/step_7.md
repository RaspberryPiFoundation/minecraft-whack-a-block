## Getting the player ready

Now that you have a gameboard for the player to use, you need to create the logic for the game itself.

1.  To give the player a warning that the game is about to start, post a couple of messages to the chat window and put a delay into the program using `sleep(seconds)`. The following code can be placed into your program after the initial gameboard has been created.

	~~~ python
	mc.postToChat("Get ready ...")
	sleep(2)
	mc.postToChat("Go")
	~~~

1.  Run the program again. You should see the game board appear directly in front of the player, and the messages "Get ready ..." and "Go".
