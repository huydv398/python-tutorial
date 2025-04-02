import ipaddress

# Ask user to enter the IP network in CIDR format (e.g., 10.1.1.0/24)
network_input = input('Enter the IP network (e.g., 10.1.1.0/24): ')

# Parse the network using ipaddress module
network = ipaddress.IPv4Network(network_input, strict=False)

# Extract network address and mask
network_address = network.network_address
netmask = network.netmask

# Function to convert IP address to binary format
def ip_to_binary(ip):
    return '.'.join(f'{octet:08b}' for octet in ip.split('.'))

# Display the Network Address in decimal and binary formats
print("\nNetwork:")
# Decimal format
print(f"{network_address}")
# # Binary format
# print(ip_to_binary(str(network_address)))

# # Display the Subnet Mask in decimal and binary formats
# print("\nMask:")
# # CIDR notation
# print(f"/{network.prefixlen}")
# # Decimal format
# print(f"{netmask}")
# # Binary format
# print(ip_to_binary(str(netmask)))