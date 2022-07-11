import socket

SRV_ADDR = input("escribe la direccion ip del servidor: ")
SRV_PORT = int(input("Escribe el puerto del servidor: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("servidor abierto, esperando conexiones...")
conn, addr = s.accept()
print("cliente conectado con la direccion: ", addr)
while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(b'-- Message Received --\n')
    print(data.decode('utf-8'))

s.close
