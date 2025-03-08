import subprocess

def obtener_ip(interface="eth0"):
    try:
        # Ejecutamos el comando ifconfig y capturamos la salida
        salida = subprocess.check_output(["ifconfig", interface], text=True)
        
        # Buscamos la dirección IP en la salida
        for linea in salida.splitlines():
            if "inet " in linea:
                partes = linea.split()
                ip = partes[1]
                return ip
        
        # Si no se encuentra la IP, devolvemos un mensaje de error
        return "No se pudo encontrar la dirección IP en la interfaz especificada."
    
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar el comando: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"

# Especificamos la interfaz de red
interface = "eth0"

# Obtenemos la dirección IP
ip = obtener_ip(interface)

# Mostramos la dirección IP
print(f"Tu dirección IP en {interface} es: {ip}")
