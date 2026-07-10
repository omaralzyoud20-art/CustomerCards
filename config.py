from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4

PAGE_WIDTH, PAGE_HEIGHT = A4

CARDS_PER_PAGE = 5

PAGE_MARGIN_X = 1.2 * cm
PAGE_MARGIN_Y = 1.0 * cm

CARD_WIDTH = PAGE_WIDTH - PAGE_MARGIN_X * 2
CARD_HEIGHT = 5.0 * cm

CARD_SPACING = 0.35 * cm

FONT_NAME = "Amiri"

FONT_SIZE = 9
TITLE_SIZE = 9
VALUE_SIZE = 9

PHONE_SIZE = 10
AMOUNT_SIZE = 10

LINE_HEIGHT = 0.48 * cm

OUTPUT_FOLDER = "output"
INPUT_FILE = "شات اكسل.xlsx"
