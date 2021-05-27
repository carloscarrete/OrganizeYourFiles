import os, shutil, sys, getopt, time, colorama
from colorama import Fore

downloads_path = None
extensions = [('.jpg','.png','.jpeg','.gif', '.bmp', '.pict', '.psd','.tif'),   #Images
        ('.wmv','.avi','.mp4','.wmv','.mov','.mkv', '.mpg'),                    #Video
        ('.doc','.docx','.pdf','.txt','.rtf','.wpd','.wps'),                    #Text Files
        ('.rar','.zip','.tar'),                                                 #Compressed Files
        ('.aac', '.au', '.mid', '.mp3', '.ra', '.snd', '.wma', '.wav')]         #Audio                                         
extComp = [item for ext in extensions for item in ext]

def organize(file,ext):
    if ext in extComp:
        for order in extComp:
            folderCreation('Images')
            folderCreation('Videos')
            folderCreation('Compressed')
            folderCreation('TextFiles')
            folderCreation('Audio')
            if ext in extensions[0]:
                shutil.move(downloads_path+file,downloads_path+'/Images/'+file)
            if ext in extensions[1]:
                shutil.move(downloads_path+file,downloads_path+'/Videos/'+file)
            if ext in extensions[2]:
                shutil.move(downloads_path+file,downloads_path+'/TextFiles/'+file)      
            if ext in extensions[3]:
                shutil.move(downloads_path+file,downloads_path+'/Compressed/'+file)
            if ext in extensions[4]:
                shutil.move(downloads_path+file,downloads_path+'/Audio/'+file)
            return
    else:
        if os.path.isfile(downloads_path+file) and not os.path.isdir(downloads_path+file):
            folderCreation('Others')
            shutil.move(downloads_path+file,downloads_path+'/Others/'+file)

def folderCreation(FolderName):
    folderName = FolderName
    if not os.path.exists(downloads_path+'/'+folderName):
        os.mkdir(downloads_path+'/'+folderName)
        print(folderName + ' has been created!')


def checkArgvs():
    argv = sys.argv[1:]
    try:
        opts, argvs = getopt.getopt(argv,"d:h",['help'])
    except getopt.GetoptError as Err:
        print('Error, please check the argument: ',Err)
        sys.exit(2)
    for op, ag in opts:
        global downloads_path
        if ag == 'dow':
            downloads_path='/home/carlos/Downloads/'
            print('Downloads has been established')
            print(downloads_path)
        elif ag == 'doc':
            downloads_path='/home/carlos/'
            print('Documents has been established')
        if op in ('-h','--help'):
            help()


def help():
    print('-*-*-*This is a little help for helping how to use this script for organizing your files.-*-*-*')
    print('In order to use this script its necessary to pass as a parameter what will be the folder to sort the files inside that folder.') 
    print('By default comes the option to order the Downloads folder and the Home folder (Caution: it is necessary to set your path and user name inside the script, because by default comes mine which is /home/carlos/ and /home/carlos/Downloads, so you will have to configure this to your needs.')
    print('If you are using Linux you can set up your alias to simplify the way that you use the script')
    print('//////////////////////////////////////////////////')
    print('So, the first step after once you have configured your folders to organize, you must type in the terminal like this:')
    print(Fore.CYAN +'* python Order.py -d ag1')
    print(Fore.RESET +'Where python: Order.py is the script')
    print(Fore.CYAN +'* -d is the argv for directory')
    print('* agv1 is the name of folder that is goig to organize, in my case in the script i got dow for downloads and doc for documents/home')
    print(Fore.RESET +'So....if you wanna order the Downloads folder, you must type:')
    print('python Order.py -d dow')
    print('And that way, the script starting to organize all files in that folder')
    print('//////////////////////////////////////////////////')     
def main():
    start = time.time()
    checkArgvs()
    if downloads_path != None:
        for fileX in os.listdir(downloads_path):
            if not fileX.startswith('.'):
                name, ext = os.path.splitext(fileX)
                organize(fileX,ext)
            #print(downloads_path+'/'+fileX +' has been moved correctly!')
        print('-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*')
        print('All files were organized correctly.!')
        print('New Version')
        end = time.time()
        print('Final time: ', (end-start))


if __name__=='__main__':
    main()