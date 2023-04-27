##This Script get 2 argument as image folder and outpot folder
##image folder must contain some picture with jpg format
##output folder will be create if doese not exist



import sys
import os
from PIL import Image


image_folder = sys.argv[1]
output_folder = sys.argv[2]


#check if new/ exist,if not create it

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print('all done!')
