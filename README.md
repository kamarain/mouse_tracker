# mouse_tracker
Code for various trackers that track using the mouse pointer. The idea is to illustrate control in robotics.

## Tracker 1 - What a programmer would implement without any knowledge about robotics
The first tracker is only limited by its frame rate f (defined as "times per second" i.e. 1/s). Every time the tracker is evaluted its new location
is set to the most recent location of the mouse pointer, i.e. **x**^(t) = (x^(t),y^(t)) = (x_m, y_m)

<img src="https://render.githubusercontent.com/render/math?math=\mathbf{x}^t = (x^t,y^t) = (x_m^t,y_m^t)">

where x_m^t and y_m^t are the current locations of the mouse pointer.
