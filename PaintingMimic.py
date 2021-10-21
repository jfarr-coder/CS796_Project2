import sys
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import os

def convertToFileName(argv):
    inp= str(argv)
    cwd = os.getcwd()
    filename = cwd + "/data/" + inp + ".jpeg"
    return str(filename)

def saveFileName(argv):
    inp= str(argv)
    cwd = os.getcwd()
    filename = cwd + "/results/" + inp + ".jpeg"
    return str(filename)

if __name__ == "__main__":
    filename = convertToFileName(sys.argv[1])
    saveLoc = saveFileName(sys.argv[1])
    print(filename)
    img = image.imread(filename)
    #imgplot = plt.imshow(img)
    #imgplot.show()
    with cbook.get_sample_data(filename) as image_file:
        image = plt.imread(image_file)
  
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.axis('off')
  
    plt.title('matplotlib.pyplot.imread() function Example', fontweight ="bold")
    plt.savefig(saveLoc)
    plt.show()