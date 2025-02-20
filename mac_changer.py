import subprocess
import optparse
import re

#funciones
def get_aguments():
#parcer sirve para crear los comandos 
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest = "interface", help = "Interface para cambiar la direccion MAC")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "Nueva direccion MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Indica la interfaz, usa --help para mas informacion")
    elif not options.new_mac:
        parser.error("[-] Indica la nueva direccion MAC, usa --help para mas informacion")
    return options

def change_mac(interface, new_mac):
#esto es todo el codigo, lo que hace el programa
    print("[+] La direccion MAC cambio para " + interface + " a " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    #Con esto revisamos si la direccion MAC cambio adecuadamente 
    #Se hace referencia a exprecion regular, y este es el codigo que se necesita para usarse
    #la r sola significa read
    #para obtener la expresion regular lo buscamos en pythex,org 
    ifconfig_results = subprocess.check_output(["ifconfig", options.interface])
    ifconfig_results = ifconfig_results.decode('utf-8')
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_results)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print ("[-] No se pudo leer la direccion MAC")

#Aqui llama las opciones y los argumentos que se encuentran en el return de get_arguments
options = get_aguments()

current_mac = get_current_mac(options.interface)
print("** MAC atual = " + str(current_mac) + " **")

#Aqui definimos la s variables que usaremos
change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] La MAC cambio a " + current_mac)
else:
    print("[-] La MAC no fuie cambiada")
