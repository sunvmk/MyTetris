__author__ = 'Lain'

from Settings.Settings import *

class FigureRender:
    def __init__(self, context, offset = 5):
        self.__context = context
        self.__offset = offset

    def SetRenderObject(self, figure):
        self.__figure = figure

    def Init(self):
        self.__canvasData = dict()
        if self.__figure is None:
            print("figure: None")
            return
        for xNum, x in enumerate(self.__figure.templateGrid):
            for yNum, block in enumerate(x):

                if(block == 1):
                    xCoord = (xNum + self.__figure.x) * BLOCK_SIZE + self.__offset
                    yCoord = (yNum + self.__figure.y) * BLOCK_SIZE + self.__offset

                    newGraphObject = self.__context.create_rectangle\
                        (xCoord , yCoord ,
                        xCoord + BLOCK_SIZE, yCoord + BLOCK_SIZE,
                        fill=self.__figure.color)

                    self.__canvasData[str(xNum) + 'x' + str(yNum) + 'y'] = newGraphObject

    def Render(self):
        self.Init()

    def move(self,direction):
        #controller tam ->
        if self.__canvasData == []:
            return
        deltax, deltay = 0, 0
        if direction == "down":
            deltay = 1
        elif direction == "right":
            deltax = 1
        elif direction == "left":
            deltax = -1
        for i, elem in enumerate(self.__canvasData):
            self.__context.move(self.__canvasData[elem],deltax*BLOCK_SIZE,deltay*BLOCK_SIZE)
        self.__figure.x = self.__figure.x + deltax
        self.__figure.y = self.__figure.y + deltay
