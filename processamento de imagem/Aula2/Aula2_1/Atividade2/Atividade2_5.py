from PIL import Image

img = Image.new('L', (256, 256), 'BLACK')

h , w = img.size

for i in range(h):
    for j in range(w):
        img.putpixel((i, j), 0)

col = h
for linha in range(h-1,0,-1):
    for coluna in range(int(w - col), w):
        img.putpixel((linha, coluna), 255)
        
    col = col - 1

img.show() 
img.save('img5.tif')