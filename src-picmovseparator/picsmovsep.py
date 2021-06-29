'''
This is a small script to recursively go trough a bunch of folders and put all the pictures in a subfolder called pics
rev 00 - 03-aug-2016
@author: Jorrit Vander Mynsbrugge
'''
import os

def is_picture(f):
    '''check of file f een afbeelding is'''
    ext = os.path.splitext(f)[-1]
    if  ext in ('.jpg', '.JPG', '.jpeg', '.png', '.PNG', '.gif'):
        return True
    else:
        return False

def main(startingpoint = os.getcwd()):
    '''verplaatst de files die niet op hun plaats staan'''
    #walk 
    for root, dirs, files in os.walk(startingpoint):
        for f in files:
            if f == 'Thumbs.db':
                continue
            original_fullpath = os.path.join(root, f)
            dirname = os.path.basename(root)
            ispic = is_picture(f)
            if dirname == 'pics':
                if not ispic:
                    # is not pic but is in pics so move the file one dir up
                    target_directory = os.path.split(root)[0]
                    target_fullpath = os.path.join(target_directory, f)
                    if os.path.exists(target_fullpath):
                        continue
                    os.rename(original_fullpath ,target_fullpath)
                    print('Moved Up: ' + '\n\t' + original_fullpath + '\n' + 'To ' + '\n\t' + target_fullpath)
            else:
                if ispic:
                    # is pic but is not in pics so move the file one dir down
                    target_directory = os.path.join(root, 'pics')
                    target_fullpath = os.path.join(target_directory, f)
                    if not os.path.exists(target_directory):
                        # create directory
                        os.makedirs(target_directory)
                        print('Created:' + '\n\t' + target_directory)
                    if os.path.exists(target_fullpath):
                        continue
                    os.rename(original_fullpath ,target_fullpath)
                    print('Moved Down:' + '\n\t' + original_fullpath + '\n' + 'To ' + '\n\t' + target_fullpath)


if __name__ == '__main__':
    main()

