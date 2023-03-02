from PIL import Image
import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename() 
    img = Image.open(file_path)
    img = img.convert("1")
    binary_data = list(img.getdata())
    width, height = img.size 
    binary_data = [binary_data[i:i+width] for i in range(0, len(binary_data), width)]
    binary_data = [[1 if pixel else 0 for pixel in row] for row in binary_data]
    draw_image(binary_data)

def draw_image(binary_data):
    width = len(binary_data[0])
    height = len(binary_data)
    window = tk.Tk()   
    window.geometry('{}x{}'.format(width*2, height*2))   
    window.title('Binary Image')

    canvas = tk.Canvas(window)  
    canvas.pack(fill="both", expand=True)

    for row in binary_data:
        for pixel in row:
            if pixel == 1:
                canvas.create_rectangle(row.index(pixel)*2, binary_data.index(row)*2, (row.index(pixel)+1)*2, (binary_data.index(row) + 1)*2, fill='black')
            else:
                canvas.create_rectangle(row.index(pixel)*2, binary_data.index(row)*2, (row.index(pixel)+1)*2, (binary_data.index(row) + 1)*2, fill='white')
    window.mainloop()

if __name__ == '__main__':
    open_file()
