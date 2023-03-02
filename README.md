
# Gradient
This program creates a gradient image with two colors and a damping effect. The user can control the position of the gradient by moving the mouse.

## Requirements
- Python 3.x 
- tkinter 
- PIL 

## Usage 
Run `main()` to start the program. The window will open with the gradient image and an FPS counter at the bottom. Move your mouse to control the position of the gradient. 

## Code Overview 
The code consists of several functions: 
- `create_gradient_image()` creates an image with a two-color gradient, given two colors, width, height and number of steps. 
- `update()` is used to update the window every 20 milliseconds, calculating FPS and updating the position of the gradient based on mouse movement.  
- `set_gradient_position()` draws a new gradient image with updated position in each update loop.  
- `set_mouse_position()` sets up mouse position for each update loop.