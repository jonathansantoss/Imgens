from PIL import Image
import math

imglenna = Image.open('Lenna.png')
imgLennaCinza = imglenna.convert('L')
imgLennaCinza.show()

h, w = imgLennaCinza.size

img = Image.new('L', (1000, 1000) , 'BLACK')
img2 = Image.new('L', (int((w)*1.5), int((h)*1.5)) , 'BLACK')  


def posicao(height, width):
    tupla = []
    D1 = math.sqrt((math.pow(img2.getpixel((height, width)), 2)) + (math.pow(img2.getpixel((height - 1, width + 1)), 2)))
    D2 = math.sqrt((math.pow(img2.getpixel((height, width)), 2)) + (math.pow(img2.getpixel((height + 1, width)), 2)))
    D3 = math.sqrt((math.pow(img2.getpixel((height, width)), 2)) + (math.pow(img2.getpixel((height, width + 1)), 2)))
    D4 = math.sqrt((math.pow(img2.getpixel((height, width)), 2)) + (math.pow(img2.getpixel((height -1, width)), 2)))
    D5 = math.sqrt((math.pow(img2.getpixel((height, width)), 2)) + (math.pow(img2.getpixel((height, width - 1)), 2)))
    D6 = math.sqrt((math.pow(img2.getpixel((height, width)), 2)) + (math.pow(img2.getpixel((height-1, width - 1)), 2)))
    D7 = math.sqrt((math.pow(img2.getpixel((height, width)), 2)) + (math.pow(img2.getpixel((height+1, width - 1)), 2)))
    #D8 = math.sqrt((math.pow(img2.getpixel((height, width)), 2)) + (math.pow(img2.getpixel((height, width + 1)), 2)))
    
    
    # X7 = img.getpixel((height - 1, width - 1)) * mascaraAlta[0][0]
    # X8 = img.getpixel((height + 1, width - 1)) * mascaraAlta[2][0]
    # M = int((T + X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8))
    
    
    maior = D1
    
    tupla.insert(0, D1)
    tupla.insert(1, D2)
    tupla.insert(2, D3)
    
    for k in range(len(tupla)):
        if tupla[k] < maior:
            maior = tupla[k] 
    
    return maior


for linha in range(0, h):
    for coluna in range(0, w):
        pixel = imgLennaCinza.getpixel((coluna, linha))
        img2.putpixel((int(coluna  *1.5)   , int(linha * 1.5)), pixel)
        
img2.show()
img2.save('img77.png')
        
for linha in range(1, h):
    for coluna in range(1, w):
        #pixel = int(posicao(coluna, linha))
        pixel =img2.getpixel((coluna, linha))
        Y = int(coluna * math.sin(45) + linha * math.cos(45))
        X = int((coluna * math.cos(45) - linha * math.sin(45)))
        # pixel = int(posicao(X,Y ))
        # if (X > 0 & X < 512) & (Y < 512):
        
        #DY = math.sqrt((math.pow((coluna - X), 2)) + (math.pow(linha -Y, 2)))
               
        if X < 0:
            X = 500 + X
            img.putpixel((int(X / 2), int(Y / 2)), pixel)
            
        else:
            X = 500 + X
            img.putpixel((int(X / 2), int(Y / 2)), pixel)
        
img.show()
img.save('img1.png')
