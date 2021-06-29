import os
import zipfile

print("Archiver...")
print("-----------------------")
print("Folders in current folder will be zipped if the zips don't exist yet.")
print("No version check will occur.")
print("-----------------------")


def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))


if __name__ == '__main__':
    dlist = []
    flist = []
    for filename in os.listdir():
        if os.path.isdir(filename):
            dlist.append(filename)
        else:
            flist.append(filename)

    l = len(dlist)
    i = 0
    for dir in dlist:
        i = i + 1
        flag = 0
        zip = dir + ".zip"
        rar = dir + ".rar"
        tar = dir + ".tar"

        if zip not in flist and rar not in flist and tar not in flist:
            print("("+str(i)+"/"+str(l)+") Archiving '" + dir + "'")
            zipf = zipfile.ZipFile(zip, 'w', zipfile.ZIP_STORED, True)
            zipdir(dir, zipf)
            zipf.close()
        else:
            print("("+str(i)+"/"+str(l)+") Skipping '" + dir + "'")

    input("press enter to exit..")
