#Edit multiple photos with the same edits to automate. Using Pillow install

from PIL import Image, ImageEnhance, ImageFilter
import os

path = "/Users/brian/Desktop/Test"
pathOut = "/Users/brian/Desktop/Edited"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

#Sharpen image quality, convert to grayscale
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

#Add contract based on the factor used
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)

    edit = enhancer.enhance(factor)


#Name and save edited pictures
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')