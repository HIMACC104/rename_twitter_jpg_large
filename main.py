import os
import pathlib
import glob


directory = os.getcwd()
target_path = directory + '\\*'

origin_suffixes = ".jpg_large"
final_suffixes = ".jpg"

full_path = target_path + origin_suffixes 


targetPattern = full_path
suitable_files=glob.glob(targetPattern)


for filename in suitable_files:
    root,suffixes = os.path.splitext(filename)
    filename_new = root + final_suffixes
    print(filename + " --> " + filename_new)
    os.rename(filename,filename_new)
