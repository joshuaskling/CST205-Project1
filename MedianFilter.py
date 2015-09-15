import time, sys, os, java

#variable declaration
imgList = []
imgNum = 0
height = 0
width = 0
#path = "C:\\Users\\Josh\\Documents\\Fall 2015\\CST 205 - Multimedia Programming\\Project1\\"
path = ""

def makePixel(pixel, selector):

  #change selection
  if (selector == 1):

    i = 0
    channelList = []
  
    
    while (i < imgNum):
       #print getX(pixel)
       #print getY(pixel)
       curPix = getPixel(imgList[i], getX(pixel), getY(pixel))
       channelList.append((getRed(curPix)+getBlue(curPix)+getGreen(curPix), i))
       i=i+1
  
    #sort list
    channelList.sort()
  
  
    #get median
    medianNum = channelList[imgNum/2][1]
    
    #return pixel color
    return getColor(getPixel(imgList[medianNum], getX(pixel), getY(pixel)))
    
  elif (selector == 2):
    #get mean
    i = 0
    newRed = 0
    newGreen = 0
    newBlue = 0
    
    while (i < imgNum):
      curPix = getPixel(imgList[i], getX(pixel), getY(pixel))
      newRed = newRed + getRed(curPix)
      newGreen = newGreen + getGreen(curPix)
      newBlue = newBlue + getBlue(curPix)
      
      i = i + 1
    
    newRed = newRed/imgNum
    newGreen = newGreen/imgNum
    newBlue = newBlue/imgNum
    
    return (makeColor(newRed, newGreen, newBlue))

def makeImage():
  startTime = time.time()
  
  selector = 1
  done = false
  
  #get filter selection
  while (done != true):
    userInput = input("Select filter. 1:Median 2:Mean ")
    if (userInput == 1):
      selector = 1
      done = true
    elif (userInput == 2):
      selector = 2
      done = true
    else:
      print "Invalid input. Try again."

  print "Processing..."
  sys.stdout.write("[")
  sys.stdout.flush()
  
  finalImage = makeEmptyPicture(width, height)
  j = 0
  k = 0
  statusCheck = 0
  statusInt = height*.02
  
  while (j < height):
    while (k < width):
      pixel = getPixel(finalImage, k, j)
      setColor(pixel, makePixel(pixel, selector))
      k=k+1
    k = 0
    j=j+1
    
    if (j > statusCheck):
      sys.stdout.write("=")
      sys.stdout.flush()
      statusCheck = statusCheck + statusInt
    
  endTime = time.time()
  
  sys.stdout.write("]")
  sys.stdout.flush()
  print "\n...Done! Process took " + str((int((endTime-startTime)*100)+.5)/100) + " seconds"
  print "Filename: finalimage.png"
  
  global path
  finalPath = path+"\\finalImage.png"
  
  #writePictureTo(finalImage, "C:\\Users\\Josh\\Documents\\Fall 2015\\CST 205 - Multimedia Programming\\Project1\\finalimage.png")
  writePictureTo(finalImage, finalPath)

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

#load all of the files!
def loadFiles():
  global path
  global imgNum
  global height
  global width
  path = raw_input('Enter path to folder: ')

  for file in os.listdir(path):
    if (file.endswith(".jpg") or file.endswith(".png")):
      imgNum = imgNum+1
      imgList.append(makePicture(path + file))
      
  #get minimum width and height
  width = 10000
  height = 10000
  i = 0
  
  while (i < imgNum):
    if (height > getHeight(imgList[i])):
      height = getHeight(imgList[i])
    if (width > getWidth(imgList[i])):
      width = getWidth(imgList[i])
    i = i+1
      
  
#test image elements
def test():
  pixel = getPixel(imgList[0],0,0)
  color = getColor(pixel)
  print str(imgNum) + " Images Loaded"
  print "Width: " + str(width)
  print "Height: " + str(height)

#run program
#load()
loadFiles()
test()
makeImage()