from tkinter.filedialog import askdirectory
import os
import zipfile

source = askdirectory()
print (source)
destination = askdirectory()
print (destination)

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


    zipf = zipfile.ZipFile(destination+'/heutigesdatum.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(source, zipf)
    zipf.close()