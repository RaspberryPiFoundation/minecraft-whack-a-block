from mcpi.minecraft import Minecraft
from random import shuffle
from threading import Thread, Timer
from time import sleep

mc = Minecraft.create()
px, py, pz = mc.player.getPos()

board = [[1, 1, 1],
         [1, 89, 1],
         [1, 1, 1]]

pause = 2
game_over = False
points = 0

def draw_board():
    for y, row in enumerate(board):
        for x, block in enumerate(row):
            mc.setBlock(px+x, py+y, pz + 3, block)
         
def pop_up():
    for row in board:
        shuffle(row)
    shuffle(board)
    draw_board()

def game():
    while not game_over:
        pop_up()
        sleep(pause)

def end():
    global game_over
    game_over = True

go = Thread(target=game)
go.start()

t = Timer(60, end)
t.start()

while not game_over:
    for hitBlock in mc.events.pollBlockHits():
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == 89:
            pop_up()
            points += 1
            if pause > 0.2:
                pause -= 0.05

mc.postToChat('You scored {0}'.format(points))

        
        
