# mouse_tracker
Code for various trackers that track using the mouse pointer. The idea is to illustrate control in robotics.

## Tracker 1 - No physics (computer scientist's tracker)
The first tracker is only limited by its frame rate f (defined as "times per second" i.e. 1/s). Every time the tracker is evaluted its new location
is set to the most recent location of the mouse pointer, i.e.

<img src="https://render.githubusercontent.com/render/math?math=\mathbf{x}^t = (x^t,y^t) = (x_m^t,y_m^t)">

where x_m and y_m are the current locations of the mouse pointer. You can test this tracker by running

```
~> python mouse_tracker_1.py
```

Does it look realistic movement? No, this tracker is like Harry Potter book "apparation" or teleportation where your tracker does not obey any rules of physics, but can instantaenously jump anywhere in the map.
