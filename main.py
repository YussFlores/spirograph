import turtle as draw # turtle's alias will be "draw"
import random
draw.colormode(255)
def get_color():
    # get a random number teween 0 and 255, then convert all to tuple and return the tuple
    red = random.randint(0,255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

draw.speed('fastest') # draw circle inmediatly
def draw_spirograph(size_of_gap):
    for n in range(int(360 / size_of_gap)): #This will repeat the result of 360 / the parameter
        draw.color(get_color())
        draw.circle(100)
        draw.setheading(draw.heading() + size_of_gap) # Set the coordinates of next circle the current position
        # + parameter

draw_spirograph(5)
draw.exitonclick()






