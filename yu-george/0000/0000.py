'''
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。
Author: George Yu
'''

NOTIFS = 4

from PIL import Image, ImageFont, ImageDraw

while True:
    imgSrc = input('Input the source of the image file: ')
    if not imgSrc:
        imgSrc = 'resources/0000/original.jpg'
    try:
        avatar = Image.open(imgSrc)
    except FileNotFoundError:
        print('The image file could not be found!')
    break

width, height = avatar.size

if width != height:
    print('Warning: The image is not a perfect square, the output might not be accurate.')

draw = ImageDraw.Draw(avatar)

ref = min(width, height)
size = ref * 0.26
padding = size * 1.18
posX = width - padding
posY = padding - size
tPosX = posX * 1.09
tPosY = posY * 1.82

font = ImageFont.truetype('resources/0000/HelveticaNeue.otf', int(size*0.9))

draw.ellipse((posX, posY, posX+size, posY+size), fill='red')
draw.text((tPosX, tPosY), str(NOTIFS), (255,255,255), font=font)

avatar.save('output.jpg')
