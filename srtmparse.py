# Defines a class with functions to parse HGT files (the srtmParser class is adapted from a stack-exchange post)
import struct

class srtmParser(object):
    def parseFileL1(self,filename):
        # Read 12,967,201 (3601x3601) high-endian signed 16-bit words into self.z
        # Used for Level 3 SRTM data (1-arc second granularity)
        fi=open(filename,"rb")
        contents=fi.read()
        fi.close()
        self.hgtcontents=struct.unpack(">12967201H", contents)
    def parseFileL3(self,filename):
        # Read 1,442,401 (1201x1201) high-endian signed 16-bit words into self.z
        # Used for Level 1 SRTM data (3-arc second granularity)
        fi=open(filename,"rb")
        contents=fi.read()
        fi.close()
        self.hgtcontents=struct.unpack(">1442401H", contents)
