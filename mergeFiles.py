import os
from os import path
import sys
import glob

# Controllo se ci sia già il file di output
# Se c'è lo elimino, altrimenti l'esecuzione andrebbe in loop perchè
# si aprirebbe da solo e si scriverebbe all'interno all'infinito
if path.exists("test/outputFile.txt"):
    os.remove("test/outputFile.txt")

# Creo la lista che contiene i nomi di tutti i file nella directory test
files = glob.glob("test/*.txt")

# Apro un nuovo file e ci scrivo tutto il contenuto di tutti i file
with open('test/outputFile.txt', 'w') as outfile:
    for fname in files:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

for file in files:
    os.remove(file)