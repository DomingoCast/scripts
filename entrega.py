# Poner los proyectos en una carpeta, ejecutar programa y generara un zip y 
# una carpeta con los .cs llamado entrega

import os
import shutil

d = '.'
subdirs = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
os.mkdir("entrega")
for dir in subdirs:
    for file in os.listdir(dir):
        if file.endswith(".cs"):
            shutil.copy(os.path.join(dir, file), os.path.join('entrega', dir+'.cs'))
            break

shutil.make_archive('entrega', 'zip', 'entrega')
print(os.listdir("entrega"))

# shutil.rmtree('entrega') # para borrar la carpeta con los .cs 
