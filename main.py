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
    return [width, length]

country_dimensions = []
for i in range(num_of_countries):
    loc = local_country()
    country_dimensions.append(loc)
    
print('------------------------------------------------------------------------------')
for i in country_dimensions:
    print('Width: {}, Length: {}'.format(i[0],i[1]))
    
print('\nRendering...')
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

'''
---------------------------------------------
Put rendering code under here, but before arcade.finish_render()
'''

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()
