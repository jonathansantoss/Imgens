from PIL import Image

img = Image.new('L', (8,8), 'BLACK')

h , w = img.size

for i in range(h):
    for j in range(w):
        img.putpixel((i, j), 0)

for linha in range(h):
    for coluna in range(w):
        if ( (linha + coluna) % 2)  == 0:
            img.putpixel((linha,coluna), 0)
        else:
            img.putpixel((linha,coluna), 255)
        
img.show() 
img.save('img9.tif')