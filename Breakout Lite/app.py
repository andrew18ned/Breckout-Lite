from tkinter import Tk, Canvas
from PIL import Image, ImageTk

from game.game import Game
from settings import *

tk = Tk()

# Ініціалізація вінка Tkinter
tk.title(GAME_NAME)
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

# Ініціалізація Canvas, на якім ми можемо малювати
canvas = Canvas(tk, width=WIDTH,
                height=HEIGHT, highlightthickness=0)
bg = ImageTk.PhotoImage(Image.open('backgraund.jpg').resize((WIDTH, HEIGHT)))
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=bg)

canvas.pack()
tk.update()

# Імпортуємо налаштування в словник, розуміючий класом гри
settings = {
    'ball_size': BALL_SIZE,
    'ball_color': BALL_COLOR,
    'puddle_width': PUDDLE_WIDTH,
    'puddle_height': PUDDLE_HEIGHT,
    'puddle_color': PUDDLE_COLOR,
    'score_size': SCORE_SIZE,
    'score_color': SCORE_COLOR,
    'end_text_size': END_TEXT_SIZE,
    'end_text_color': END_TEXT_COLOR
}

# Ініціалізація гри
game = Game(tk, canvas, settings)

# Запуск гри
if __name__ == '__main__':
    game.run()