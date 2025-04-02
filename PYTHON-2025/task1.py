
from sys import argv



london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}


device = input('Enter device name: ')
parameter = input('Enter parameter name (ios, model, vendor, location, ip): ')

# Chuyển tham số nhập vào thành chữ thường và tra cứu trong từ điển
device = device.lower()
parameter = parameter.lower()
print(london_co[device][parameter])

# Using .get() to safely access the device and parameter
device_info = london_co.get(device, {})
parameter_value = device_info.get(parameter, "Parameter not found")

print(parameter_value)
# print(london_co.get(device))


# print(london_co["r1"]["ip"])

# #Print 1 var
# print('device {}'.format(device))

# #Print 2 var
# print("1. IP %s is %s" % (device, parameter))
# print("2. IP {} is {}".format(device, parameter))
# print("3. IP {0} is {1}".format(device, parameter))
# print("4. IP {n} is {s}".format(n=device, s=parameter))
# print("5. IP " + str(device) + " is " + str(parameter))
# print("6. IP", device, "is", parameter)