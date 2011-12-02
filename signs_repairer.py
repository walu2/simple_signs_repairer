# -*- coding: utf-8 -*-
import codecs
import tkFileDialog
import sys


import os
import glob
 
old_file_encoding = 'utf-8'
dest_file_encoding = 'iso-8859-2'
dest_file_suffix =  '_pl_'
prompt_txt = 'Wybierz katalog zawierający źle zakodowane źródła'

file_regex_types = '*' # or could be eg. '*.txt' etc.

def replace_file( source_file_path ):
   reload(sys)
   source_file = open( source_file_path, 'r' )
   sys.setdefaultencoding( old_file_encoding )
   dest_file_name = source_file.name[0:] + dest_file_suffix
   dest_file = codecs.open(dest_file_name, 'w', dest_file_encoding) 
 
   for l in source_file.readlines():
      dest_file.write( l.encode(old_file_encoding) ) 
 
   source_file.close()
   dest_file.close()
   
def repair_all_files_from_directory( path ):
   for infile in glob.glob( os.path.join(path, file_regex_types) ):
      replace_file( infile )
    
def main():
   source_dir = tkFileDialog.askdirectory(title = prompt_txt) 
   repair_all_files_from_directory( source_dir )
    
if __name__ == "__main__":
   main()
