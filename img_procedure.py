# Proje 4
import numpy
from PIL import Image

def getImg(img_dir):
    try:
      
        img = Image.open(img_dir).convert('L')
    except:
        return None

    if img.size != (25, 25):
        img = img.resize((25, 25))
  
    img = numpy.array(img).tolist()
    img_list = []
    for line in img:
        for value in line:
            img_list.append(value)
    return img_list

def getImgDir(argumans):
   
    if len(argumans) < 2:
        return None
    return argumans[1]
