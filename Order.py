import os, shutil, sys, getopt

downloads_path = None
images = ('.jpg','.png','.jpeg','.gif')
video = ('.wmv','.avi','.mp4','.wmv','.mov','.mkv')
text = ('.doc','.docx','.pdf','.txt')
compressed = ('.rar','.zip')
dot = images + video + text + compressed
def organize(file,ext):
    if ext in (dot):
        for order in images:
            folderCreation('Images')
            if ext == order:
                shutil.move(downloads_path+file,downloads_path+'/Images/'+file)
        for order in video:
            folderCreation('Videos')
            if ext == order:
                shutil.move(downloads_path+file,downloads_path+'/Videos/'+file)
        for order in compressed:
            folderCreation('Compressed')
            if ext == order:
                shutil.move(downloads_path+file,downloads_path+'/Compressed/'+file)
        for order in text:
            folderCreation('TextFiles')
            if ext == order:
                shutil.move(downloads_path+file,downloads_path+'/TextFiles/'+file)

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


if __name__=='__main__':
    main()