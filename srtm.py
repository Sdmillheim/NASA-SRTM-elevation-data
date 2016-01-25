import numpy as np
import struct
import urllib
import zipfile

#define an class with a function to parse HGT files (the srtmParser class is adapted from a stack-exchange post)
class srtmParser(object):
    def parseFile(self,filename):
        # read 12,967,201 (3601x3601) high-endian signed 16-bit words into self.z
        fi=open(filename,"rb")
        contents=fi.read()
        fi.close()
        self.z=struct.unpack(">12967201H", contents)

#set target coordinates, example of format below
target = "N46W122"
#downloads zipped file and extracts contents as hgt file named 'target' + .hgt
file = urllib.request.urlretrieve("http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11/"+target+".SRTMGL1.hgt.zip", "file.hgt.zip")
unzip = zipfile.ZipFile('file.hgt.zip')
unzip.extractall()

#parse HGT file and save contents as numpy array
f = srtmParser()
f.parseFile(target+".hgt")
csvtarget = np.zeros((12960000,3)) #3600x3600
i = 0
for r in range(3600):
    for c in range(3600):
        va=f.z[(3601*(r+1))+c+1]
        if (va<0 or va>30000):
            va=0.0
        csvtarget[i][0]=int(c)
        csvtarget[i][1]=-int(r)
        csvtarget[i][2]=int(va*3.281) #for altitude in meters, remove the '*3.281' in this line
        i += 1
np.savetxt("elevationtarget.csv", csvtarget, delimiter=",")
