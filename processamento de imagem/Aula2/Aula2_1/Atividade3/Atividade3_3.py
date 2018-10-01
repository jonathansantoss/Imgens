from PIL import Image

imagemF2 = Image.open('f2.png')
imagemF3 = Image.open('f3.png')

h , w = imagemF2.size

img = Image.new('L', (h, w), 'BLACK')

for linha in range(h):
    for coluna in range(w):
        pixel = imagemF2.getpixel((linha,coluna)) - imagemF3.getpixel((linha,coluna))
        img.putpixel((linha,coluna), pixel)
        
img.show() 
img.save('f4.png')