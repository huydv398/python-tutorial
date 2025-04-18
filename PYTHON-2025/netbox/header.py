import requests
def list_link():
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Token da6b8955f31e800827e0c4fd1dfc3316f1024683'
        }
    url = 'https://172.16.66.29/'
    r = requests.get(url+'api', headers=headers, verify=False)
    link = r.json()
    return link