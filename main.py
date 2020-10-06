# 1. download from team city to buildSourceBinaryFiles (done manually for now)
# 2. Unzip the files to local dir
# 3. Do folder manipulation


import os
import zipfile
from pathlib import Path
#from shutil import copy
#from shutil import rmtree

buildSourceBinaryFilesPath = Path(os.getcwd() + "/buildSourceBinaryFiles/")
def get_binaries_from_TC():
    # Us the TC API 
    # Know which build to use
    # Download the files in the correct directory /buildSourceBinaryFiles
    # prefer to rename the downlaoded file to mediasuite, CMS , ContentSetPublish
    pass

def unZip_Binaries():
    # 1. Check that directory has correct binaries
    # 2. unzip all OR get binaries from TC and unzip
    # 3. delete zip files
    zipList = ['cms.mediasuite.rim_52.zip','RIM_CMS_v52.zip','RIM_ContentSetPublish_v52.zip']
        # Need to be able to parse these with only containing mediasuite, CMS , ContentSetPublish
    for name in zipList:
        with zipfile.ZipFile(Path(os.getcwd() + "/buildSourceBinaryFiles/" + name),"r") as zip_ref: #The file path is not working with this.
            zip_ref.extractall(Path(os.getcwd() + "/buildSourceBinaryFiles/" + name.replace('.zip','')))
            # This needs to be update to remove the hardcoded names and instead parse for the names

def prepare_files_for_deploy():
    # 1. Rename files - 
    # 2. Confiugure
    
    localList = os.listdir(buildSourceBinaryFilesPath)

    # Change all conditionals from hardcoded to some method function .contains
    for item in localList:
        if item == 'cms.mediasuite.rim_52':
            newList = os.listdir(Path(buildSourceBinaryFilesPath + "/cms.mediasuite.rim_52/"))
            for i in newList:
                if i != ('SeedData' or 'Upload' or 'Web.config'):
                    print('hey')
                    #os.remove(os.path.join(buildSourceBinaryFilesPath, file))

        elif item == 'RIM_CMS_v52':
            print('RIM_CMS_v52')

        elif item == 'RIM_ContentSetPublish_v52':
            print('RIM_ContentSetPublish_v52')

def remove_zip_files():
        for file in os.listdir(buildSourceBinaryFilesPath):
            if file.endswith('.zip'):
            os.remove(os.path.join(buildSourceBinaryFilesPath, file))

#unZip_Binaries()
#remove_zip_files
prepare_files_for_deploy()



