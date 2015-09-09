#variable declaration
imgList = []
imgNum = 9
height = 0
width = 0

def makePixel(pixel):
  i = 0
  channelList = []
  
  while (i < imgNum):
    curPix = getPixel(imgList[i], getX(pixel), getY(pixel))
    channelList.append((getRed(curPix)+getBlue(curPix)+getGreen(curPix), i))
    i=i+1
  
  #sort list
  channelList.sort()
  
  #get median
  medianNum = channelList[imgNum/2][1]
  
  #return pixel color
  return getColor(getPixel(imgList[medianNum], getX(pixel), getY(pixel)))

def makeImage():
  #print "makeImage"
  finalImage = makeEmptyPicture(width, height)
  j = 0
  k = 0
  
  while (j < height):
    while (k < width):
      pixel = getPixel(finalImage, k, j)
      setColor(pixel, makePixel(pixel))
      k=k+1
    k = 0
    j=j+1
    
  writePictureTo(finalImage, "C:\\Users\\Josh\\Documents\\Fall 2015\\CST 205 - Multimedia Programming\\Project1\\finalImage.png")

#set image list to all 9 images
def load():
  i = 1

  while (i <= imgNum):
    file = "C:\\Users\\Josh\\Documents\\Fall 2015\\CST 205 - Multimedia Programming\\Project1\\" + str(i) + ".png"
    imgList.append(makePicture(file))
    i = i+1
    
  global height
  global width
    
  height = getHeight(imgList[0])
  width = getWidth(imgList[0])
  
#test image elements
def test():
  pixel = getPixel(imgList[0],0,0)
  color = getColor(pixel)
  print pixel
  print color
  print width
  print height

#run program
load()
test()
makeImage()