import numpy
from PIL import Image

image=Image.new('RGB',(200,200))
im=image.load()

for i in range(0,50):
    for j in range(0,50):
        im[i,j]=(255,255,255)
    for j in range(101, 150):
        im[i, j] = (255, 255, 255)
for i in range(101,150):
    for j in range(0,50):
        im[i,j]=(255,255,255)
    for j in range(101,150):
        im[i,j]=(255,255,255)
for i in range(51,100):
    for j in range(51,100):
        im[i,j]=(255,255,255)
    for j in range(151,200):
        im[i,j]=(255,255,255)
for i in range(151,200):
    for j in range(51,100):
        im[i,j]=(255,255,255)
    for j in range(151,200):
        im[i,j]=(255,255,255)

image.save('test.png')
image.show('test.png')