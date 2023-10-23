"""Draw a basic image of our solar system!

I broke up a complex function in my draw_line function because it was required to find a starting 
position based on a given angle. Instead I created separate functions to find the starting x and y values 
based on the given angle and then called those functions in the draw_line function.
I tried something fun with the random module. I used randrange() and randint() to place many stars of 
random sizes in random places on the screen. I also used a for loop in my main function to create the repeated 
sun rays because the rays are almost identical except for position and angle. In the for loop, I was able to 
change the angle consistently over each loop such that the only change I had to consider was the changing
angle and my program would create a different starting position for each ray. Finally, I used a for/in range 
loop with a parameter of a list of lists to create planets because then each loop would call the indexes 
of the bigger list to determine which planet to draw, then the list held by each index in the bigger list
can be used to create the specific planet which it's different dimensions.
"""

__author__ = "730648328"

from turtle import Turtle, colormode, done
import random
colormode(255) 


def draw_rectangle(turtle: Turtle, x: float, y: float, width: float, height: float, r: float, g: float, b: float) -> None:
    """Draw a rectangle with given parameters."""
    turtle.penup()
    turtle.color(r, g, b)
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()
    turtle.begin_fill()
    i: int = 0
    while i < 2:
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
        i += 1
    turtle.end_fill()


def draw_full_circle(turtle: Turtle, x_center: float, y_center: float, rad: float, r: float, g: float, b: float) -> None:
    """Draw a circle with the given parameters."""
    turtle.penup()
    turtle.color(r, g, b)
    turtle.goto(x_center + rad, y_center)
    turtle.setheading(0.0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()


def create_stars(turtle: Turtle, x_center: float, y_center: float, rad: float, r: float, g: float, b: float) -> None:
    """Draw a star represented by an open white circle."""
    turtle.penup()
    turtle.color(r, g, b)
    turtle.goto(x_center + rad, y_center)
    turtle.setheading(0.0)
    turtle.pendown()
    turtle.circle(rad)


def determine_x(angle: float) -> float:
    """Determine the x value of the start of one of the sun's rays based on the rays angle."""
    x: int = 0
    if angle == 0:
        x = -150
    elif angle == 45:
        x = -165
    elif angle == 90:
        x = -210
    elif angle == 135:
        x = -255
    elif angle == 180:
        x = -270
    elif angle == 225:
        x = -255
    elif angle == 270:
        x = -210
    elif angle == 315:
        x = -165
    return x


def determine_y(angle: float) -> float:
    """Determine the y value of the start of one of the sun's rays based on the ray's angles."""
    y: int = 0
    if angle == 0:
        y = -170
    elif angle == 45:
        y = -125
    elif angle == 90:
        y = -110
    elif angle == 135:
        y = -125
    elif angle == 180:
        y = -170
    elif angle == 225:
        y = -215
    elif angle == 270:
        y = -230
    elif angle == 315:
        y = -215
    return y


def draw_line(turtle: Turtle, length: float, r: float, g: float, b: float, angle: float) -> None:
    """Draw a straight line based on the given values."""
    x: float = determine_x(angle)
    y: float = determine_y(angle)
    turtle.penup()
    turtle.color(r, g, b)
    turtle.goto(x, y)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(length)


def draw_planet(turtle: Turtle, val_list: list[float]) -> None:
    """Given a list, use the held values to create a circle."""
    draw_full_circle(turtle, val_list[0], val_list[1], val_list[2], val_list[3], val_list[4], val_list[5])


def main() -> None:
    """Draw the entire image!"""
    solaire: Turtle = Turtle()
    solaire.hideturtle()
    solaire.speed(150)
    image_w: float = 600
    image_h: float = 520
    """Draw the galaxy backdrop."""
    draw_rectangle(solaire, -300, 260, image_w, image_h, 30, 5, 60)
    for i in range(0, 100):
        create_stars(solaire, random.randrange(-290, 290), random.randrange(-230, 230), random.randint(1, 4,), 255, 255, 255)
    """Draw the sun."""
    draw_full_circle(solaire, -270, -230, 60, 255, 255, 0)
    angle_idx: float = 0.0
    for idx in range(0, 8):
        draw_line(solaire, 30, 255, 255, 0, angle_idx)
        angle_idx = angle_idx + 45
    """Draw the planets."""
    mercury: list[float] = [-140, -210, 15, 204, 102, 0]
    venus: list[float] = [-80, -163, 25, 153, 102, 51]
    earth: list[float] = [-100, -68, 30, 0, 153, 0]
    mars: list[float] = [30, -108, 19, 255, 0, 0]
    jupiter: list[float] = [0, -33, 48, 255, 204, 102]
    saturn: list[float] = [150, 15, 42, 255, 204, 255]
    uranus: list[float] = [100, 140, 31, 153, 204, 255]
    neptune: list[float] = [200, 145, 28, 51, 102, 255]
    pluto: list[float] = [260, 220, 9, 153, 153, 102]
    planet_list: list[list[float]] = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
    for elem in planet_list:
        draw_planet(solaire, elem)
    """Draw saturns ring."""
    draw_rectangle(solaire, 142, 60, 100, 8, 204, 0, 153)
    done()


if __name__ == "__main__":
    """Makes the main function usable on it's own."""
    main()