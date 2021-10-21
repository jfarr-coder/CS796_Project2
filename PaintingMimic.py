import sys
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import os
class Rectangle:  
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    def display(self):
        print("[{} {} {}]".format(self.red, self.green, self.blue))

#Links That Could Help Me
# https://matplotlib.org/stable/tutorials/introductory/images.html
# https://www.tutorialspoint.com/matplotlib/matplotlib_working_with_images.htm
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html
# https://www.geeksforgeeks.org/matplotlib-pyplot-imread-in-python/
# https://www.geeksforgeeks.org/getting-started-scikit-image-image-processing-python/
# https://matplotlib.org/stable/gallery/images_contours_and_fields/image_clip_path.html#sphx-glr-gallery-images-contours-and-fields-image-clip-path-py

def convertToFileName(argv):
    inp= str(argv)
    cwd = os.getcwd()
    filename = cwd + "/data/" + inp + ".jpeg"
    return str(filename)

def saveFileName(argv):
    inp= str(argv)
    cwd = os.getcwd()
    directory = cwd + "/results/" + inp 
    os.makedirs(directory)
    filename = directory + "/Result0.jpeg"
    return str(filename)

if __name__ == "__main__":
    filename = convertToFileName(sys.argv[1])
    saveLoc = saveFileName(sys.argv[1])
    print(filename)
    #img = image.imread(filename)
    r = Rectangle(255, 255, 255)
    r.display()
    #imgplot = plt.imshow(img)
    #imgplot.show()
    with cbook.get_sample_data(filename) as image_file:
        image = plt.imread(image_file)
    #arrays =0
    #for img in image:
    #    arrays+=1
    #print(arrays)
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.axis('off')
  
    #plt.title('matplotlib.pyplot.imread() function Example', fontweight ="bold")
    plt.savefig(saveLoc)
    plt.show()