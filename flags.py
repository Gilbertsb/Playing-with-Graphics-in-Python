# Gilbert SIBOMANA Cohort 2

#This program was made to show Flags of 3 countries(Congo brazaville, Niger, Guinea) in graphics
#I have used aluLib, to assist me to create all graphics stuff you will see, you can find more of this at http://projectpython.net/chapter19/


from aluLib import *

window_width = 1000
window_height = 600


def congo_brazaville():                        #Defining function that will holds all of our actions to create Congo's flag

    set_fill_color(1, 0.81, 0)                               # Setting a yellow color for incoming shape.
    draw_rectangle(0, 0, window_width, window_height)     # drawing a rectangle that has same size as window and the location is at 0,0.
    disable_stroke()                                      # Disabling stroke fro nice look

    set_fill_color(0, 0.58, 0.22)                            # Setting a green color for incoming shape
    draw_triangle(0, 0, 700, 0, 0, 600)                   # drawing our first triangle where x1 is at 0, and y1 is at 0
    disable_stroke()                                      # And x2 is 700 then y2 is at 0, lastly, x3 is at 0 and y3 is 600
                                                          # Disabled stroke just for nice look

    set_fill_color(0.93, 0.2, 0.25)                                  # Setting a red color for incoming shape
    draw_triangle(1000, 600, -115, 1000, 1000, 0)           # drawing our second triangle where x1 is at 1000, and y1 is at 1000
    disable_stroke()                                         # And x2 is -115 then y2 is at 1000, lastly, x3 is at 1000 and y3 is 0
                                                             # Disabled stroke just for nice look


  
def niger():                                   # Defining function that will holds all of our actions to create Niger's flag.

    rectangle_height = window_height / 3               # Dividing window's height into 3 parts

    set_fill_color(0.87, 0.32, 0.02)                                      # Setting an orange color for incoming shape
    draw_rectangle(0, 0, window_width,rectangle_height)               # drawing a rectangle that has same width as window and 1 of 3 of rectangle's heighr and located at 0,0.
    disable_stroke()                                                  # Stroke is disable fro nice look

    set_fill_color(0.87, 0.32, 0.02)                                   # Setting an orange color for incoming shape
    draw_circle(500, 300, 90)                                      # drawing a circle that is located at 500x and 300y and has 90 radius
    disable_stroke()                                               # Stroke is disabled fro nice look.

    set_fill_color(0.05, 0.60, 0.16)                                   # Setting a green color for incoming shape
    draw_rectangle(0, 400, window_width,rectangle_height)        # drawing a rectangle that has same width as window and 1 of 3 of rectangle's heighr and located at 0,400.
    disable_stroke()                                             # Stroke is disable fro nice look

    pass


def guinea():                                  # Defining function that will holds all of our actions to create Gunea's flag.

    rectangle_width = window_width / 3                 # Dividing window's width into 3 parts

    set_fill_color(0.75, 0.06, 0.04)                                     # Setting a red color for incoming shape
    draw_rectangle(0,0, rectangle_width, window_height)           # drawing a rectangle that has same height as window and 1 of 3 of rectangle's width and located is at 0,0.
    disable_stroke()                                              # Stroke is disable fro nice look

    set_fill_color(0.98, 0.81, 0.08)                                     # Setting a yellow color for incoming shape
    draw_rectangle(333, 0,rectangle_width, window_height)       # drawing a rectangle that has same height as window and 1 of 3 of rectangle's width and located at 333,0.
    disable_stroke()                                            # Stroke is disable fro nice look

    set_fill_color(0, 0.58, 0.37)                                # Setting a green color for incoming shape
    draw_rectangle(666, 0, rectangle_width, window_width)     # drawing a rectangle that has same height as window and 1 of 3 of rectangle's width and located at 666,0.
    disable_stroke()                                          # Stroke is disable fro nice look

    pass


start_graphics(niger, width=window_width, height=window_height)     # Within this line of code we are starting graphic by calling our functions to draw flags
                                                                     # And mention width and height of window
