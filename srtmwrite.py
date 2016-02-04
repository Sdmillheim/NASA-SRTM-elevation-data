# Defines a class with a function to read tuple from parser into numpy array and save as a CSV file. 
# Prompts the user to provide a file name.
import numpy as np

class srtmWriter(object):
    def srtmWriteFile(self, csvtarget, width, horizontalscale, hgtcontents, unitscale):
        i = 0
        for ydimension in range(1, width): #technically 'height' in this loop, but it's a square
            for xdimension in range(1, width):
                csvtarget[i][0]=int(xdimension)*horizontalscale*unitscale
                csvtarget[i][1]=-int(ydimension)*horizontalscale*unitscale
                csvtarget[i][2]=int(hgtcontents[width*ydimension+xdimension]*unitscale)
                i += 1
        
        csvfilename = input("What would you like to name your CSV file?")
        np.savetxt(csvfilename + ".csv", csvtarget, delimiter=",")
        return 'File is saved.'
