from PIL import Image

img = Image.new('L', (256,256), 'BLACK')

h , w = img.size

for i in range(h):
    for j in range(w):
        img.putpixel((int(i /2)+60, int(j /2)+60 ), 255)

img.show() 
img.save('img1.tif')