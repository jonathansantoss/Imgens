from PIL import Image

imagemLenna = Image.open('Lenna.png')
imagemLennaCinza = imagemLenna.convert('L')

h , w = imagemLenna.size

for linha in range(h):
    for coluna in range(w):
        if linha % 2 == 0:
            imagemLennaCinza.putpixel((linha, coluna), 255)
        
imagemLennaCinza.show() 
imagemLennaCinza.save('f3.png')
