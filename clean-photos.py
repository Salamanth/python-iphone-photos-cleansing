# Python program to rename all file
# names in your directory 

import os

# Setting directory
os.chdir('photos')

# Looping on all files 
for file in os.listdir():
  fileName, fileExt = os.path.splitext(file)
  filePath = os.path.join(os.getcwd(), file)

  # Removing .AAE files
  if fileExt == '.AAE' :
    os.remove(filePath)

  # Replacing original files with edited ones
  if fileName.find('_E') != -1 :
    originalFileName = fileName.replace('_E', '_')

    # Deleting the the original file if it exists
    if os.path.exists(originalFileName + fileExt):
      os.remove(originalFileName + fileExt)
    
    # Renaming the edited file with the original fileName
    os.rename(file, originalFileName + fileExt)