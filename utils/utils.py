import os
import shutil


def createFolder(path, delete=True):
    if os.path.exists(path) and delete:
        shutil.rmtree(path)
        os.makedirs(path)
    else:
        try:
            if not os.path.exists(path):
                os.makedirs(path)

        except:
            print('Error creating ', path)
