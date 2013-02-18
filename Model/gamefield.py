__author__ = 'Lain'

class gamefield:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

        self.__fallenBlocks = []

        for i in range(0, y):
            temp = []
            for j in range(0, x):
                temp.append(0)
            self.__fallenBlocks.append(temp)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def CurrentFigure(self):
        return self.__CurrentFigure
    @CurrentFigure.setter
    def CurrentFigure(self, CurrentFigure):
        self.__CurrentFigure = CurrentFigure

    __fallenBlocks = []

    def GetBlock(self, x, y):
        return self.__fallenBlocks[y][x]

    def SetBlock(self, x, y, value=0):
        self.__fallenBlocks[y][x] = value

    def GetGrid(self):
        return self.__fallenBlocks

    def updateField(self, line_to_delete):
        #print self.__fallenBlocks
        if not line_to_delete:
            return
        temp = []

        for i in range(0, self.__x):
            temp.append(0)

        for line in line_to_delete:
            del self.__fallenBlocks[line]
            self.__fallenBlocks.insert(0,temp)
        print self.__fallenBlocks

