__author__ = 'Lain'

BLOCK_SIZE = 20
FIGURE_TEMPLATE_SIZE = 4

DEFAULT_BACKGROUND_COLOR = "lavender"
DEFAULT_FILLED_BLOCK_COLOR = "sky blue"
DEFAULT_BORDER_COLOR = "gray"

DEFAULT_FIGURE_COLOR = DEFAULT_FILLED_BLOCK_COLOR
DEFAULT_FIGURE_TIP_COLOR = DEFAULT_BACKGROUND_COLOR
DEFAULT_FIGURE_TYPE =\
                {
                    1:[[(1,1,1),(0,1,0)],[(1,0),(1,1),(1,0)],[(0,1,0),(1,1,1)],[(0,1),(1,1),(0,1)]],
                    2:[[(1,1),(1,1)]],
                    3:[[(0,1),(0,1),(0,1),(0,1)],[(1,1,1,1)]],
                    4:[[(1,1,0),(0,1,1)],[(0,1),(1,1),(1,0)]],
                    5:[[(0,1,1),(1,1,0)],[(1,0),(1,1),(0,1)]],
                    6:[[(0,1),(0,1),(1,1)],[(1,1,1),(0,0,1)],[(1,1),(1,0),(1,0)],[(1,0,0),(1,1,1)]],
                    7:[[(1,0),(1,0),(1,1)],[(0,0,1),(1,1,1)],[(1,1),(0,1),(0,1)],[(1,1,1),(1,0,0)]]
                }