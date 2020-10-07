# 1. download from team city to buildSourceBinaryFiles (done manually for now)
# 2. Unzip the files to local dir
# 3. Do folder manipulation


import os
import zipfile
import time
from pathlib import Path
import shutil
from shutil import copy
from shutil import copytree
#from shutil import rmtree

buildSourceBinaryFilesPath = Path(os.getcwd() + "/buildSourceBinaryFiles/")
#localList = os.listdir(buildSourceBinaryFilesPath)
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
def remove_zip_files():
    try:
        for file in os.listdir(buildSourceBinaryFilesPath):
            if file.endswith('.zip'):
                os.remove(os.path.join(buildSourceBinaryFilesPath, file))
    except:
        print('Can not remove .zip files')

def prepare_files_for_deploy():
    # Change all conditionals from hardcoded to some method function .contains
    localList = os.listdir(buildSourceBinaryFilesPath)
    for item in localList:
        if item == 'cms.mediasuite.rim_52':
            mediaPath = str(buildSourceBinaryFilesPath) + "/" + item
            newList = os.listdir(mediaPath)
            for i in newList:
                if i not in ('SeedData','Web.config','Upload'):
                    os.remove(os.path.join(mediaPath, i))

        elif item == 'RIM_CMS_v52':
            cmsPath = str(buildSourceBinaryFilesPath) + "/" + item
            #print(item)
            #print(os.listdir(cmsPath))
            #os.chdir(cmsPath + "/" + "ingestservice")
            #copy(cmsPath + "/" + "ingestservice/",buildSourceBinaryFilesPath )
            #copytree(cmsPath + "/" + "ingestservice/",buildSourceBinaryFilesPath )
            # 1. Go into RIM_CMS_v52 -> Ingestservices -> publications
            # 2. Copy content back two directories
            # 3. Remove ingestservices
           
            tmpList = os.listdir(cmsPath + "/ingestservice/publications/")
            #newPath = cmsPath + "/ingestservice/publications/"
            #print(tmpList)
            #print(newPath)
            #print(cmsPath)
            copytree(cmsPath + "/ingestservice/publications/", cmsPath + "new")
        
            #os.remove(os.path.join(cmsPath + "/ingestservice", i))
        else:
            return
            #keep this line or fnction does not work

def rename_folders():
    localList = os.listdir(buildSourceBinaryFilesPath)
    os.chdir(buildSourceBinaryFilesPath)
    for item in localList:
        if item == 'cms.mediasuite.rim_52':
            os.rename(item,'mediasuite')
        elif item == 'RIM_CMS_v52':
            os.rename(item,'CMS')
        elif item == 'RIM_ContentSetPublish_v52':
            os.rename(item,'ContentSetPublish')

#get_binaries_from_TC()

#unZip_Binaries()

#remove_zip_files()

prepare_files_for_deploy()

#rename_folders()




