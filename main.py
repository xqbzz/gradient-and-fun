import random
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import time

def main():
    # Сделать окно
    root = tk.Tk()
    root.title("Gradient")

    # Параметры
    width, height = 800, 600
    
    # Цвет
    color1 = (255, 0, 0)
    color2 = (0, 255, 0)
    steps = 50

    # Create initial image with gradient
    gradient_image = create_gradient_image(width, height, color1, color2, steps)

    # Set up gradient position
    gradient_position = [0.5]

    # Set up damping
    damping = 10

    # Set up mouse position
    mouse_position = [None, None]

    # Set up initial image
    photo_image = ImageTk.PhotoImage(gradient_image)
    canvas = tk.Canvas(root, width=width, height=height)
    gradient_id = canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)
    canvas.pack()

    # Set up FPS counter
    fps_text = tk.StringVar(value="FPS: 0")
    fps_label = tk.Label(root, textvariable=fps_text)
    fps_label.pack()

    # Start update loop
    update(canvas, gradient_image, gradient_id, photo_image, fps_text, time.time(), mouse_position, gradient_position, damping, color1, color2, steps)

    # Start tkinter main loop
    root.mainloop()
    
    # Close the tkinter window properly
    root.destroy()


def create_gradient_image(width, height, color1, color2, steps):
    gradient_image = Image.new("RGB", (width, height), color1)

    for i in range(steps):
        progress = i / (steps-1)
        r = int(color1[0] * (1 - progress) + color2[0] * progress)
        g = int(color1[1] * (1 - progress) + color2[1] * progress)
        b = int(color1[2] * (1 - progress) + color2[2] * progress)
        draw = ImageDraw.Draw(gradient_image)
        y0 = int((height * i) / steps)
        y1 = int((height * (i+1)) / steps)
        draw.rectangle((0, y0, width, y1), fill=(r, g, b))

    return gradient_image


def update(canvas, gradient_image, gradient_id, photo_image, fps_text, start_time, mouse_position, gradient_position, damping, color1, color2, steps):
    # Calculate FPS
    elapsed_time = max(0.0001, time.time() - start_time)
    fps = int(1 / elapsed_time)
    fps_text.set(f"FPS: {fps}")

    # Redraw gradient image with updated position
    updated_gradient_image = set_gradient_position(gradient_image.copy(), gradient_position, color1, color2, steps, damping)
    updated_photo_image = ImageTk.PhotoImage(updated_gradient_image)
    canvas.itemconfig(gradient_id, image=updated_photo_image)

    # Update the gradient position based on mouse movement
    canvas.bind("<Motion>", lambda event: set_mouse_position(event, canvas, gradient_position))

    # Schedule the next update
    canvas.after(20, update, canvas, updated_gradient_image, gradient_id, updated_photo_image, fps_text, time.time(), mouse_position, gradient_position, damping, color1, color2, steps)


def set_gradient_position(gradient_image, gradient_position, color1, color2, steps, damping):
    # Calculate new gradient position
    x = int(gradient_position[0] * gradient_image.width)
    
    # Draw gradient with updated position
    draw = ImageDraw.Draw(gradient_image)
    for i in range(steps):
        progress = i / (steps-1)
        r = int(color1[0] * (1 - progress) + color2[0] * progress)
        g = int(color1[1] * (1 - progress) + color2[1] * progress)
        b = int(color1[2] * (1 - progress) + color2[2] * progress)
        y0 = int((gradient_image.height * i) / steps) - x // damping
        y1 = int((gradient_image.height * (i+1)) / steps) - x // damping
        draw.rectangle((0, y0, gradient_image.width, y1), fill=(r, g, b))

    return gradient_image


def set_mouse_position(event, canvas, gradient_position):
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    gradient_position[0] = x / canvas.winfo_width()

if __name__ == "__main__":
    main()

