import turtle

screen = turtle.Screen()
screen.setup(width=750, height=500)
screen.title("Indian States Game")
image = "india1.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()