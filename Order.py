import os
import shutil

downloads_path = '/home/carlos/Downloads'
images = ('.jpg','.png','.jpeg','.gif')
video = ('.wmv','.avi','.mp4','.wmv','.mov')
text = ('.doc','.docx','.pdf','.txt')

if not os.path.exists('/home/carlos/Desktop/Archivos'):
    os.mkdir('/home/carlos/Desktop/Archivos')
else:
    print('Ya existe')
name = "Nota.txt"
shutil.move(downloads_path+'/Nota.txt','/home/carlos/Desktop/Archivos/'+name)