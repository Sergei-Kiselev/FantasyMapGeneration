import arcade
import fcg_dont_print as fdp
import random
import math

num_of_countries = random.choice(range(2,6))

# Set constants for the screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 675
SCREEN_AREA = SCREEN_WIDTH * SCREEN_HEIGHT

max_large_size = round(SCREEN_AREA / num_of_countries)
max_medium_size = round((max_large_size / 4) * 3)
max_small_size = round(max_large_size / 2)

min_wl_ratio = 1/4

country_profiles = []

def local_country():
    results = fdp.fantasy_country()
    print(results)
    if results[0] == "large":
        size = random.randint(max_medium_size, max_large_size)
        w_to_l = random.uniform(min_wl_ratio,1)
        w_to_l = round(w_to_l,2)
        print(w_to_l)
    elif results[0] == "medium":
        size = random.randint(max_small_size, max_medium_size)
        w_to_l = random.uniform(min_wl_ratio,1)
        w_to_l = round(w_to_l,2)
        print(w_to_l)
    elif results[0] == "small":
        size = random.randint(max_small_size/2, max_small_size)
        w_to_l = random.uniform(min_wl_ratio,1)
        w_to_l = round(w_to_l,2)
        print(w_to_l)
    else:
        print('Something has gone wrong.')

    print(size)
    
    r_eq_side = size / w_to_l
    length = math.sqrt(r_eq_side)
    print(length)
    width = size / length
    print(width)

'''
w * l = 100
w = 0.5 * l
0.5 * l^2 = 100

length^2 = size / wlratio
'''
local_country()
FILLED_PIXEL_AREAS = []

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Countries")

# Set the background color to white.
# For a list of named colors see:
# http://arcade.academy/arcade.color.html
# Colors can also be specified in (red, green, blue) format and
# (red, green, blue, alpha) format.
arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()


# Draw the face
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# Draw the right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the left eye
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# Draw the smile
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()
