# Importing Image from PIL package
from PIL import Image, ImageMath
import math
import os



#overly coplicated tuple adder
def tupleAdd(tup1, tup2):
    newTup = ()
    if(len(tup1) >= len(tup2)):
        for x in range(len(tup2)):
            newTup += (tup1[x] + tup2[x],)
        for x in range(len(tup2),len(tup1)):
            newTup += (tup1[x],)
        return newTup
    else:
        for x in range(len(tup1)):
            newTup += (tup1[x] + tup2[x],)
        for x in range(len(tup1),len(tup2)):
            newTup += (tup2[x],)
        return newTup

#overly complicated tuple subtracter
def tupleSub(tup1, tup2):
    newTup = ()
    if(len(tup1) >= len(tup2)):
        for x in range(len(tup2)):
            newTup += (tup1[x] - tup2[x],)
        for x in range(len(tup2),len(tup1)):
            newTup += (tup1[x],)
        return newTup
    else:
        for x in range(len(tup1)):
            newTup += (tup1[x] - tup2[x],)
        for x in range(len(tup1),len(tup2)):
            newTup += (tup2[x],)
        return newTup

#returns average value of the pixels suroudning the given currdinates
#has bounds checking
def avgPixel(image,x,y):
    rgbavg = image.getpixel((x,y))
    pixelCount = 1
    if(x != 0):
        rgbavg = tupleAdd(rgbavg, image.getpixel((x-1,y)))
        pixelCount += 1
    if(x != image.width-1):
        rgbavg = tupleAdd(rgbavg, image.getpixel((x+1,y)))
        pixelCount += 1
    if(y != 0):
        rgbavg = tupleAdd(rgbavg, image.getpixel((x,y-1)))
        pixelCount += 1
    if(y != 0):
        rgbavg = tupleAdd(rgbavg, image.getpixel((x,y+1)))
        pixelCount += 1
    return tuple(val//pixelCount for val in rgbavg)

#ignore
def main2():
    image = Image.open('1.jpg')
    for x in range(image.width-1):
        for y in range(image.height-1):
            rgb = image.getpixel((x,y))

            image.putpixel((x,y),(rgb[0]+50,rgb[1],rgb[2]))
    return image

#blurs image
def blur(image, val):
    for times in range(val):
        for x in range(image.width-1):
            for y in range(image.height-1):
                rgb = avgPixel(image,x,y)
                image.putpixel((x,y),(rgb[0],rgb[1],rgb[2]))
    return image

#inverts the image's colors
def invert(image):
    for x in range(image.width-1):
        for y in range(image.height-1):
            rgb = image.getpixel((x,y))
            image.putpixel((x,y),(255-rgb[0],255-rgb[1],255-rgb[2]))
    return image

#flips image vertically
def flipHalf(image):
    for x in range(image.width-1):
        for y in range((image.height-1)//2):
            rgb = image.getpixel((x,y))
            image.putpixel((image.width-1-x,image.height-1-y),rgb)
    return image

#helper fucnitno that gives the distance of two tuples
def distance(tup1, tup2):
    newt = tupleSub(tup1, tup2)
    squaredSum = 0
    for num in newt:
        squaredSum += num**2
    return int(math.sqrt(squaredSum))

#replaces a target color with a new color
def colorReplace(image,target,color):
    for x in range(image.width-1):
        for y in range(image.height-1):
            rgb = image.getpixel((x,y))
            if(distance(rgb[:3],target) < 50):
                image.putpixel((x,y),color+(255,))
    return image

#given a mask(black and white image) any place that the mask is black the
#correspondong pixel from the provided image will be copied over to the
#origionsl Image
def masker(image,copy,mask):
    for x in range(image.width-1):
        for y in range(image.height-1):
            if(distance(mask.getpixel((x,y)), (0,0,0)) < 20):
                image.putpixel((x,y),copy.getpixel((x,y)))
    return image

#chromaKey's a image with a background. Gets the color to be replaces from the
#oixel at (0,0) and replaces all pixels close to the same color with the background
def chromaKey(image,bg):
    key = image.getpixel((0,0))
    for x in range(image.width-1):
        for y in range(image.height-1):
            if(distance(image.getpixel((x,y)), key) < 20):
                image.putpixel((x,y),bg.getpixel((x,y)))
    return image

#given an image with an object infront of a background, an image of just the
#background, and a new background this fucntion replaces the background of the
#origional image with a new background
def backSub(image,bg,newBG):
    for x in range(image.width-1):
        for y in range(image.height-1):
            if(distance(image.getpixel((x,y)), bg.getpixel((x,y))) < 20):
                image.putpixel((x,y),newBG.getpixel((x,y)))
    return image

#edge detection functino that productes a grayscale output in which the whiter
#the pixels the more drastic an edge was detected
def edges(image):
    for x in range(image.width-2):
        for y in range(image.height-2):
            rgb = image.getpixel((x,y))
            rgb2 = image.getpixel((x+1,y+1))
            diff = abs(rgb[0]+rgb[1]+rgb[1]-rgb2[0]-rgb2[1]-rgb2[1])
            image.putpixel((x,y),(diff,diff,diff))
    return image
#hides a black and white image in a color image
def encode(image,hidden):
    for x in range(image.width-1):
        for y in range(image.height-1):
            rgb = image.getpixel((x,y))
            if (rgb[0]%2) == 1:
                image.putpixel((x,y),(rgb[0]-1,rgb[1],rgb[2]))

    for x in range(image.width-1):
        for y in range(image.height-1):
            rgbO = image.getpixel((x,y))
            rgbMes = hidden.getpixel((x,y))
            #bizzare logic in if likely needed to deal with photos that have
            #alpha channel but is easily avoided by not using images
            #with an alpha channel
            if (rgbMes[0]==0 and rgbMes[1]==0 and rgbMes[2]==0):
                image.putpixel((x,y),(rgbO[0]+1,rgbO[1],rgbO[2]))
    return image

#decodes a color image into a hidden black and white image
def decode(image):
    output = Image.new("RGB",(image.width,image.height))
    for x in range(image.width-1):
        for y in range(image.height-1):
            rgbMes = image.getpixel((x,y))
            if((rgbMes[0]%2) == 1):
                output.putpixel((x,y),(0,0,0))
    return output




def main():
    dir = os.getcwd()+"/photos/"
    test = Image.open(dir+"logo.jpg")
    blur(test,10).save("logo_blur.png" ,"PNG")


if __name__ == "__main__":
    main()



