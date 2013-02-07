import Tkinter
import sys

class display:
    def __init__(self, width=10, height=10, grid_size=10):
        self._width = width * grid_size
        self._height = height * grid_size
        self._grid_size = grid_size
        self._canvas_x = 0
        self._canvas_y = self._width - 1
        self._canvas_xs = self._width - 1
        self._canvas_ys = self._height - 1
        self._canvas = None
        self._root_window = None
        self._figure = None
        self._poly = [] #TODO move to figure class

    def begin_graphics(self):
        # Check for duplicate call
        if self._root_window is not None:
            # Lose the window.
            self._root_window.destroy()

        self._root_window = Tkinter.Tk()#TODO refactor
        #self._root_window.protocol('WM_DELETE_WINDOW', self._destroy_window)
        self._root_window.title('Tetris')
        self._root_window.resizable(0, 0)
        try:
            self._canvas = Tkinter.Canvas(self._root_window, width=self._width, height=self._height)
            self._canvas.pack()
            #self._canvas.update()
        except:
            self._root_window = None
            raise

        self._root_window.bind( "<KeyPress>", self._keypress )
        #self._root_window.bind( "<KeyRelease>", _keyrelease )

    def draw_field(self, field):
        #poly = self._canvas.create_rectangle(10,90,20,100, fill="green", outline="blue")
        #poly = self._canvas.create_rectangle(20,90,30,100, fill="green", outline="blue")
        for xNum, x in enumerate(field):
            for yNum, cell in enumerate(x):
                if cell == 1:
                    xc,yc = ((yNum*self._grid_size),(xNum*self._grid_size))
                    poly = self._canvas.create_rectangle(xc,yc,xc+self._grid_size,yc+self._grid_size, fill="green", outline="blue")
                    #add poly mas
                    print xNum,yNum

        #self._canvas.update()
        #self._canvas.pack()
    def draw_figure(self, figure):
        self._poly=[]
        xstart = figure.x*self._grid_size
        ystart = figure.y*self._grid_size
        shape = figure.template[figure.state]
        self._figure = figure

        for xNum, x in enumerate(shape):
            for yNum, cell in enumerate(x):
                if cell == 1:
                    yc = ystart +yNum*self._grid_size
                    xc = xstart +xNum*self._grid_size
                    self._poly.append(self._canvas.create_rectangle(xc,yc,xc+self._grid_size,yc+self._grid_size, fill="green", outline="blue"))

    def move_figure(self, direction):
        if self._poly == []:
            pass
        deltax, deltay = 0, 0
        if direction == "down":
           deltay = 1
        elif direction == "right":
            deltax = 1
        elif direction == "left":
            deltax = -1
        for i, elem in enumerate(self._poly):
            self._canvas.move(elem,deltax*self._grid_size,deltay*self._grid_size)
        self._figure.x = self._figure.x + deltax
        self._figure.y = self._figure.y + deltay

    def rotate_figure(self):
        if self._poly == []:
            pass
        spape = self._figure.rotate()
        for i, elem in enumerate(self._poly):
            self._canvas.delete(elem)
        self.draw_figure(self._figure)

    def delete_figure(self):
        if self._poly == []:
            pass
        for i, elem in enumerate(self._poly):
            self._canvas.delete(elem)
        self._poly =[]
        self._figure = None

    def start(self):
        self._root_window.mainloop()
    def update(self):
        self._root_window.update_idletasks()
        self._root_window.update()

    #@property
    #def display(self):
    #    return self._root_window

    @property
    def cur_figure(self):
        return self._figure

    def _keypress(self, event):
        print event.char, event.keycode
        if event.keycode == 40:
            self.move_figure("down")
        elif event.keycode == 37:
            self.move_figure("left")
        elif event.keycode == 39:
            self.move_figure("right")
        elif event.keycode == 32:
            self.rotate_figure()

    def _destroy_window(self,event=None):
        sys.exit(0)