
import requests
import json
from header import list_link
from config import headers

    
# list all site
def list_site():
    url_api = list_link()["dcim"] + 'sites/'
    r = requests.get(url_api, headers=headers, verify=False)
    data = r.json()
    return data

def get_site():
    print("\nList Site:")
    for data in list_site()['results']:
        print("ID %s \t name: %s" % (data['id'], data['name']))
    while True:
        try:
            # Get user input and try to convert it to an integer
            site_id_input =  int(input("\nEnter ID site: ")) 
            return site_id_input
        except ValueError:
            # If the input is not a valid integer, show an error message and ask again
            print("Invalid input! Please enter a valid numeric ID.")
