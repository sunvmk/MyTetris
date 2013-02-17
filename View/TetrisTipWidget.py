__author__ = 'Lain'

from Tkinter import *
from FigureRender import *
from Controller.TetrisController import *
from Settings.Settings import *

class TetrisTipWidget(Frame):

    BORDER_OFFSET = 2;

    def __init__(self, root, controller, bordercolor = DEFAULT_BORDER_COLOR, tipbackcolor = DEFAULT_FIGURE_TIP_COLOR):
        Frame.__init__(self, root, width = BLOCK_SIZE * (FIGURE_TEMPLATE_SIZE + 1),
            height = BLOCK_SIZE * (FIGURE_TEMPLATE_SIZE + 1));

        self.__canvas = Canvas(self, width=BLOCK_SIZE * (FIGURE_TEMPLATE_SIZE + 1),
            height=BLOCK_SIZE * (FIGURE_TEMPLATE_SIZE + 1), background=tipbackcolor,
            highlightbackground = bordercolor);
        self.__canvas.pack();

        self.__controller = controller;
        self.__figureRender = FigureRender(self.__canvas, TetrisTipWidget.BORDER_OFFSET);

    def mainloop(self, n=0):
        self.__figureRender.SetRenderObject(self.__controller.GetNextFigure());
        self.__figureRender.Render();

        Canvas.mainloop(self.__canvas);
        Frame.mainloop(self, n=0);


