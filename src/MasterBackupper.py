from tkinter.filedialog import askdirectory
import os
import zipfile
import datetime

now = datetime.datetime.now()

source = askdirectory(title = 'Source Folder')

destination = askdirectory(title = 'Destination Folder')

zipf = zipfile.ZipFile(destination + '/backup' + now.strftime('%Y%m%d%H%M') + '.zip', 'w', zipfile.ZIP_DEFLATED)
dirs = os.listdir(source)
for file in dirs:
    zipf.write(source + '/' + file)
zipf.close()
