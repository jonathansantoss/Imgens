from PIL import Image

imglenna = Image.open('images.jpg')
imglennaCinza = imglenna.convert('L')
imglennaCinza.show()

imgMascara1 = Image.new('L', (imglennaCinza.size[0], imglennaCinza.size[1]), 'BLACK')
imgMascara2 = Image.new('L', (imglennaCinza.size[0], imglennaCinza.size[1]), 'BLACK')
imgMascara3 = Image.new('L', (imglennaCinza.size[0], imglennaCinza.size[1]), 'BLACK')
img = Image.new('L', (imglennaCinza.size[0] + 4, imglennaCinza.size[1] + 4), 'BLACK')

h = imglennaCinza.size[0]
w = imglennaCinza.size[1]

for i in range(h):
    for j in range(w):
        X = imglennaCinza.getpixel((i, j))
        img.putpixel((i + 1, j + 1), X)


def Mascara1(height, width):
    T = img.getpixel((height, width)) 
    X3 = img.getpixel((height + 1, width)) 
    X4 = img.getpixel((height - 1, width)) 
    X5 = img.getpixel((height, width + 1)) 
    X6 = img.getpixel((height, width - 1))  
    M = int((T + X3 + X4 + X5 + X6) / 5)
    return M


def Mascara2(height, width):
    T = img.getpixel((height, width)) 
    X1 = img.getpixel((height + 1, width + 1)) 
    X2 = img.getpixel((height - 1, width + 1)) 
    X3 = img.getpixel((height + 1, width)) 
    X4 = img.getpixel((height - 1, width)) 
    X5 = img.getpixel((height, width + 1)) 
    X6 = img.getpixel((height, width - 1)) 
    X7 = img.getpixel((height - 1, width - 1)) 
    X8 = img.getpixel((height + 1, width - 1)) 
    M = int((T + X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8) / 9)
    return M


def Mascara3(height, width):
    T = img.getpixel((height, width)) 
    X1 = img.getpixel((height + 1, width + 1)) 
    X2 = img.getpixel((height - 1, width + 1)) 
    X3 = img.getpixel((height + 1, width)) 
    X4 = img.getpixel((height - 1, width)) 
    X5 = img.getpixel((height, width + 1)) 
    X6 = img.getpixel((height, width - 1)) 
    X7 = img.getpixel((height - 1, width - 1)) 
    X8 = img.getpixel((height + 1, width - 1)) 
    
    X9 = img.getpixel((height + 2, width + 2)) 
    X10 = img.getpixel((height - 2, width + 2)) 
    X11 = img.getpixel((height + 2, width)) 
    X12 = img.getpixel((height - 2, width)) 
    X13 = img.getpixel((height, width + 2)) 
    X14 = img.getpixel((height, width - 2)) 
    X15 = img.getpixel((height - 2, width - 2)) 
    X16 = img.getpixel((height + 2, width - 2))
    
    M = int((T + X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 + X9 + X10 + X11 + X12 + X13 + X14 + X15 + X16) / 17)
    return M

    
for height in range(2, h + 2):
    for width in range(2, w + 2):
        m1 = Mascara1(height, width)
        m2 = Mascara2(height, width)
        m3 = Mascara3(height, width)
        imgMascara1.putpixel((height - 2, width - 2), m1)
        imgMascara2.putpixel((height - 2, width - 2), m2)
        imgMascara3.putpixel((height - 2, width - 2), m3)
       
imgMascara1.show()
imgMascara2.show()
imgMascara3.show()
