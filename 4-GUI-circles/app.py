from tkinter import *
import time
from Ball import Ball

window = Tk()
window.title("Bounce Balls")
WIDTH = 500
HEIGHT = 500
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
volly_ball = Ball(canvas,0,0,100,3,2,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,8,7,"orange")

while True:
    volly_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)
window.mainloop()