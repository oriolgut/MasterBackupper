import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


    zipf = zipfile.ZipFile('DESTINATIONPATH', 'w', zipfile.ZIP_DEFLATED)
    zipdir('SOURCEPATH', zipf)
    zipf.close()