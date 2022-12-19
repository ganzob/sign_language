import json
import os

import pandas as pd
import csv
ff = open('/data/ZHO/formats/kinetics/kinetics_letter_only/train.csv', 'w')
writer = csv.writer(ff)

with open('/data/ZHO/formats/ucf101_letters_only/annotations/trainlist01.txt') as f:

    #[writer.writerow(line) for line in f.readlines()]
    text = f.read()
    for line in text.split('\n'):
        print(line)
        writer.writerow([line])
ff.close()

ff = open('/data/ZHO/formats/kinetics/kinetics_letter_only/test.csv', 'w')
writer = csv.writer(ff)

with open('/data/ZHO/formats/ucf101_letters_only/annotations/testlist01.txt') as f:

    #[writer.writerow(line) for line in f.readlines()]
    text = f.read()
    for line in text.split('\n'):
        print(line)
        writer.writerow([line])

ff.close()


ff = open('/data/ZHO/formats/kinetics/kinetics_letter_only/val.csv', 'w')
writer = csv.writer(ff)

with open('/data/ZHO/formats/ucf101_letters_only/annotations/vallist01.txt') as f:

    #[writer.writerow(line) for line in f.readlines()]
    text = f.read()
    for line in text.split('\n'):
        print(line)
        writer.writerow([line])

ff.close()


# Prepare custom classnames.json

dictionary = {}
with open('/data/ZHO/formats/ucf101_letters_only/annotations/classInd.txt') as f:

    class_names = f.read()
    for line in class_names.split('\n'):
        print(line)
        [class_index, class_name] = line.split(' ')

        dictionary[class_name] = class_index

with open('/data/ZHO/formats/kinetics/kinetics_letter_only/custom_classnames.json', "w") as outfile:
    json.dump(dictionary, outfile)
