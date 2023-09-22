import subprocess

interface = "eth0"
grep = " | grep -oP '(?<=inet\s)\\d+(\\.\\d+){3}'"

# Concatenamos los comandos en una sola cadena
comando = f"ifconfig {interface}{grep}"

# Ejecutamos el comando y capturamos la salida
salida = subprocess.check_output(comando, shell=True)

# La salida será de tipo bytes, si deseas convertirla a una cadena de texto puedes hacer lo siguiente
salida = salida.decode('utf-8')

# Ahora la variable 'salida' contiene la información de la dirección IP
print("Tu direccion IP es " + salida)