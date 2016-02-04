import numpy as np
import srtmchoose
import srtmdownload
import srtmparse

# Select target coordinates, level of detail, and units of altitude and define parameters based on input
parameters = srtmchoose.srtmChoose()
target = parameters.chooseTarget()
detail, csvtarget, width, horizontalscale = parameters.chooseDetail()
unitscale = parameters.chooseUnits()

# Download, unzip, and parse HGT file
downloader = srtmdownload.srtmDownloader()
parser = srtmparse.srtmParser()

if detail == 1:
    downloader.downloadFileL1(target)
    parser.parseFileL1(target+".hgt")
else:
    downloader.downloadFileL3(target)
    parser.parseFileL3(target+".hgt")
    
# Read data from file into numpy array and save as a CSV file. There are three columns with X, Y, and Z dimensions for each point   
i = 0
for ydimension in range(1, width): # Technically height here, but it's a square
    for xdimension in range(1, width):
        csvtarget[i][0]=int(xdimension)*horizontalscale*unitscale
        csvtarget[i][1]=-int(ydimension)*horizontalscale*unitscale
        csvtarget[i][2]=int(parser.hgtcontents[width*ydimension+xdimension]*unitscale)
        i += 1
        
csvfilename = input("What would you like to name your CSV file?")
np.savetxt(csvfilename + ".csv", csvtarget, delimiter=",")

# This csv file can be imported directly into Rhinoceros 5 software to create a 3D point cloud of the topography.
