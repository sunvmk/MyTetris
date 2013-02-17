__author__ = 'Lain'

from Model.figure import *
from Model.gamefield import *
from Settings.Settings import *
import random
import copy

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
        self.__figure = figure(x=self.__gamefield.x/2-2, y=0, type = random.randrange(1,7))

    def collisionCheck(self, direction):
        # bottom border
        if self.__figure.y + self.__figure.height == self.__gamefield.y:
            return True
        # right border
        if self.__figure.x + self.__figure.width == self.__gamefield.x:
            print("right border")
        # left border
        if self.__figure.x == 0:
            print ("left border")
        # field collision


        return False

    def appendFigure(self):
         for i in range(0, self.__figure.height):
            for j in range(0, self.__figure.width):
                ololo = self.__figure.templateGrid
                if ololo[j][i]:
                    self.__gamefield.SetBlock(self.__figure.x+j,self.__figure.y+i, 1)

    def keypress(self, event):
        print event.char, event.keycode
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



