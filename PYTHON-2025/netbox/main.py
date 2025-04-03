import requests
import urllib3
import json

urllib3.disable_warnings()


url = 'https://172.16.66.29'
headers = {
    'Accept': 'application/json',
    'Authorization': 'Token da6b8955f31e800827e0c4fd1dfc3316f1024683'
    }
# interface = input('Enter interface: ')
# ip = input('Enter ip address: ')
# mask = input('Enter mask: ')

def configure_intf(intf_name, ip, mask):
    print('interface', intf_name)
    print('ip address', ip, mask)
# configure_intf(interface,ip,mask)

# add new tenant
def add_tenant():
    tenant_name = str(input("Enter name tenant: "))
    url_api = url + 'api/tenancy/tenants/'

    data = {
        'name': tenant_name,
        'slug': tenant_name.replace(" ", "-")
    }
    r = requests.post(url_api, headers=headers, json=data, verify=False)
    # print(r) #result Status code

# get tenant
def get_tenant():
    # tenant_name = str(input("Enter name tenant: "))
    url_api = url + '/api/tenancy/tenants/'

    r = requests.get(url_api, headers=headers, verify=False)
    data = r.json()
    for id in data['results']:
        print("ID %s \tis name %s" % (id['id'], id['name']))
# get_tenant()


# update tenant
def update_tenant():
    print("\n## Update Tenant")
    def get_tenant_id():
        while True:
            try:
                # Get user input and try to convert it to an integer
                tenant_id_input =  int(input("Enter id tenant: ")) 
                return tenant_id_input
            except ValueError:
                # If the input is not a valid integer, show an error message and ask again
                print("Invalid input! Please enter a valid numeric ID.")

    tenant_id = str(get_tenant_id())
    tenant_name = str(input("\nEnter name tenant: "))   
    url_api = url + '/api/tenancy/tenants/' + tenant_id + '/'
    data = {
        'name': tenant_name
    }
    r = requests.patch(url_api, headers=headers, json=data, verify=False)
    print(r) #result Status code
    if r.status_code == 200:
        print("Update successful:", r.json())
        get_tenant()
    else:
        print("Error:", r.text)


# Remove tenant
def remove_tenant():
    print("\n## Delete Tenant")
    def get_tenant_id():
        while True:
            try:
                # Get user input and try to convert it to an integer
                tenant_id_input =  int(input("Enter ID tenant: ")) 
                return tenant_id_input
            except ValueError:
                # If the input is not a valid integer, show an error message and ask again
                print("Invalid input! Please enter a valid numeric ID.")
    tenant_id = str(get_tenant_id())

    url_api = url + '/api/tenancy/tenants/' + tenant_id + '/'
    r = requests.delete(url_api, headers=headers, verify=False)
    print(r) #result Status code
    get_tenant()

# list all device
def list_device():
    url_api = url + '/api/dcim/devices/'

    r = requests.get(url_api, headers=headers, verify=False)
    data = r.json()
    for data in data['results']:
        print(data)
        # print("name %s" % (id['id'], data['name']))
# list_device()

# list all role
def list_device_role():
    url_api = url + '/api/dcim/device-roles/'

    r = requests.get(url_api, headers=headers, verify=False)
    data = r.json()
    for data in data['results']:
        # print(data)
        print("ID %s \tis name: %s" % (data['id'], data['name']))


# add device
def r_netbox():
    # tenant_name = str(input("Enter name tenant: "))
    url_api = url + '/api/dcim/devices/'
    def get_device_role():
        list_device_role()
        while True:
            try:
                # Get user input and try to convert it to an integer
                device_role_input =  int(input("Enter ID Device Role: ")) 
                return device_role_input
            except ValueError:
                # If the input is not a valid integer, show an error message and ask again
                print("Invalid input! Please enter a valid numeric ID.")
    device_role_id = str(get_device_role())

    data = {
        "name":"huydv1234",
        "role":{
            "id":"1"
        },
        "site":{
            "id":"1"
        },
        "description":"description",
        "status":"active",
        "device_type":{
            "model":"PowerEdge R630"
        }
        }

    # r = requests.post(url_api, headers=headers, json=data, verify=False)


    print(device_role_id) #result Status code

r_netbox()
