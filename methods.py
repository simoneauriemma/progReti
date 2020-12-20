import os
import re
from constant import Constant
from os import path
import json
import re


def analyze(request, items, output_file, index):
    
    # Booleano per stampare oppure no le informazioni all'interno del file:
    # - Se found = false -> non è stato trovato nulla -> non scrivere la request nel file
    # - Se found = true -> è stato trovata qualche informazione -> inserisci l'informazione in info e scrivi la request nel file
    found = False
    info = []

    for line in items:

        if re.findall(Constant.NOME_COGNOME, line):
            # print("'NOME_COGNOME' trovate in " + line)
            if not 'Nome_Cognome' in info:
                info.append("Nome_Cognome")
            found = True

        if re.findall(Constant.EMAIL, line):
            # print("'EMAIL' trovate in " + line)
            if not 'Email' in info:
                info.append("Email")
            found = True

        if re.findall(Constant.GENDER, line):
            # print("'GENDER' trovate in " + line)
            if not 'Gender' in info:
                info.append("Gender")
            found = True

        # if re.findall(Constant.ALTEZZA, line):
        # # print("'ALTEZZA' trovate in " + line)
        # info.append("Altezza")

        if re.findall(Constant.PESO, line):
            # print("'PESO' trovate in " + line)
            if not 'Peso' in info:
                info.append("Peso")
            found = True

        if re.findall(Constant.BIRTHDATE, line):
            # print("'BIRTHDATE' trovate in " + line)
            if not 'Birthdate' in info:
                info.append("Birthdate")
            found = True

        if re.findall(Constant.CELLULARE, line):
            # print("'CELLULARE' trovate in " + line)
            if not 'Cellulare' in info:
                info.append("Cellulare")
            found = True

        if re.findall(Constant.ALTAVILLA, line):
            # print("'ALTAVILLA' trovate in " + line)
            if not 'Altavilla' in info:
                info.append("Altavilla")
            found = True

        if re.findall(Constant.MATTINE, line):
            # print("'MATTINE' trovate in " + line)
            if not 'Mattine' in info:
                info.append("Mattine")
            found = True

        if re.findall(Constant.POSTAL_CODE, line):
            # print("'POSTAL_CODE' trovate in " + line)
            if not 'Postal_Code' in info:
                info.append("Postal_Code")
            found = True

        if re.findall(Constant.PHONE_NAME, line):
            # print("'PHONE_NAME' trovate in " + line)
            if not 'Phone_Name' in info:
                info.append("Phone_Name")
            found = True

        if re.findall(Constant.CARRIER, line):
            # print("'CARRIER' trovate in " + line)
            if not 'Carrier' in info:
                info.append("Carrier")
            found = True

        if re.findall(Constant.UDID, line):
            # print("'UDID' trovate in " + line)
            if not 'UDID' in info:
                info.append("UDID")
            found = True

        if re.findall(Constant.IDFA, line):
            # print("'IDFA' trovate in " + line)
            if not 'IDFA' in info:
                info.append("IDFA")
            found = True

    if found:
        output_file.write("Ho trovato nella richiesta " + str(index) + ": ")
        for inf in info:
            output_file.write(inf.upper() + ", ")
        output_file.write("\n\n")
        output_file.write(json.dumps(request, indent=4, sort_keys=True))
        output_file.write('\n\n####################################\n\n')


# ------------ GET & DELETE ------------
# Funzione per analizzare le GET REQUEST
def analyze_get_delete_request(request, output_file, index):
    items = []

    # URL
    if 'url' in request:
        url = request['url']
        items.append(url)


    # HEADERS
    if 'headers' in request:
        headers = request['headers']
        for item in headers:
            if 'value' in item:
                header_value = item['value']
                items.append(header_value)
                # analyze(request, header_value, output_file, index)

    # QUERY_STRING
    if 'queryString' in request:
        query_string = request['queryString']
        for item in query_string:
            if 'value' in item:
                query_string_value = item['value']
                items.append(query_string_value)
                #analyze(request, query_string_value, output_file, index)

    # COOKIES
    if 'cookies' in request:
        cookies = request['cookies']
        for cookie in cookies:
            if 'value' in cookie:
                cookie_value = item['value']
                items.append(cookie_value)
                #analyze(request, cookie_value, output_file, index)

        analyze(request, items, output_file, index)


# Funzione per analizzare le GET RESPONSE
def analyze_get_delete_response(response, output_file, index):
    pass

# ------------ :GET & DELETE ------------


# ------------ POST & PUT ------------
def analyze_post_put_request(request, output_file, index):
    items = []

    # URL
    if 'url' in request:
        url = request['url']
        items.append(url)
        #analyze(request, url, output_file, index)

    # HEADERS
    if 'headers' in request:
        headers = request['headers']
        for item in headers:
            if 'value' in item:
                header_value = item['value']
                items.append(header_value)
                #analyze(request, header_value, output_file, index)


    # QUERY_STRING
    if 'queryString' in request:
        query_string = request['queryString']
        for item in query_string:
            if 'value' in item:
                query_string_value = item['value']
                items.append(query_string_value)
                #analyze(request, query_string_value, output_file, index)

    # COOKIES
    if 'cookies' in request:
        cookies = request['cookies']
        for cookie in cookies:
            if 'value' in cookie:
                cookie_value = item['value']
                items.append(cookie_value)
                #analyze(request, cookie_value, output_file, index)

    # POST_DATA
    if 'postData' in request:
        # POST_DATA
        postData = request['postData']
        if 'text' in postData:
            text = postData['text']
            items.append(text)
            #analyze(request, text, output_file, index)

        if 'params' in postData:
            params = postData['params']
            for param in params:
                if 'value' in param:
                    items.append(param['value'])
                    #analyze(request, param['value'], output_file, index)

    analyze(request, items, output_file, index)
# ------------ :POST & PUT ------------


# ------------ PATCH ------------
# ------------ :PATCH ------------