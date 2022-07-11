import socket

SER_ADDR = input("introduce direccion servidor: ")
SER_PORT = int(input("introduce puerto server: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SER_ADDR, SER_PORT))
print("conexion establecida!")

message = input("Mensaje a enviar: ")
s.sendall(message.encode())
s.close()
