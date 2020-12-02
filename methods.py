import os
import re
from constant import Constant
from os import path
import json


def analyze(request, line, output_file):

    found = False
    info = []

    if re.search(Constant.NOME_COGNOME, line):
        # print("'NOME_COGNOME' trovate in " + line)
        info.append("Nome_Cognome")
        found = True

    if re.search(Constant.EMAIL, line):
        # print("'EMAIL' trovate in " + line)
        info.append("Email")
        found = True

    if re.search(Constant.GENDER, line):
        # print("'GENDER' trovate in " + line)
        info.append("Gender")
        found = True

    # if re.search(Constant.ALTEZZA, line):
    # # print("'ALTEZZA' trovate in " + line)
    # info.append("Altezza")

    if re.search(Constant.PESO, line):
        # print("'PESO' trovate in " + line)
        info.append("Peso")
        found = True

    if re.search(Constant.BIRTHDATE, line):
        # print("'BIRTHDATE' trovate in " + line)
        info.append("Birthdate")
        found = True

    if re.search(Constant.CELLULARE, line):
        # print("'CELLULARE' trovate in " + line)
        info.append("Cellulare")
        found = True

    if re.search(Constant.ALTAVILLA, line):
        # print("'ALTAVILLA' trovate in " + line)
        info.append("Altavilla")
        found = True

    if re.search(Constant.MATTINE, line):
        # print("'MATTINE' trovate in " + line)
        info.append("Mattine")
        found = True

    if re.search(Constant.POSTAL_CODE, line):
        # print("'POSTAL_CODE' trovate in " + line)
        info.append("Postal_Code")
        found = True

    if re.search(Constant.PHONE_NAME, line):
        # print("'PHONE_NAME' trovate in " + line)
        info.append("Phone_Name")
        found = True

    if re.search(Constant.CARRIER, line):
        # print("'CARRIER' trovate in " + line)
        info.append("Carrier")
        found = True

    if re.search(Constant.UDID, line):
        # print("'UDID' trovate in " + line)
        info.append("UDID")
        found = True

    if found:
        output_file.write("Ho trovato ")
        for inf in info:
            output_file.write(inf.upper() + ", ")
        output_file.write("\n\n")
        output_file.write(json.dumps(request, indent=4, sort_keys=True))
        output_file.write('\n\n####################################\n\n')


# ------------ GET & DELETE ------------
# Funzione per analizzare le GET REQUEST
def analyze_get_delete_request(request, output_file):
    # URL
    if 'url' in request:
        url = request['url']
        analyze(request, url, output_file)

    # HEADERS
    if 'headers' in request:
        headers = request['headers']
        for item in headers:
            if 'value' in item:
                header_value = item['value']
                analyze(request, header_value, output_file)
            """
            if 'name' in item:
                header = item['name']
                if header == 'user-agent':
                    user_agent = item['value']
                    # analyze(request, user_agent)
            """

    # QUERY_STRING
    if 'queryString' in request:
        query_string = request['queryString']
        for item in query_string:
            if 'value' in item:
                query_string_value = item['value']
                analyze(request, query_string_value, output_file)

    # COOKIES
    if 'cookies' in request:
        cookies = request['cookies']
        for cookie in cookies:
            if 'value' in cookie:
                cookie_value = item['value']
                analyze(request, cookie_value, output_file)


# Funzione per analizzare le GET RESPONSE
def analyze_get_delete_response(response, output_file):
    pass

# ------------ :GET & DELETE ------------


# ------------ POST & PUT ------------
def analyze_post_put_request(request, output_file):
    # URL
    if 'url' in request:
        url = request['url']
        analyze(request, url, output_file)

    # HEADERS
    if 'headers' in request:
        headers = request['headers']
        for item in headers:
            if 'value' in item:
                header_value = item['value']
                analyze(request, header_value, output_file)
            """
            if 'name' in item:
                header = item['name']
                if header == 'user-agent':
                    user_agent = item['value']
                    # analyze(request, user_agent)
            """

    # QUERY_STRING
    if 'queryString' in request:
        query_string = request['queryString']
        for item in query_string:
            if 'value' in item:
                query_string_value = item['value']
                analyze(request, query_string_value, output_file)

    # COOKIES
    if 'cookies' in request:
        cookies = request['cookies']
        for cookie in cookies:
            if 'value' in cookie:
                cookie_value = item['value']
                analyze(request, cookie_value, output_file)

    # POST_DATA
    if 'postData' in request:
        # POST_DATA
        postData = request['postData']
        if 'text' in postData:
            text = postData['text']
            analyze(request, text, output_file)
# ------------ :POST & PUT ------------


# ------------ PATCH ------------
# ------------ :PATCH ------------
