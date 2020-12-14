from pathlib import Path
import re 
import shutil
import os
import glob
import random

def list_of_files(dir_path):
    '''
    returns list of files inside a given directory
    
    ----Parameters----
    path : directory path --> 'data/images/'
    
    '''
    entries = Path(dir_path)
    file_names = []
    for entry in entries.iterdir():
        file_names.append(entry.name)
    return file_names



def map_list_of_directories(file_names, dir_loc):
    '''
    returns : list, ['dir_loc/file_in_list']
    
    ----Parameters----
    file_names : list of files inside directory
    dir_loc : string, directory address    
    '''
    dir_lst = []
    for file in file_names:
        dir_lst.append(dir_loc+file)
    return dir_lst



def rename_imgs(parent_dir, class_name, file_type):
    '''# rename images with plant type + condition'''
    files = Path(parent_dir)
    count = 0
    for file in files.iterdir():     
        if file.is_file():
            directory = file.parent
            new_name = class_name + str(count) + file_type
            new_name_path = Path(directory, new_name)
            
            file.rename(new_name_path)
            count+=1
    return str(count)+' renamed images'



def class_file_list(parent_dir_path, species_type, condition):    
    pathname = parent_dir_path + species_type + condition
    class_file_list = glob.glob(pathname)
    return class_file_list 

