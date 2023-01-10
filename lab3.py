from PIL import Image, ImageDraw
import math
image = Image.new('RGBA', (960, 960), (255, 255, 255))
imageDraw = ImageDraw.Draw(image)
angle = math.radians(130)
with open("D:\Programms\DS2.txt", "r") as file:
    for line in file:
        coordinates = line.split()
        i = int(coordinates[0]) - 480
        j = int(coordinates[1]) - 480
        x = math.cos(angle) * i - math.sin(angle) * j
        y = math.sin(angle) * i + math.cos(angle) * j
        imageDraw.line((x + 480, y + 480, x + 481, y + 481),
        fill=(0, 190, 255))
image.show()
image.save('result.png')