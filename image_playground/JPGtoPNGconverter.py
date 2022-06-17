from ast import arg
import os
from sys import argv
from PIL import Image # Install Pillow

folder = argv[1]
new_folder = argv[2]

if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    
for filename in os.scandir(folder):
    if filename.is_file():
        img = Image.open(filename.path)
        file = os.path.splitext(filename.name)[0]
        img.save(f'{new_folder}/{file}.png', 'png')

print('Converted!!!')