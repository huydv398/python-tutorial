import requests
import urllib3
import json
from header import list_link
from tenancy import get_tenant
from config import headers
from dc_site import *


def add_device():
    name_dev =  input("Enter Name Device: ")
    url_api = list_link()["dcim"] + 'devices/'
    device_role_id = str(get_device_role())
    site_id = str(get_site())
    device_type = str(get_device_type())
    


    data = {
        "name": name_dev,
        "role": {
            "id": device_role_id
        },
        "site":{
            "id": site_id
        },
        "description":"description",
        "status":"active",
        "device_type":{
            "id": device_type
        }
        }

    r = requests.post(url_api, headers=headers, json=data, verify=False)

    print(r)



    
# list all device
def list_device():
    url_api = list_link()["dcim"] + 'devices/'
    r = requests.get(url_api, headers=headers, verify=False)
    data = r.json()
    return data

# list all role
def list_device_role():
    url_api = list_link()["dcim"] + 'device-roles/'

    r = requests.get(url_api, headers=headers, verify=False)
    data = r.json()
    return data
# list device type
def list_device_type():
    url_api = list_link()["dcim"] + 'device-types/'

    r = requests.get(url_api, headers=headers, verify=False)
    data = r.json()
    return data
# get detail vm
def get_detail_device(device_id):

    r_detail_vm = requests.get(list_link()["dcim"] + 'devices/' + device_id + '/', headers=headers, verify=False)
    detail_vm = r_detail_vm.json()
    return detail_vm
    # print(r_detail_vm) #result Status code

def get_device_type():
    for data in list_device_type()['results']:
        print("ID: %s \t %s-%s" % (data['id'], data['manufacturer']['name'], data['display']))
    while True:
        try:
            # Get user input and try to convert it to an integer
            device_type_input =  int(input("\nEnter ID Device Type: ")) 
            return device_type_input
        except ValueError:
            # If the input is not a valid integer, show an error message and ask again
            print("Invalid input! Please enter a valid numeric ID.")

def get_device_role():
    print("\nShow Device Role!!!")
    for data in list_device_role()['results']:
        print("ID %s \t name: %s" % (data['id'], data['name']))
    while True:
        try:
            # Get user input and try to convert it to an integer
            device_role_input =  int(input("\nEnter ID Device Role: ")) 
            return device_role_input
        except ValueError:
            # If the input is not a valid integer, show an error message and ask again
            print("Invalid input! Please enter a valid numeric ID.")

def get_device_id():
    while True:
        valid_dev = [id['id'] for id in list_device()['results']]
        try:
            # Get user input and try to convert it to an integer
            device_id_input =  int(input("Enter id Device: ")) 
            if device_id_input in valid_dev:
                return device_id_input
            else:
                print("Invalid status! Please enter one of: %s" % ", ".join(valid_dev))
        except Exception as e:
            print(f"Error: {e}. Please try again.")

def update_description(detail_vm):
    while True:
        try:
            current = detail_vm['description'] if detail_vm.get('description') else 'unknown'
            description = input("\n[1]. Update Description (%s): " % current).strip()

            # If user just presses Enter, return the current status
            if not description:
                return current
            if description:
                return description
        except Exception as e:
            print(f"Error: {e}. Please try again.")

#Cập nhật status DEV
def get_status(detail_vm):
    valid_statuses = ['offline', 'active', 'planned', 'staged', 'failed', 'inventory', 'decommissioning']

    while True:
        try:
            current_status = detail_vm['status']['value'] if detail_vm.get('status') and detail_vm['status'].get('value') else 'unknown'
            status = input("[2]. Status (%s): " % current_status).strip().lower()

            # If user just presses Enter, return the current status
            if not status:
                return current_status

            if status in valid_statuses:
                return status
            else:
                print("Invalid status! Please enter one of: %s" % ", ".join(valid_statuses))
        except Exception as e:
            print(f"Error: {e}. Please try again.")



#Cập nhật tenant
def update_tenant(detail_vm):
    # đưa json đầu vào chuyển thành list
    valid_tenant = [id['name'] for id in get_tenant()['results']]

    while True:
        try:
            current_tenant = detail_vm['tenant']['name'] if detail_vm.get('tenant') and detail_vm['tenant'].get('name') else 'unknown'
            print('\nSelect Tenant: ', valid_tenant)
            tenant = input("[3]. Tenant (%s): " % current_tenant)

            # If user just presses Enter, return the current status
            if not tenant:
                return current_tenant

            if tenant in valid_tenant:
                return tenant
            else:
                print("Invalid tenant! Please enter one of: %s" % ", ".join(valid_tenant))
        except Exception as e:
            print(f"Error: {e}. Please try again.")

#Cập nhật serial
def update_serial(detail_vm):
    # valid_statuses = ['offline', 'active', 'planned', 'staged', 'failed', 'inventory', 'decommissioning']

    while True:
        try:
            current = detail_vm['serial'] if detail_vm.get('serial') else 'unknown'
            serial = input("[4]. Serial number (%s): " % current).strip().upper()

            # If user just presses Enter, return the current status
            if not serial:
                return current
            if serial:
                return serial
        except Exception as e:
            print(f"Error: {e}. Please try again.")
            
def update_device():
    print("\n## Function Update info Device")
    for data in list_device()['results']:
        # print(data)
        print("ID %s \tis name: %s" % (data['id'], data['name']))

    
    #lấy ra được ID của device
    device_id = str(get_device_id())

    #dùng lại function get_detail_device toàn bộ dev list ra màn hình
    detail_vm = get_detail_device(device_id)

    

    print("\nUpdate Server: %s" %(detail_vm['name']))
    print('Complete field below!')

    #lây input cho các body để update
    description = update_description(detail_vm)
    status = get_status(detail_vm)
    tenant = update_tenant(detail_vm)
    serial = update_serial(detail_vm)
    
    print("Result device ID: %s\n1. Description: %s\n2. Status: %s\n3. Tenant: %s\n4. Serial: %s" % (device_id, description, status, tenant, serial))

    print("\n## Confirm Update device")
    url_api = list_link()["dcim"] + 'devices/' + device_id + '/'
    data = {
        "status": status,
        "description": description,
        "serial": serial,
        "tenant": {
            "name": tenant
        }
    }

    # Confirm trước khi update, chọn y - tiếp tục, chọn n - hủy bỏ.
    while True:

        choice = input("Do you want to continue? (y/n): ").strip().lower()
        if choice == 'y':
            print("Updating...\n")
            r = requests.patch(url_api, headers=headers, json=data, verify=False)
            print(r) #result Status code
            return
            # Code to continue doing something...
        elif choice == 'n':
            print("Update  !!!")
            return
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
