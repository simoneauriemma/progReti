import os
import sys
from datetime import datetime
import re
import glob
from os import path


try:
    output_directory = sys.argv[1]
    print('Analizzo la directory ' + output_directory + '\n')
except:
    print('Errore: parametri errati!\n')
    sys.exit("Assicurati di scrivere analyze.py '<path/to/input_directory>'")

print("\n")
start_time = datetime.now()
print("Current time: " + str(start_time))
print("\n")
print("Starting analysis...")
print("\n\n")

# Controllo se ci sia già il file di output
# Se c'è lo elimino, altrimenti l'esecuzione andrebbe in loop perchè
# si aprirebbe da solo e si scriverebbe all'interno all'infinito
if path.exists(output_directory + '/outputFile.txt'):
    os.remove(output_directory + 'outputFile.txt')

# Creo la lista che contiene i nomi di tutti i file nella directory test
files = glob.glob(output_directory + '/*.txt')

# Per ogni file in files
for file in files:
    found = False

    # Apro il file
    with open(file) as infile:

        for line in infile:
            x = re.search(r'\b[a-zA-Z_]+profile\b', line)
            if x:
                found = True

        # Se non c'è un match con niente, elimino il file
        if not found:
            os.remove(file)

print("\n\n")
end_time = datetime.now() - start_time
print("Total time:" + str(end_time))
print("\n")
print("\aAnalysis completed.")