from tkinter.filedialog import askdirectory
import os
import zipfile

source = askdirectory(title = 'Source Folder')

destination = askdirectory(title = 'Destination Folder')

zipf = zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED)
dirs = os.listdir(source)
for file in dirs:
    zipf.write(source + '/' + file)
zipf.close()
