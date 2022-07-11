import socket

target = input("introduce ip objetivo: ")
portRange = input("Introduce el rango de puertos(0-65535): ")

lowport = int(portRange.split('-')[0])
highport = int(portRange.split('-')[1])

print("scanning host ", target, "from port ", lowport, "to port ", highport)

for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print("*** port ", port, "- OPEN ***")
    s.close
