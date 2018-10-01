from PIL import Image

imagemLenna = Image.open('Lenna.png')
imagemLennaCinza = imagemLenna.convert('L')
imagemLennaCinza.save('f1.png')

h , w = imagemLenna.size

for linha in range(h):
    for coluna in range(w):
        if coluna % 2 == 0:
            imagemLennaCinza.putpixel((linha,coluna), 255)
        
imagemLennaCinza.show() 
imagemLennaCinza.save('f2.png')