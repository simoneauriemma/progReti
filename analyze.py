import os
import sys
import json
import methods
from datetime import datetime
from os import path

try:
    input_file = sys.argv[1]
    print('\nAnalizzo il file ' + input_file + '\n')
except:
    print('\nErrore: parametri errati!\n')
    sys.exit('Assicurati di scrivere analyze.py "<path/to/input_file>"')

start_time = datetime.now()
print('Analisi iniziata...\n\n')

# Apro il file
with open(input_file) as infile:
    # Converto il file in json
    json_file = json.load(infile)

    # Recupero le entries (= richieste effettuate)
    json_entries = json_file["log"]["entries"]

    # Creo la cartella di output
    output_folder = './results'
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # Creo il file di output
    input_file_name = input_file.split('/')[-1].split('.')[0]

    if path.exists(output_folder + '/' + input_file_name + '.txt'):
        os.remove(output_folder + '/' + input_file_name + '.txt')

    output_file = open(output_folder + '/' + input_file_name + '.txt', 'w')

    # Le scorro una ad una
    for index, http_request in enumerate(json_entries):

        # Controllo il method per recuperare solo i campi che mi servono
        #GET & DELETE
        if http_request['request']['method'] == 'GET' or http_request['request']['method'] == 'DELETE':

            # REQUEST
            request = http_request['request']
            methods.analyze_get_delete_request(request, output_file)

            # RESPONSE
            response = http_request['response']
            methods.analyze_get_delete_response(response, output_file) #TODO

        # POST & PUT
        elif http_request['request']['method'] == 'POST' or http_request['request']['method'] == 'PUT':

            # REQUEST
            request = http_request['request']
            methods.analyze_post_put_request(request, output_file)

            # RESPONSE
            #TODO

        # PATCH
        elif http_request['request']['method'] == 'PATCH':
            pass

        else:
            print(http_request['request']['method'])

    output_file.close()

print('\n')
print('\aAnalisi completata.')
end_time = datetime.now() - start_time
print('Tempo totale:' + str(end_time) + '\n')
