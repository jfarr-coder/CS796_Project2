import sys
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import os
from random import randint
from PIL import Image

# Class created for a Coordinate
class Coordinate:
    def __init__(self, i, x, y):
        self.id = i
        self.x = x
        self.y = y
    
    def display(self):
        print("Coordinate {}: {},{}".format(self.id,self.x, self.y))

# Class created for a Rectangle
class Rectangle:  
    def __init__(self, red, green, blue, x, y):
        self.red = red
        self.green = green
        self.blue = blue
        self.x = x
        self.y = y
        

    def display(self):
        print("Colors: [{} {} {}]".format(self.red, self.green, self.blue))
        print("Coordinates: [{} {}]".format(self.x, self.y))
        #for c in self.coords:
        #    c.display()

# Used for getting the original rectangles from the image
def getData(filename):
    originals = []
    with open(filename, "rb") as fp:
        im = Image.open(fp)
        pix = im.load()
        width, height = im.size
        pixel_values = np.array_split(im.getdata(),height)
        h=0
        while h < height:
            w=0
            while w < width:
                test = str(pixel_values[h][w])
                p2= str.split(test)
                p3 = str.split(p2[1],"[")
                R = int(p3[0])
                G = int(p2[1])
                p4 = str.split(p2[1],"]")
                B = int(p4[0])
                r = Rectangle(R,G,B,h,w)
                originals.append(r)

                w+=1
            h+=1
    return originals

# Used for creating rectangles, with randomly generated RGB values
def generateRectangles(filename):
    rectangles= []
    with open(filename, "rb") as fp:
        im = Image.open(fp)
        pix = im.load()
        width, height = im.size
    h=0
    while h < height:
        w=0
        while w < width:
            R= randint(0,255)
            G= randint(0,255)
            B= randint(0,255)
            r = Rectangle(R,G,B,h,w)
            rectangles.append(r)
            w+=1
        h+=1
    return rectangles

# Calculates the differences between both the original and generated rectangles
def fitness(randoms, originals):
    i=0
    diffs=[]
    while i< len(originals):
        rO = originals[i]
        rG = randoms[i]
        
        diff_red = rO.red - rG.red
        diff_green = rO.green - rG.green
        diff_blue = rO.blue - rG.blue

        red_close = 0 < diff_red < 10
        green_close = 0 < diff_green < 10
        blue_close = 0 < diff_blue < 10
        if(red_close or green_close or blue_close):
            selection(rG)
            diffs.append(diff_red)
            diffs.append(diff_green)
            diffs.append(diff_blue)
        elif(diff_red <0 or diff_green<0 or diff_blue<0):
            diff_red = randint(0,rO.red)
            diff_green = randint(0,rO.green)
            diff_blue = randint(0,rO.blue)
            diffs.append(diff_red)
            diffs.append(diff_green)
            diffs.append(diff_blue)
            
            
        #print("Differences between the two rectangles: {} {} {}".format(diff_red,diff_green,diff_blue))
        i+=1
    return diffs

# Planned to have the function take the rectangle parameter and append it to the mutated array.
def selection(rectangle):
    rgbs = []
    rgb = []
    rgb.append(rectangle.red)
    rgb.append(rectangle.blue)
    rgb.append(rectangle.green)
    rgbs.append(rgb)
    #print("CODE HERE")

# Planned to have the function take the height and width of the data and then use it for creating an empty numpy array.
# The array would take mix both aspects of the original and generated rectangles.
# Finally, I was thinking of having that array be converted into an image
def geneticMutation(height, width):
    mutation = np.empty((height, width))
    #print("CODE HERE")

#Links That Could Help Me
# https://matplotlib.org/stable/tutorials/introductory/images.html
# https://www.tutorialspoint.com/matplotlib/matplotlib_working_with_images.htm
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html
# https://www.geeksforgeeks.org/matplotlib-pyplot-imread-in-python/
# https://www.geeksforgeeks.org/getting-started-scikit-image-image-processing-python/
# https://matplotlib.org/stable/gallery/images_contours_and_fields/image_clip_path.html#sphx-glr-gallery-images-contours-and-fields-image-clip-path-py

# Converts the command line argument to a filename, with both a directory and extension
def convertToFileName(argv):
    inp= str(argv)
    cwd = os.getcwd()
    filename = cwd + "/data/" + inp + ".jpeg"
    return str(filename)

# Saves the result in an output file in the results directory
# Has all the images outputted already
def saveFileName(argv):
    inp= str(argv)
    cwd = os.getcwd()
    directory = cwd + "/results/" + inp 
    if(not os.path.isdir(directory)):
        os.makedirs(directory)
    filename = directory + "/Result0.jpeg"
    return str(filename)

if __name__ == "__main__":
    filename = convertToFileName(sys.argv[1])
    saveLoc = saveFileName(sys.argv[1])
    mutation = np.empty((5, 5))
    print(filename)
    im = Image.open(filename)
    print("BEFORE CONVERTING TO NUMPY")
    a = np.asarray(im)
    print("AFTER CONVERTING TO NUMPY")
    print(a)
    print("Getting the Original Rectangles")
    originals = getData(filename)
    print(originals)
    print("Generating Random Rectangles")
    randoms = generateRectangles(filename)
    print(randoms)
    print("Finding the Difference Between the Two")
    print(fitness(randoms,originals))
    with cbook.get_sample_data(filename) as image_file:
        image = plt.imread(image_file)
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.axis('off')

    plt.savefig(saveLoc)
    plt.show()