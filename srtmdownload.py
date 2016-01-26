#define a class with functions to download zipped file and extract contents as hgt file named 'target' + .hgt
import urllib
import zipfile

class srtmDownloader(object):
    def downloadFileL1(self,target):
        file = urllib.request.urlretrieve("http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11/"+target+".SRTMGL1.hgt.zip", "file.hgt.zip")
        zipfile.ZipFile('file.hgt.zip').extractall()
    def downloadFileL3(self,target):
        file = urllib.request.urlretrieve("http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL3.003/2000.02.11/"+target+".SRTMGL3.hgt.zip", "file.hgt.zip")
        zipfile.ZipFile('file.hgt.zip').extractall()
