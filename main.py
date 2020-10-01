# 1. download from team city to buildSourceBinaryFiles (done manually for now)
# 2. Unzip the files to local dir
# 3. Do folder manipulation


import os
import zipfile
from pathlib import Path
#from shutil import copy
#from shutil import rmtree

def unZipBinaries():
    #unzip all
    #delete zip files
    zipList = ['cms.mediasuite.rim_52','RIM_CMS_v52','RIM_ContentSetPublish_v52']
        # Need to be able to parse these with only containing mediasuite, CMS , ContentSetPublish

    for name in zipList:
        with zipfile.ZipFile("buildSourceBinaryFiles" + name,"r") as zip_ref: #The file path is not working with this.
            zip_ref.extractall(os.getcwd())
        # TODO 
        #go into dir
        #check if the zip exsit 
        #yes unzip
        #no go to next one




#def prepareFilesForDeploy():
    #return

unZipBinaries()
#prepareFilesForDeploy()



