#variable declaration
imgList = []

#set image list to all 9 images
def load():
  i = 1

  while (i <= 9):
    file = "C:\\Users\\Josh\\Documents\\Fall 2015\\CST 205 - Multimedia Programming\\Project1\\" + str(i) + ".png"
    imgList.append(makePicture(file))
    i = i+1
  
#test image elements
def test():
  #show(imgList[0])
  pixel = getPixel(imgList[0],0,0)
  color = getColor(pixel)
  print pixel
  print color

#run program
load()
test()