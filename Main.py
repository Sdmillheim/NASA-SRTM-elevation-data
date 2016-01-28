import numpy as np
import srtmdownload
import srtmparse

# Select target coordinates, level of detail, and units of altitude
while True:
    try:
        target = input("Select target coordinates (example: N46W122)")
    except ValueError:
        print("invalid target format")
        continue
    if target[0] in ("N", "E") and target[1:3].isdigit() and target[3] in ("W", "E") and target[4:7].isdigit():
        break
    else:
        print("Please enter coordinates in the correct format. Examples include: N46W122, N27E088, or S32W071")
while True:
    try:
        detail = int(input("Select level of detail. Enter 1 for 1-arc second (higher detail) or 3 for 3-arc second (lower detail)"))
    except ValueError:
        print("Please input either 1 or 3")
        continue
    if detail == 1 or detail == 3:
        break
    else:
        print("Please enter either 1 or 3")
while True:
    try:
        units = input("Select units of altitude. Enter 'Feet' or 'Meters'")
    except ValueError:
        print("please input either 'Feet' or 'Meters'")
        continue
    if units in ("Feet", "Meters"):
        break
    else:
        print("please enter either 'Feet' or 'Meters'")

# Define some parameters for later use based on input        
if units == "Feet":
    unitscale = 3.281 # this is feet per 1 meter
else:
    unitscale = 1
csvtarget = np.zeros((int(3600/detail)**2,3)) #either 3600X3600 or 1200X1200. One less than file dimension because files overlap. 
width = int(3600/detail) + 1
horizontalscale = 30*detail #this corresponds to the granularity (in meters) of the data

# Download, unzip, and parse HGT file
downloader = srtmdownload.srtmDownloader()
parser = srtmparse.srtmParser()

if detail == 1:
    downloader.downloadFileL1(target)
    parser.parseFileL1(target+".hgt")
else:
    downloader.downloadFileL3(target)
    parser.parseFileL3(target+".hgt")
    
# Read data from file into numpy array and save as a CSV file. There are three columns and each row represents X, Y, and Z dimensions    
i = 0
for ydimension in range(1, width): #technically 'height' in this loop, but it's a square
    for xdimension in range(1, width):
        csvtarget[i][0]=int(xdimension)*horizontalscale*unitscale
        csvtarget[i][1]=-int(ydimension)*horizontalscale*unitscale
        csvtarget[i][2]=int(parser.hgtcontents[width*ydimension+xdimension]*unitscale)
        i += 1
        
csvfilename = input("What would you like to name your CSV file?")
np.savetxt(csvfilename + ".csv", csvtarget, delimiter=",")

# This csv file can be imported directly into Rhinoceros 5 software to create a 3D point cloud of the topography.
