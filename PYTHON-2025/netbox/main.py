import requests
import urllib3
import json
from tenancy import get_tenant, add_tenant, update_tenant
from device import list_device, update_device, add_device
from dc_site import *
from header import list_link

urllib3.disable_warnings()



def confirm():
    while True:
        choice = input("Do you want to continue? (y/n): ").strip().lower()
        if choice == 'y':
            print("Continuing...\n")
            # Code to continue doing something...
        elif choice == 'n':
            print("Exiting loop.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")



def list_cluster():
    url_api = url + '/api/virtualization/clusters/'

    r = requests.get(url_api, headers=headers, verify=False)
    data = r.json()
    for data in data['results']:
        # print(data)
        print("ID %s \tis name: %s" % (data['id'], data['name']))



def show_func():
    # print("Select function!!!")

    data = [
        ["Show", "[1]. Device", "[2]. Tenancy", "[3]. Sites"],
        ["Create", "[4]. Device ", "[5]. Tenancy", "[6]. "],
        ["Update", "[7]. Device", "[8]. Tenancy", "[9]. "],
        ["Delete", "[10]. Device", "[11]. Tenancy", "[12]. "]
    ]

    for row in data:
        print("{:<15} {:<20} {:<20} {:<20}".format(*row))
    
def response_func(result:any):
    #for print data
    for data in result:
        print("ID %s \t name: %s" % (data['id'], data['name']))
    return 

def main():
    
    while True:
        print("\n\nDEV-API_NETBOX...")
        show_func()
        choice = input("\nSelect function!!! [Number] ").strip().lower()
        if choice == '1':
            print("\nShow Device...\n")
            # result = list_device()
            # response_func(result['results'])
            for data in list_device()['results']:
                print("ID %s \t name: %s" % (data['id'], data['name']))

        
        elif choice == '2':
            print("\nShow Tenancy!!!")
            for data in get_tenant()['results']:
                print("ID %s \t name: %s" % (data['id'], data['name']))
            # return
        
        elif choice == '3':
            print("\nShow Site!!!")
            # list_site()
            for data in list_site()['results']:
                print("ID %s \t name: %s" % (data['id'], data['name']))
        
        elif choice == '4':
            print("\nAdd new Device !!!")
            add_device()

        elif choice == '5':
            print("Add Tenancy!!!")
            add_tenant()
        elif choice == '6':
            print("Function not Available!!!")
            
        elif choice == '7':
            print("Update Device!!!")
            update_device()
        elif choice == '8':
            print("Update Tenancy !!!")
            update_tenant()
        elif choice == '9':
            print("Function not Available!!!")
            
        elif choice == '10':
            print("Delete Device !!!")
            
        elif choice == '11':
            print("Delete Tenancy !!!")
            
        else:
            print("Invalid input. Please enter number '1/2/3/...'.")
main()