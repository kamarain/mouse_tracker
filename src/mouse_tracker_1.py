# Computer scientist's tracker
#
#  * Does not care about physics, i.e. the tracker can
#    move instantaneously anywhere (teleportation in sci-fi
#    or apparation in Harry Potter books
#
import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np
import time

# Tracker settings
f_t = 1/5 # tracker frame rate

# Environment initialization
run_time = 10 # in seconds
x_m, y_m = +5,+5 # mouse start point
x_t, y_t = -5,-5 # tracker start point

# Make "environment"
fig = plt.figure()
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.ion()
plt.show()

# Plot inital tracker
old_point, = plt.plot(x_t,y_t,'rx')

# Handler to get mouse coordinates
def mouse_move(event):
    global x_m, y_m
    if event.xdata: # Check Null (outside axes)
        x_m, y_m = event.xdata, event.ydata
plt.connect('motion_notify_event', mouse_move)

# Tracker loop (run on the frame rate f_t)
start_time = time.time()
while time.time()-start_time < run_time:
    old_point.remove()

    # Calculate new tracker point: apparition
    x_t, y_t = x_m, y_m
    
    old_point, = plt.plot(x_t,y_t,'rx')
    plt.draw()
    plt.pause(f_t)
