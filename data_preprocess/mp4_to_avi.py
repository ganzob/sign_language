import os
import glob
import ntpath
import sys


def convert_mp4_to_avi(file_name, output_directory):
    input_name = file_name
    output_name = ntpath.basename(file_name)
    print('input:', input_name)
    print('output_name:', output_name)
    # print('ddd:',output_name)
    output = output_directory + '/' + output_name.replace('.mp4', '.avi', 1)
    print('dddddddd:', output)
    cmd = 'ffmpeg -i "{input}" -c:v libx264 -c:a libmp3lame -b:a 384K "{output}"'.format(
        input=input_name,
        output=output)
#    print(cmd)
    return os.popen(cmd)


def convert():
    input_directory = '/data/ZHO/formats/ucf101_letters_only/'
    output_directory = '/data/ZHO/formats/ucf101_letters_only_avi/'

    for mode in ['train', 'test', 'val']:
        for clas in os.listdir(os.path.join(input_directory, mode)):
            # print(clas)
            files = os.listdir(os.path.join(input_directory, mode, clas))
            # for file_name in glob.glob(os.path.join(input_directory,mode,clas)+'*.mp4'):
            print('files:', files)
            os.makedirs(os.path.join(output_directory, mode, clas))
            for file_name in files:
                print(file_name)
                try:
                    print('try:', file_name)
                    convert_mp4_to_avi(os.path.join(input_directory, mode, clas, file_name), os.path.join(
                        output_directory, mode, clas))
                except:
                    raise


if __name__ == "__main__":

    convert()
