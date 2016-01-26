import numpy as np
import urllib
import zipfile
import srtm

#select target coordinates, level of detail, and units of altitude
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

#download zipped file and extract contents as hgt file named 'target' + .hgt
file = urllib.request.urlretrieve("http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL"+str(detail)+".003/2000.02.11/"+target+".SRTMGL"+str(detail)+".hgt.zip", "file.hgt.zip")
zipfile.ZipFile('file.hgt.zip').extractall()

#parse HGT file and save contents as numpy array
parser = srtm.srtmParser()
if detail == 1:
    parser.parseFileL3(target+".hgt")
    csvtarget = np.zeros((12960000,3)) #3600x3600
    width = 3601
    horizontalscale = 30 #this corresponds to the granularity (in meters) of the data
else:
    parser.parseFileL1(target+".hgt")
    csvtarget = np.zeros((1440000,3)) #1200x1200
    width = 1201
    horizontalscale = 90 #this corresponds to the granularity (in meters) of the data
if units == "Feet":
    unitscale = 3.281 # this is feet per 1 meter
else:
    unitscale = 1
    
#place parsed np array into CSV file. There are three columns and each row represents X, Y, and Z dimensions    
i = 0
for ydimension in range(1, width):
    for xdimension in range(1, width):
        csvtarget[i][0]=int(xdimension)*horizontalscale*unitscale
        csvtarget[i][1]=-int(ydimension)*horizontalscale*unitscale
        csvtarget[i][2]=int(parser.hgtcontents[width*ydimension+xdimension]*unitscale)
        i += 1
csvfilename = input("What would you like to name your  CSV file?")
np.savetxt(csvfilename + ".csv", csvtarget, delimiter=",")

# This csv file can be imported directly into Rhinoceros 5 to create a 3D point cloud of the topography.
