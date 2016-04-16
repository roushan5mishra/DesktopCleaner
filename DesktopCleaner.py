# Script: DesktopCleaner.py

# Author: Roushan Mishra

# Version: 1.0
# Date: 16-Apr-16

# Description: This python code moves files/directories from the Desktop to a specific folder on Desktop


import shutil
import os


def FileChecker(destFolder):
    try:
        if not os.path.exists("/Users/roushan/Desktop/"+destFolder):
            os.makedirs("/Users/roushan/Desktop/"+destFolder)
            print 'New Folder created as: '+destFolder
    except:
        print 'Great Destination file already exists!'


def FilesToMove(fileExtension, destFolder):

    try:

        for files in os.listdir("/Users/roushan/Desktop"):
               
            if files.endswith(fileExtension):
                shutil.move("/Users/roushan/Desktop/"+files, "/Users/roushan/Desktop/"+destFolder+'/'+files)
                print files+ ' moved to '+destFolder
    except:
        print "Error Occurred! try again.."

def DirectoriesToMove(directory, destFolder):

    try:

        for files in os.listdir("/Users/roushan/Desktop"):
            try:
                if not os.path.exists("/Users/roushan/Desktop"+destFolder):
                    os.makedirs("/Users/roushan/Desktop"+destFolder)
                    print 'New Folder created as: '+destFolder
            except:
                print 'Great Destination file already exists!'
                
            if files == directory:
                shutil.move("/Users/roushan/Desktop/"+files, "/Users/roushan/Desktop/"+destFolder+'/'+files)
                print directory+ ' moved to '+destFolder
    except:
        print "Error Occurred! try again.."
            
def main():
    while True:
        executer = raw_input('''
                press \'Y\' if you wish to move files from Desktop
                press \'N\' to exit
                ''')
        if executer.upper() == 'Y':

            ask = raw_input('''
                press \'1\' if you wish to move files
                press \'2\' if you wish to move directories
                press any other key to quit!!
                ''')
            if ask.upper() == '1':
                
                fileExtension = raw_input("Enter extension of file which you wish to move from Desktop: ")
                destFolder = raw_input("Enter Destination Folder name: ")
                 
                print "Moving File(s)! Please wait....."
                
                FileChecker(destFolder)
                FilesToMove(fileExtension, destFolder)
                
            elif ask.upper() == '2':
                
                directory = raw_input("Enter the name of Directory, which you wish to move from Desktop: ")
                destFolder = raw_input("Enter Destination Folder name: ")
                
                print "Moving File(s)! Please wait....."
                
                FileChecker(destFolder)
                DirectoriesToMove(directory, destFolder)
            else:
                break
        else:
            break

if __name__ == '__main__':
    main()
