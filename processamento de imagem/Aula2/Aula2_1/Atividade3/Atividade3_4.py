from PIL import Image
from random import randrange

imagemLenna = Image.open('Lenna.png')
imagemLennaCinza = imagemLenna.convert('L')

h , w = imagemLennaCinza.size

for i in range(int((h * 0.30))):
    for j in range(int((w * 0.30))):
        imagemLennaCinza.putpixel((randrange(h), randrange(w)) , 255)

imagemLennaCinza.show()  
imagemLennaCinza.save('f5.png')  
