# Defines a class with a function to read tuple from parser into numpy array and save as a CSV file. 
# Prompts the user to provide a file name.
import numpy as np

class srtmWriter(object):
    def srtmWriteFile(self, hgtcontents, detail, unitscale):
        csvtarget = np.zeros(((3600/detail)**2,3)) #either 3600X3600 or 1200X1200. One less than file dimension because files overlap. 
        i = 0
        for ydimension in range(1, int(3600/detail + 1)): # 1 to int(3600/detail + 1) represents length of x or y dimension of square
            for xdimension in range(1, int(3600/detail + 1)): 
                csvtarget[i][0]=int(xdimension)*unitscale*detail*30  # x dimension of 3D space
                csvtarget[i][1]=-int(ydimension)*unitscale*detail*30 # y dimension of 3D space
                csvtarget[i][2]=int(hgtcontents[width*ydimension+xdimension]*unitscale) # z dimension of 3D space
                i += 1
        
        csvfilename = input("What would you like to name your CSV file?")
        np.savetxt(csvfilename + ".csv", csvtarget, delimiter=",")
        return 'File is saved.'
