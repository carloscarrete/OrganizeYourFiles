import os
import shutil

downloads_path = '/home/carlos/Downloads/'
images = ('.jpg','.png','.jpeg','.gif')
video = ('.wmv','.avi','.mp4','.wmv','.mov')
text = ('.doc','.docx','.pdf','.txt')
"""
if not os.path.exists('/home/carlos/Desktop/Archivos'):
    os.mkdir('/home/carlos/Desktop/Archivos')
else:
    print('Ya existe')
name = "Nota.txt"
shutil.move(downloads_path+'/Nota.txt','/home/carlos/Desktop/Archivos/'+name)
"""

def organize(file,ext):
    for order in images:
        if ext == order:
            shutil.move(downloads_path+file,'/home/carlos/Desktop/'+file)



for fileX in os.listdir(downloads_path):
    name, ext = os.path.splitext(fileX)
    organize(fileX,ext)
'''
print(os.listdir(downloads_path))
print('-----------------')
print(os.path.splitext(downloads_path))
'''