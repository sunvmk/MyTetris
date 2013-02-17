__author__ = 'Lain'

from Tkinter import *
from FigureRender import *
from GameFieldRender import *
from Controller.TetrisController import *
from Settings.Settings import *

class TetrisWidget(Frame):

    BORDER_OFFSET = 2

    def __init__(self, root, controller,
                 backcolor=DEFAULT_BACKGROUND_COLOR,bordercolor = DEFAULT_BORDER_COLOR):

        self.__controller = controller;

        Frame.__init__(self, root, width=BLOCK_SIZE * self.__controller.GetGameField().x,
            height=BLOCK_SIZE * self.__controller.GetGameField().y);

        self.__canvas = Canvas(self, width=BLOCK_SIZE * self.__controller.GetGameField().x,
            height=BLOCK_SIZE * self.__controller.GetGameField().y, background=backcolor,
            highlightbackground = bordercolor);
        self.__canvas.pack();

        self.__figureRender = FigureRender(self.__canvas, TetrisWidget.BORDER_OFFSET);
        self.__figureRender.SetRenderObject(self.__controller.GetCurrentFigure());

        self.__gameFieldRender = GameFieldRender(self.__controller.GetGameField(), self.__canvas, TetrisWidget.BORDER_OFFSET);

    def mainloop(self, n=0):
        self.__figureRender.Render();
        self.__gameFieldRender.Render();
        Canvas.mainloop(self.__canvas);
        Frame.mainloop(self, n=0);

