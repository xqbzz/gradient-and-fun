from tkinter import filedialog
from PIL import Image

# Открыть окно для выбора файла
file_path = filedialog.askopenfilename() 
if not file_path:
    # если не выбрал, то выход
    exit()

# Открыть файл картинки и сконвертировать её в двоичный формат
with Image.open(file_path) as img:
    bin_img = img.convert("1") 

# Показать изображение
bin_img.show()
