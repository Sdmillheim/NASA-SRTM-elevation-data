# Defines a class with functions to prompt user for parameters for data download and format
import numpy as np

class srtmChoose(object):
    def chooseTarget(self):
        target = '________'
        while not (target[0] in ("N", "S") and target[1:3].isdigit() and target[3] in ("W", "E") and target[4:7].isdigit()):
            print('Select target coordinates (Format example: N46W122)')
            target = input('--> ')
        return target
    def chooseDetail(self):
        detail = ''
        while detail != 1 and detail != 3:
            print('Select level of detail. Enter 1 for 1-arc second (higher detail) or 3 for 3-arc second (lower detail)')
            detail = int(input('--> '))
        csvtarget = np.zeros(((3600/detail)**2,3)) #either 3600X3600 or 1200X1200. One less than file dimension because files overlap. 
        width = int(3600/detail + 1)
        return (detail, csvtarget, width)
    def chooseUnits(self):
        units = ''
        while units not in ("Feet", "Meters"):
            print("please input either 'Feet' or 'Meters'")
            units = input('--> ')
        if units == "Feet":
            unitscale = 3.281 # this is feet per 1 meter
        else:
            unitscale = 1
        return unitscale
