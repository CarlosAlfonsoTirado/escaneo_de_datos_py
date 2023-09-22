import scapy.all as scapy
import optparse
import netifaces

def get_interface_ip():
    # Encuentra la dirección IP de la primera interfaz activa
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface != 'lo':
            addrs = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addrs:
                return addrs[netifaces.AF_INET][0]['addr']
    return None

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    arp_request_broatcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broatcast, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac":  element[1].hwsrc}
        client_list.append(client_dict)
    return client_list
        
def print_result(result_list):
    print("\nIP\t\t\tMAC address\n--------------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])
        

interface_ip = get_interface_ip()

if interface_ip:
    scan_result = scan(interface_ip + "/24")
    print_result(scan_result)
else:
    print("No tienes conexion a una red\n no se pudo determinar una IP")
