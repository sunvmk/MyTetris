__author__ = 'Lain'

from Settings.Settings import *

class FigureRender:
    def __init__(self, context, offset = 5):
        self.__context = context;
        self.__offset = offset;

    def SetRenderObject(self, figure):
        self.__figure = figure;

    def Init(self):
        self.__canvasData = dict();

        for xNum, x in enumerate(self.__figure.templateGrid):
            for yNum, block in enumerate(x):

                if(block == 1):
                    xCoord = (xNum + self.__figure.x) * BLOCK_SIZE + self.__offset;
                    yCoord = (yNum + self.__figure.y) * BLOCK_SIZE + self.__offset;

                    newGraphObject = self.__context.create_rectangle\
                        (xCoord , yCoord ,
                        xCoord + BLOCK_SIZE, yCoord + BLOCK_SIZE,
                        fill=self.__figure.color);

                    self.__canvasData[str(xNum) + 'x' + str(yNum) + 'y'] = newGraphObject;

    def Render(self):
        self.Init();





