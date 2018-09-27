from PIL import Image

imglenna = Image.open('img.jpg')
imglennaCinza = imglenna.convert('L')
imglennaCinza.show()

imgPassaFaixa = Image.new('L', (imglennaCinza.size[0], imglennaCinza.size[1]), 'BLACK')
imgPassaAlta = Image.new('L', (imglennaCinza.size[0], imglennaCinza.size[1]), 'BLACK')
imgPassaBaixa = Image.new('L', (imglennaCinza.size[0], imglennaCinza.size[1]), 'BLACK')
img = Image.new('L', (imglennaCinza.size[0] + 2, imglennaCinza.size[1] + 2), 'BLACK')

h = imglennaCinza.size[0]
w = imglennaCinza.size[1]

for i in range(h):
    for j in range(w):
        X = imglennaCinza.getpixel((i, j))
        img.putpixel((i + 1, j + 1), X)

mascaraBaixa = ([1,1,1],[1,1,1],[1,1,1])
mascaraAlta = ([-1, -1, -1], [0, 0, 0], [1, 1, 1])
mascaraFaixa = ([0, -1, 0], [-1, 5, -1], [0, -1, 0])


def PassaAlto(height, width):
    T = img.getpixel((height, width)) * mascaraAlta[1][1]
    X1 = img.getpixel((height + 1, width + 1)) * mascaraAlta[2][2]
    X2 = img.getpixel((height - 1, width + 1)) * mascaraAlta[0][0]
    X3 = img.getpixel((height + 1, width)) * mascaraAlta[2][1]
    X4 = img.getpixel((height - 1, width)) * mascaraAlta[0][1]
    X5 = img.getpixel((height, width + 1)) * mascaraAlta[1][2]
    X6 = img.getpixel((height, width - 1)) * mascaraAlta[1][0]
    X7 = img.getpixel((height - 1, width - 1)) * mascaraAlta[0][0]
    X8 = img.getpixel((height + 1, width - 1)) * mascaraAlta[2][0]
    M = int((T + X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8))
    return M

def PassaBaixa(height, width):
    T = img.getpixel((height, width)) * mascaraBaixa[1][1]
    X1 = img.getpixel((height + 1, width + 1)) * mascaraBaixa[2][2]
    X2 = img.getpixel((height - 1, width + 1)) * mascaraBaixa[0][0]
    X3 = img.getpixel((height + 1, width)) * mascaraBaixa[2][1]
    X4 = img.getpixel((height - 1, width)) * mascaraBaixa[0][1]
    X5 = img.getpixel((height, width + 1)) * mascaraBaixa[1][2]
    X6 = img.getpixel((height, width - 1)) * mascaraBaixa[1][0]
    X7 = img.getpixel((height - 1, width - 1)) * mascaraBaixa[0][0]
    X8 = img.getpixel((height + 1, width - 1)) * mascaraBaixa[2][0]
    M = int((T + X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8))
    return M

def PassaFaixa(height, width):
    T = img.getpixel((height, width)) * mascaraFaixa[1][1]
    X1 = img.getpixel((height + 1, width + 1)) * mascaraFaixa[2][2]
    X2 = img.getpixel((height - 1, width + 1)) * mascaraFaixa[0][0]
    X3 = img.getpixel((height + 1, width)) * mascaraFaixa[2][1]
    X4 = img.getpixel((height - 1, width)) * mascaraFaixa[0][1]
    X5 = img.getpixel((height, width + 1)) * mascaraFaixa[1][2]
    X6 = img.getpixel((height, width - 1)) * mascaraFaixa[1][0]
    X7 = img.getpixel((height - 1, width - 1)) * mascaraFaixa[0][0]
    X8 = img.getpixel((height + 1, width - 1)) * mascaraFaixa[2][0]
    M = int((T + X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8))
    return M

    
for height in range(1, h + 1):
    for width in range(1, w + 1):
        mAlta =PassaAlto(height, width)
        mBaixa = PassaBaixa(height, width)
        mFaixa = PassaFaixa(height, width)
        imgPassaAlta.putpixel((height - 1, width - 1), mAlta)
        imgPassaBaixa.putpixel((height - 1, width - 1), mBaixa)
        imgPassaFaixa.putpixel((height - 1, width - 1), mFaixa)
       
imgPassaAlta.show()
imgPassaBaixa.show()
imgPassaFaixa.show()