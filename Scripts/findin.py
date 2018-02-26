#! /usr/bin/python

/* Python script which will find a file or directory within a specific directory. Put this script in your path, and change the permissions. 
  Call the script with two arguments, the first one being the directory, and the second one being the file or 
  directory you are looking for, example:
  findin.py var index.php */

import os
import sys

def dirFilePath(directory):
    file = sys.argv[2]
    match_output = ''
    error_output = ''
    if os.path.isfile(directory):
        if file == directory:
            path = os.path.realpath(directory)
            match_output += "MATCH: %s " % (path)
        else:
            match = os.path.realpath(options)
            error_output += "ERROR: %s was not found in: %s \n" % (file, match)
    elif os.path.isdir(directory):
        dirList = os.walk(os.path.realpath(directory))
        print "Looking in directory:", directory
        for root, dirs, files in dirList:
            for name in files:
                if file == name:
                    path =  os.path.join(root, name)
                    match_output += "MATCH FILE IN: %s \n" % (path)
            for name in dirs:
                if file == name:
                    path =  os.path.join(root, name)
                    match_output += "MATCH DIRECTORY IN: %s \n" % (path)
    if match_output:
        print match_output
    else:
        match = directory
        print "ERROR: %s was not found in: %s \n" % (file, match)

def main(dir, fil):
    directory = dir
    file = fil
    dirFilePath(directory)

if __name__ == '__main__': main(sys.argv[1], sys.argv[2])
