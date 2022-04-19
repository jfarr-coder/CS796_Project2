import sys
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import os
from random import randint
from PIL import Image, ImageDraw

# Class created for a Rectangle
class Rectangle:  
    def __init__(self, red, green, blue, x, y):
        self.red = red
        self.green = green
        self.blue = blue
        self.x = x
        self.y = y
     #   self.fitness = 0.0

    #def setFitness(self,f):
    #    self.fitness = f
    def display(self):
        print("Coordinates: [{} {}]".format(self.x, self.y))
        print("Colors: [{} {} {}]".format(self.red, self.green, self.blue))
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
                #r.setFitness(100.0)
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
    excess_height=height*2
    excess_width=width*2
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
def fitness(random, original):
    o_sum=original.red + original.green + original.blue + 1
    r_sum=random.red + random.green + random.blue

    fitness = (r_sum/o_sum)*100
    return fitness

# Planned to have the function take the rectangle parameter and append it to the mutated array.
def selection(random, originals, f=None):
    old_fitness=0.0
    #selection=random
    for o in originals:
        if o==f:
            continue
        fitn=fitness(random,o)
        if(fitn<old_fitness):
            continue
        elif(fitn>= 90 or fitn<=100):
            selection=random
            old_fitness=fitn
    #selection.display()
    return selection

def mutate(child):
    gen=randint(0,2)
    if(gen==0):
        child.red=randint(0,255)
    elif(gen==1):
        child.green=randint(0,255)
    elif(gen==2):
        child.blue=randint(0,255)
    return child

def crossover(parent1, parent2):
    gen=randint(0,2)
    if(gen==0):
        child=Rectangle(parent1.red, parent1.green, parent2.blue, parent1.x, parent1.y)
    elif(gen==1):
        child=Rectangle(parent1.red, parent2.green, parent2.blue, parent1.x, parent1.y)
    elif(gen==2):
        child=Rectangle(parent2.red, parent2.green, parent1.blue, parent1.x, parent1.y)
    return child

def genetic(randoms, originals):
    population = []
    prob_mutation=None
    gen=randint(0,1)
    for r in range(len(randoms)):
        p1 = selection(randoms[r], originals)
        p2 = selection(randoms[r+1], originals, f=p1)
        child = crossover(p1, p2)
        if(gen==1):
            prob_mutation=1/3
        if(prob_mutation!=None):
            child=mutate(child)
        child.display()
        population.append(child.red)
        population.append(child.green)
        population.append(child.blue)
    return population

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
    i = Image.open(filename)
    o = np.asarray(i)
    directory = cwd + "/results/" + inp
    if(not os.path.isdir(directory)):
        os.makedirs(directory)
    filename = directory + "/Original.jpeg"
    if(not os.path.exists(filename)):
        i = Image.fromarray(o)
        i.save(filename)
    return str(filename)

# Saves the result in an output file in the results directory
# Has all the images outputted already
def saveFileName(argv, result, gen):
    inp= str(argv)
    cwd = os.getcwd()
    directory = cwd + "/results/" + inp
    if(not os.path.isdir(directory)):
        os.makedirs(directory)
    filename = directory + "/Result" + str(result) + ".jpeg"
    if(not os.path.exists(filename)):
        i = Image.fromarray(gen.astype(np.uint8))
        i.save(filename)
    return str(filename)

if __name__ == "__main__":
    filename = convertToFileName(sys.argv[1])
    mutation = np.empty((5, 5))
    im = Image.open(filename)
    #im1 = Image.Image.getcolors(im) 
    width, height = im.size
 
    # Setting the points for cropped image
    left = 5
    top = height / 4
    right = 164
    bottom = 3 * height / 4
    
    crop1 = im.crop((left, top, right, bottom))
    crop1.save("Crop.jpg")
    im3 = Image.Image.getcolors(crop1) 
    for i in im3:
        print(i[1])

    w, h = 220, 190
    shape = [(100, 100), (w - 10, h - 10)]
    im2 = Image.new( mode = "RGB", size = (im.width, im.height))
    #im2.save("Test.jpg")

    # creating new Image object
    im3 = Image.new("RGB", (w, h))
  
    # create rectangle image
    im3 = ImageDraw.Draw(im2)  
    im3.rectangle(shape, fill ="#ffff33")
    im2.save("Test2.jpg")
    originals = getData(filename) 
    r = 1
    #while(r<=5):
    #    randoms = generateRectangles(filename)
    #    gens = genetic(randoms,originals)
        #print(gens)
    #    gented = np.asarray(gens).reshape(im.height, im.width, 3)
    #    saveFileName(sys.argv[1],r, gented)
    #    r+=1
    #gented = np.asarray(gens).reshape(im.height, im.width, 3)
    #g = gented.reshape(im.height, im.width, 3)
    #print(g)
    #print(g.shape)
    #print(g.size)
    #i2 = Image.fromarray(g.astype(np.uint8))
    #i2.save("test5.jpeg")