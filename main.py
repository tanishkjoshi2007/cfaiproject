import os
print(os.listdir())

from PIL import Image, ImageDraw, ImageFont

text = input("Enter the text: ")

img = Image.new('RGB', (800, 400), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("handwriting.ttf", 32)
except:
    print("Font not found, using default")
    font = ImageFont.load_default()

draw.text((20, 50), text, fill=(0, 0, 0), font=font)

img.save("output.png")

print("Saved as output.png")