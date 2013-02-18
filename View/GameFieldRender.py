__author__ = 'Lain'

from Settings.Settings import *

class GameFieldRender:
    def __init__(self, gamefield, context, offset = 5, blockcolor = DEFAULT_FILLED_BLOCK_COLOR):
        self.__context = context
        self.__gamefield = gamefield
        self.__offset = offset
        self.__blockColor = blockcolor

        self.Init()

    def Init(self):
        self.__canvasData = dict()

        for xNum in range(0, self.__gamefield.x):
            for yNum in range(0, self.__gamefield.y):
                self.RenderBlock(xNum, yNum)


    def Render(self):
        for xNum in range(0, self.__gamefield.x ):
            for yNum in range(0, self.__gamefield.y ):
                self.RenderBlock(xNum, yNum)

    def RenderBlock(self, x, y):
        block = self.__gamefield.GetBlock(x, y)

        if(block == 1):
            newGraphObject = self.__context.create_rectangle\
                (x * BLOCK_SIZE + self.__offset , y * BLOCK_SIZE + self.__offset,
                x * BLOCK_SIZE + BLOCK_SIZE + self.__offset, y * BLOCK_SIZE + BLOCK_SIZE + self.__offset,
                fill=self.__blockColor)
            self.__canvasData[str(x) + 'x' + str(y) + 'y'] = newGraphObject
        else:
            if(self.__canvasData.has_key(str(x) + 'x' + str(y) + 'y')):
                print self.__canvasData[str(x) + 'x' + str(y) + 'y']
                self.__context.delete(self.__canvasData[str(x) + 'x' + str(y) + 'y'])
                del self.__canvasData[str(x) + 'x' + str(y) + 'y']

