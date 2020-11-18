import json
import sys
from urllib.parse import unquote


def parse_chlsj(output_directory, count, data):
    host = data['host']
    #client_address = data['clientAddress']
    method = data['method']
    request = data['request']
    response = data['response']

    if 'path' in data:
        path = data['path']
        line_sum = '# ' + method + ' ' + host + str(path)
    else:
        line_sum = '# ' + method + ' ' + host

    out_file = open(output_directory + '/' + method + ' - ' + host + '_' + str(count) + '.txt', 'w')

    out_file.write(line_sum)
    out_file.write('\n\n')

    # REQUEST
    out_file.write('+ Request')
    out_file.write('\n\n')

    # request header
    out_file.write('\t' + '> Headers' + '\n')

    for header in request['header']['headers']:
        out_file.write('\t\t')
        out_file.write(header['name'])
        out_file.write(': ')
        out_file.write(header['value'])
        out_file.write('\n')

    # request body

    out_file.write('\n\n\n')

    # RESPONSE
    response_code = response['status']
    out_file.write('+ Response (' + str(response_code) + ')')
    out_file.write('\n\n')

    # response header
    out_file.write('\t' + '> Headers' + '\n')

    for header in response['header']['headers']:
        out_file.write('\t\t')
        out_file.write(header['name'])
        out_file.write(': ')
        out_file.write(header['value'])
        out_file.write('\n')

    out_file.write('\n\n\n')

    # response body
    if 'body' in response:
        # Il campo body è presente

        if 'text' in response['body']:
            # Il campo body è presente
            out_file.write('\t\t')
            out_file.write('Response body text: ')
            out_file.write(unquote(response['body']['text']))
            out_file.write('\n\n')
            


    out_file.write('===========================================================================')
    out_file.write('\n\n\n')

    out_file.close()

try:
    in_file_name = sys.argv[1]
    output_directory = sys.argv[2]
    print('Converto il file ' + in_file_name + ' e metto le richieste in ' + output_directory + '\n')
except:
    print('Errore: parametri errati!\n')
    sys.exit("Assicurati di scrivere chlsj2json.py '<path/to/.chlsj>' '<path/to/output_directory>'")

print(output_directory)

if in_file_name.endswith('.chlsj'):
    with open(in_file_name) as in_file:
        datas = json.load(in_file)
        if len(datas) > 1:
            count = 1
            for data in datas:
                parse_chlsj(output_directory, count, data)
                count = count + 1
        else:
            parse_chlsj(output_directory, count, datas[0])

    print('Process complete!')

else:
    print('Unrecognized file type.')