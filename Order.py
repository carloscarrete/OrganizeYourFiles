import os
import shutil

downloads_path = '/home/carlos/Downloads/'
images = ('.jpg','.png','.jpeg','.gif')
video = ('.wmv','.avi','.mp4','.wmv','.mov','.mkv')
text = ('.doc','.docx','.pdf','.txt')
compressed = ('.rar','.zip')

def organize(file,ext):
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

    if ext =="":
        if not os.path.isdir(downloads_path+file):
            folderCreation('Others')
            shutil.move(downloads_path+file,downloads_path+'/Others/'+file)


def folderCreation(FolderName):
    folderName = FolderName
    if not os.path.exists(downloads_path+'/'+folderName):
        os.mkdir(downloads_path+'/'+folderName)
        print(folderName + ' has been created!')


def main():
    for fileX in os.listdir(downloads_path):
        name, ext = os.path.splitext(fileX)
        organize(fileX,ext)
    print('-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*')
    print('All files were organized correctly.!')


if __name__=='__main__':
    main()