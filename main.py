import turtle as turtle_module
import random

tim = turtle_module.Turtle()
color_list = [(240, 232, 214), (223, 159, 72), (50, 95, 58), (242, 201, 48), (61, 123, 173), (180, 64, 53),
              (219, 174, 197), (171, 173, 46), (44, 49, 96), (210, 90, 58), (181, 55, 59), (207, 165, 186),
              (130, 160, 186), (74, 131, 187), (37, 45, 80), (148, 169, 154), (243, 202, 7), (40, 82, 50),
              (189, 80, 86), (229, 174, 165), (176, 189, 214), (32, 54, 41), (110, 139, 118), (49, 42, 24),
              (179, 199, 185), (76, 142, 173), (57, 42, 53), (171, 199, 207), (97, 46, 65), (130, 38, 26),
              (75, 75, 30), (41, 72, 79)]
turtle_module.colormode(255)
DOT_SIZE = 20
PACE = 50


def determine_start_position(x_dots, y_dots):
    """Takes number of dots for both 'X' and 'Y' axes as inputs and determines the start position of
    the painting."""
    tim.speed(0)
    tim.penup()
    tim.hideturtle()
    position_x = int(-x_dots * PACE / 2)
    position_y = int(-y_dots * PACE / 2)
    tim.goto(position_x, position_y)
    y_movements(position_x, x_dots, position_y, y_dots)


def x_movements(initial_pos, dots_x):
    """Takes the start position and number of horizontal dots the user needs as inputs; and plots
    the dots using random colours."""
    final_x_coordinate = initial_pos + (dots_x * PACE) - 1
    end_x = False
    while not end_x:
        new_color = random.choice(color_list)
        tim.dot(DOT_SIZE, new_color)
        tim.penup()
        tim.forward(PACE)
        if tim.xcor() > final_x_coordinate:
            end_x = True


def y_movements(pos_x, dots_x, pos_y, dots_y):
    """Takes the start positions for both X and Y axes and number of dots the user needs for both axes;
    and coordinates the plotting of dots on both axes."""
    y_coordinate = pos_y
    final_y_coordinate = y_coordinate + (dots_y * PACE) - 1
    end_painting = False
    while not end_painting:
        tim.setx(pos_x)
        x_movements(pos_x, dots_x)
        pos_y += PACE
        tim.sety(pos_y)
        if tim.ycor() > final_y_coordinate:
            end_painting = True


determine_start_position(10, 10)





























screen = turtle_module.Screen()
screen.exitonclick()










# import colorgram
#
# colors = colorgram.extract("image.jpg", 35)

#for color in colors:
#    r = color.rgb[0]
#    g = color.rgb[1]
#    b = color.rgb[2]
#    color_tuple = (r, g, b)
#    new_list.append(color_tuple)
#print(new_list)

