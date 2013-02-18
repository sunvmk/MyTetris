__author__ = 'Lain'

from Model.figure import *
from Model.gamefield import *
from Settings.Settings import *
import random
import copy
import time

class TetrisController:
    def __init__(self, gameFieldWidth = 10, gameFieldHeight = 10, figureSize = FIGURE_TEMPLATE_SIZE):

        self.__templateFigureSize = figureSize
        self.__figure = None
        self.__gamefield = gamefield(gameFieldWidth, gameFieldHeight)
        self.__action = None

    def GetCurrentFigure(self):
        return self.__figure

    def GetGameField(self):
        return self.__gamefield

    def GetNextFigure(self):
        return figure(x=0, y=0, type = random.randrange(1,7))

    def spawnFigure(self):
        self.__action = None
        self.__figure = figure(x=self.__gamefield.x/2-2, y=0, type = 2)

    def collisionCheck(self, direction):
        if direction=="down":
            return self.__collision_down()
        elif direction=="right":
            return self.__collision_right()
        elif direction=="left":
            return self.__collision_left()
        elif direction=="rotate":
            return self.__collision_rotate()
        return False

    def __collision_down(self):
        #bottom border
        if self.__figure.y + self.__figure.height == self.__gamefield.y:
            return True

        return self.__field_figure_collision("down")

    def __collision_right(self):
        # right border
        if self.__figure.x + self.__figure.width == self.__gamefield.x:
            return True
        return self.__field_figure_collision("right")

    def __collision_left(self):
        # left border
        if self.__figure.x == 0:
            return True
        return self.__field_figure_collision("left")

    def __collision_rotate(self):
        # hz
        time.sleep(10)
        self.__field_figure_collision("rotate")
        return False

    def __field_figure_collision(self, action):
        # check distance figure - filled field
        if self.__figure is None:
            return False

        #if self.__figure.y + self.__figure.height < self.__get_cur_max_field():
        # no need this shit
        #    return False

        if action=="down":
            #TODO add method
            for xNum, x in enumerate(self.__figure.templateGrid):
                for yNum, block in enumerate(x):
                    if block == 1:
                        xCoord = xNum + self.__figure.x
                        yCoord = yNum + self.__figure.y + 1 # shift - down
                        if (self.__gamefield.GetBlock(xCoord, yCoord) == 1):
                            return True

        elif action=="right":
            #TODO add method
            for xNum, x in enumerate(self.__figure.templateGrid):
                for yNum, block in enumerate(x):
                    if block == 1:
                        xCoord = xNum + self.__figure.x + 1 # shift - right
                        yCoord = yNum + self.__figure.y
                        if (self.__gamefield.GetBlock(xCoord, yCoord) == 1):
                            return True

        elif action=="left":
            #TODO add method
            for xNum, x in enumerate(self.__figure.templateGrid):
                for yNum, block in enumerate(x):
                    if block == 1:
                        xCoord = xNum + self.__figure.x - 1 # shift - left
                        yCoord = yNum + self.__figure.y
                        if (self.__gamefield.GetBlock(xCoord, yCoord) == 1):
                            return True

        elif action=="rotate":
            pass

        return False



    def appendFigure(self):
         #self.__gamefield.print_ololo()
         for i in range(0, self.__figure.height):
            for j in range(0, self.__figure.width):
                block = self.__figure.templateGrid
                if block[j][i]:
                    self.__gamefield.SetBlock(self.__figure.x+j,self.__figure.y+i, 1)
                    #self.__gamefield.print_ololo()
         #time.sleep(15)

    def keypress(self, event):
        #print event.char, event.keycode
        if event.keycode == 40:
            self.__action = "down"
        elif event.keycode == 37:
            self.__action = "left"
        elif event.keycode == 39:
            self.__action = "right"
        elif event.keycode == 32:
            self.__action = "rotate"
        else:
            self.__action = None

    def getAction(self):
        return self.__action

    def resetAction(self):
        self.__action = None

    def __get_cur_max_field(self):
        pass

    def find_full_line(self):
        line_list = []
        for i in range(0, self.__gamefield .y):
            if self.__gamefield.GetBlock(0,i) == 1:
                tmp = []
                for j in range(0, self.__gamefield.x):
                    if self.__gamefield.GetBlock(j,i) == 0:
                        break
                    tmp.append(1)
                if len(tmp) == self.__gamefield.x:
                    line_list.append(i)
        self.__gamefield.updateField(line_list)

