import os, shutil, sys, getopt, itertools

downloads_path = None
'''
images = ('.jpg','.png','.jpeg','.gif')
video = ('.wmv','.avi','.mp4','.wmv','.mov','.mkv')
text = ('.doc','.docx','.pdf','.txt')
compressed = ('.rar','.zip')
dot = images + video + text + compressed
'''
extensions = [('.jpg','.png','.jpeg','.gif'),
        ('.wmv','.avi','.mp4','.wmv','.mov','.mkv'),
        ('.doc','.docx','.pdf','.txt'),
        ('.rar','.zip')]
extComp = [item for ext in extensions for item in ext]

def organize(file,ext):
    if ext in extComp:
        for order in extComp:
            folderCreation('Images')
            folderCreation('Videos')
            folderCreation('Compressed')
            folderCreation('TextFiles')
            if ext in extensions[0]:
                shutil.move(downloads_path+file,downloads_path+'/Images/'+file)
            if ext in extensions[1]:
                shutil.move(downloads_path+file,downloads_path+'/Videos/'+file)
            if ext in extensions[2]:
                shutil.move(downloads_path+file,downloads_path+'/Compressed/'+file)
            if ext in extensions[3]:
                shutil.move(downloads_path+file,downloads_path+'/TextFiles/'+file)
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
            print('Help')
            
def main():
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


if __name__=='__main__':
    main()