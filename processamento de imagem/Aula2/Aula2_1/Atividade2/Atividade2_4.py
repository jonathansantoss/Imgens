from PIL import Image

img = Image.new('L', (256, 256), 'BLACK')

h , w = img.size

for i in range(h):
    for j in range(w):
        img.putpixel((i, j), 0)

col = 0
for linha in range(h-1,0,-1):
    for coluna in range(0, col):
        img.putpixel((linha, coluna), 255)
        
    col = col + 1

img.show() 
img.save('img4.tif')