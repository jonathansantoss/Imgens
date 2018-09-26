from PIL import Image

imagem = Image.open('img10.png')
imagemGray = imagem.convert('L')

imagemGray.show()

w = imagemGray.size[1]
h = imagemGray.size[0]

img = Image.new( 'L', (imagemGray.size[0],imagemGray.size[1]), "black") # Cria uma imgem em tonz de cinza

T = 127 # Threshold

for i in range(h):
    for j in range(w):
        x = imagemGray.getpixel((i, j))
        if x > T:
            img.putpixel((i, j), 255)
        else:
            img.putpixel((i , j), 0)

img.save('img10T127.png')            
img.show();