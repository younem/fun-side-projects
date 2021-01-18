'''
Program that splits file into audio and accompaniments using
spleeter's AI library. Then saves files into a directory.

'''
from spleeter.separator import Separator
import os

def seperatechannels(filename):
    separator = Separator("spleeter:2stems")
    folder_name = "audio-channels"
    # create a directory to store the seperated audio channels
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    separator.separate_to_file(filename, folder_name)

if __name__ == '__main__':
    seperatechannels("testaudio.wav")
