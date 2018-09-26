from PIL import Image


imglenna = Image.open('Lenna.png')
imglennaCinza = imglenna.convert('L')
imglennaCinza.show()

img = Image.new('L', (imglennaCinza.size[0], imglennaCinza.size[1]), 'BLACK')


h = imglennaCinza.size[0]
w = imglennaCinza.size[1]