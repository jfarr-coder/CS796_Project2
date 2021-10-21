import sys
import matplotlib
import skimage

def convertToFileName(argv):
    inp= str(argv)
    filename = "data/" + inp + ".png"
    return filename
    
if __name__ == "__main__":
    filename = convertToFileName(sys.argv[1])
    print(filename)