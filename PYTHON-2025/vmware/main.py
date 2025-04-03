import requests
import urllib3
import json


# interface = input('Enter interface: ')
# ip = input('Enter ip address: ')
# mask = input('Enter mask: ')

def configure_intf(intf_name, ip, mask):
    print('interface', intf_name)
    print('ip address', ip, mask)
# configure_intf(interface,ip,mask)


def r_netbox():
    r = requests.get('https://api.github.com/events')
    print(r) #result Status code

r_netbox()