from __future__ import print_function

__author__ = 'Lain'

from Model.figure import *
from Model.gamefield import *
from Model.display import *
#from controller import *

import time
import random

if __name__ == "__main__":
    print("Main...")
    x, y = 10 , 20
    grid_size = 10
    testFs = [
              figure(x/2, 0, 0, [[(1,1,1),(0,1,0)],[(1,0),(1,1),(1,0)],[(0,1,0),(1,1,1)],[(0,1),(1,1),(0,1)]]),
              figure(x/2, 0, 0, [[(1,1),(1,1)]]),
              figure(x/2, 0, 0, [[(0,1),(0,1),(0,1),(0,1)],[(1,1,1,1)]]),
              figure(x/2, 0, 0, [[(1,1,0),(0,1,1)],[(0,1),(1,1),(1,0)]]),
              figure(x/2, 0, 0, [[(0,1,1),(1,1,0)],[(1,0),(1,1),(0,1)]]),
              figure(x/2, 0, 0, [[(0,1),(0,1),(1,1)],[(1,1,1),(0,0,1)],[(1,1),(1,0),(1,0)],[(1,0,0),(1,1,1)]]),
              figure(x/2, 0, 0, [[(1,0),(1,0),(1,1)],[(0,0,1),(1,1,1)],[(1,1),(0,1),(0,1)],[(1,1,1),(1,0,0)]])
             ]
    testField = gamefield(x, y)
    testDisplay = display(x,y,grid_size)
    testDisplay.begin_graphics()
    testDisplay.draw_field(testField.GetGrid())
    rnd = random.randrange(0,6)
    #ctr = ConTroller(testDisplay.display)
    testDisplay.draw_figure(testFs[rnd])

    while 1:
        time.sleep(0.35)
        #collision detection
        can_move = True
        c_figure = testDisplay.cur_figure #current figure
        #testField #current field
        #testField.x
        #testField.y
        #c_figure.x
        #c_figure.y
        #c_figure.width
        #c_figure.height

        #check for a border
        if c_figure.y + c_figure.height == testField.y:
            can_move = False
        if(can_move):
            testDisplay.move_figure("down")
        else:
            #update field of justice
            testField.append(c_figure)
            testDisplay.draw_field(testField.GetGrid())
            #spawn new figure
            rnd = random.randrange(0,6)
            testDisplay.draw_figure(testFs[rnd])

        testDisplay.update()
    testDisplay.start()

    for i in range(0, testField.y):
        print()
        for j in range(0, testField.x):
            print(testField.GetCell(i, j), end='')



