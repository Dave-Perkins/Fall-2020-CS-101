import os
import random
from PIL import Image, ImageMath


#this file gives possible functions the students may creaete for thei image
# project

def main():
    #use os to easily get students to their directory with photos
    dir = os.getcwd()+"/ims/photos/"
    image = Image.open(dir +os.listdir(dir)[random.randint(0,100)] )




# makes a collage
def collage(directory):
    output = Image.new("RGB",(2000,2000))
    for filename in os.listdir(directory):
        image = Image.open(dir + filename)
        for x in range(0,2000,100):
            for y in range(0,2000,100):
                putIm(end,image,100,100,x,y)
    return output


#helper fucntion for blur
def getAvg(image,startx,starty,size):
    avg = (0,0,0)
    for x in range(startx,startx+size):
        for y in range(starty,starty+size):
            avg = tupleAdd(avg, image.getpixel((x,y)))
    avg = (avg[0]//size**2,avg[1]//size**2,avg[2]//size**2)
    return(avg)


#helper fucntions that adds # tuples
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


def putIm(img,copy,leng,width,startx,starty):
    for x in range(startx,startx+width):
        for y in range(starty,starty+leng):
            img.putpixel((x,y),copy.getpixel((int(((x-startx)/width)*copy.width),int(((y-starty)/leng)*copy.height))))






if __name__ == "__main__":
    main()
