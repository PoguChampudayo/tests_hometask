import requests
import os
with open('ya_token.txt', encoding='utf-8') as file:
    ya_token = file.read()

def get_YaDisk_headers(ya_token):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {ya_token}'
        }
        
def check_for_folder(folder_name):
    '''Checks if folder exists. Output: response 200 or 404'''
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {'path': folder_name}
    headers = get_YaDisk_headers(ya_token)
    response = requests.get(url, params=params, headers=headers)
    return response

def create_YaDisk_folder(folder_name):
    '''Creates folder on YaDisk if it's not there.'''
    if check_for_folder(folder_name).status_code == 404:
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': folder_name}
        headers = get_YaDisk_headers(ya_token)
        response = requests.put(url, params=params, headers=headers)
        if response.status_code != 201:
            print('Произошла ошибка при создании папки')
            os._exit(0)
        return response.status_code
    else:
        return 201

# create_YaDisk_folder('test')
    