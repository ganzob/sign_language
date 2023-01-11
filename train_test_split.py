from utils.utils import createFolder
import os
import shutil

import sys
sys.path.append('/projects/sign_language/')

data_path = '/projects/ZHO/formats/letters_raw/'
dest_path = '/projects/ZHO/formats/letters_splitted/'

people = os.listdir(data_path)
classes = [i.split('.')[0]
           for i in os.listdir(os.path.join(data_path, 'Ganzo'))]
print(classes)
for i, test in enumerate(os.listdir(data_path)):
    createFolder(os.path.join(dest_path, str(i), 'test'), True)
    createFolder(os.path.join(dest_path, str(i), 'train'), True)
    createFolder(os.path.join(dest_path, str(i), 'val'), True)

    train = people.copy()
    train.remove(test)
    for letter in classes:
        createFolder(os.path.join(dest_path, str(i), 'train', letter), True)
        createFolder(os.path.join(dest_path, str(i), 'test', letter), True)
        createFolder(os.path.join(dest_path, str(i), 'val', letter), True)

        shutil.copy(os.path.join(data_path, test, letter+'.mp4'),
                    os.path.join(dest_path, str(i), 'test', letter, test+'_'+letter+'.mp4'))
        shutil.copy(os.path.join(data_path, test, letter+'.mp4'),
                    os.path.join(dest_path, str(i), 'val', letter, test+'_'+letter+'.mp4'))

        print(train)
        for person in train:
            shutil.copy(os.path.join(data_path, person, letter+'.mp4'),
                        os.path.join(dest_path, str(i), 'train', letter, person+'_'+letter+'.mp4'))
