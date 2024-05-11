from checkers.point import Point
from checkers.enums import CheckerType, SideType

PLAYER_SIDE = SideType.WHITE

X_SIZE = Y_SIZE = 8
CELL_SIZE = 75

ANIMATION_SPEED = 4

MAX_PREDICTION_DEPTH = 3

BORDER_WIDTH = 2 * 2

FIELD_COLORS = ['#E7CFA9', '#927456']
HOVER_BORDER_COLOR = '#54b346'
SELECT_BORDER_COLOR = '#944444'
POSIBLE_MOVE_CIRCLE_COLOR = '#944444'

MOVE_OFFSETS = [
    Point(-1, -1),
    Point( 1, -1),
    Point(-1,  1),
    Point( 1,  1)
]

WHITE_CHECKERS = [CheckerType.WHITE_REGULAR, CheckerType.WHITE_QUEEN]
BLACK_CHECKERS = [CheckerType.BLACK_REGULAR, CheckerType.BLACK_QUEEN]