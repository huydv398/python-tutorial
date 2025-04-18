import requests
from header import list_link
from config import headers

def input_tenant_id():
    while True:
        try:
            # Get user input and try to convert it to an integer
            tenant_id_input =  int(input("Enter id tenant: ")) 
            return tenant_id_input
        except ValueError:
            # If the input is not a valid integer, show an error message and ask again
            print("Invalid input! Please enter a valid numeric ID.")

# get tenant
def get_tenant():
    # tenant_name = str(input("Enter name tenant: "))
    url_api = list_link()["tenancy"] + 'tenants/'

    r = requests.get(url_api, headers=headers, verify=False)
    data = r.json()
    return data

# add new tenant
def add_tenant():
    tenant_name = str(input("Enter name tenant: "))
    url_api = list_link()["tenancy"] + 'tenants/'

    data = {
        'name': tenant_name,
        'slug': tenant_name.replace(" ", "-")
    }
    r = requests.post(url_api, headers=headers, json=data, verify=False)
    print(r) #result Status code

# update tenant
def update_tenant():
    print("\n## Update Tenant")
    for data in get_tenant()['results']:
        print("ID %s \t name: %s" % (data['id'], data['name']))

    input_tenant_id()

    tenant_id = str(input_tenant_id())
    tenant_name = str(input("\nEnter name tenant: "))   
    url_api = list_link()["tenancy"] + 'tenants/' + tenant_id + '/'
    data = {
        'name': tenant_name
    }
    r = requests.patch(url_api, headers=headers, json=data, verify=False)
    print(r) #result Status code
    if r.status_code == 200:
        print("Update successful!")
        # print("Update successful:", r.json())
        return
    else:
        print("Error:", r.text)
# Remove tenant
def remove_tenant():
    print("\n## Delete Tenant")

    tenant_id = str(input_tenant_id())

    url_api = url + '/api/tenancy/tenants/' + tenant_id + '/'
    r = requests.delete(url_api, headers=headers, verify=False)
    print(r) #result Status code
    get_tenant()
