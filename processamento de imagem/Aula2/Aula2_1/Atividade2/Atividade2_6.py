from PIL import Image
from random import randrange

img = Image.new('L', (256, 256), 'BLACK')

h , w = img.size

for i in range(h):
    for j in range(w):
        img.putpixel((i, j), 0)

for linha in range(int(h *0.25)):
    for coluna in range(int(w * 0.25)):
        img.putpixel((randrange(h), randrange(w)), 255)
        
img.show() 
img.save('img6.tif')
