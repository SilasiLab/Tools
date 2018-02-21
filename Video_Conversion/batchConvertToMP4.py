# Convert all h264 files in a specified directory and all subdirectories to MP4 and output to subdirectory where each h264 is found
# Author: Dirk
# Last edited: 2015-07-01 by Dirk (Happy Canaday)

# install GPAC before running this code!!!

### INPUT ###
# Change folderContaining_h264 to the folder containing the videos
# OutputFolder:
# If True, mp4s will be outputted into a seperate folder in the directory where any h264's are found.
# If False, mp4's will be outputted to the same directory whereever the corresponding h264 is
folderContaining_h264 = '/media/pi/SILASI 8GB/'
OutputFolder = False
##

import os
import glob

folderDirList = [x[0] for x in os.walk(folderContaining_h264)]

for folderDir in folderDirList:
    os.chdir(folderDir)
    for vidName in glob.glob('*.h264'):
        vidConvertName = str.replace(vidName,'h264','mp4')    
        if OutputFolder:
            if not os.path.exists(folderDir+"/MP4"):
                os.makedirs("MP4")
            conversionCommand = "MP4Box -add " + vidName + " " + ("MP4/"+vidConvertName)
            os.system(conversionCommand)
        else:
            conversionCommand = "MP4Box -add " + vidName + " " + (vidConvertName)
            os.system(conversionCommand)
        # Uncomment this if you want to play each video after it has been converted. 
        # playCommand='omxplayer ' + vidConvertName
        # os.system(playCommand)
