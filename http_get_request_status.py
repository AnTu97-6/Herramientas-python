import http.client

print("este programa devuelve una lista de metodos si las opciones estan habilitadas ** \n")

host = input("Introduce ip/host: ")
port = input("introduce el puerto(por defecto 80): ")

if (port == ""):
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('GET', '/')
    response = connection.getresponse()
    print("los metodos habilitados son: ", response.status)
    connection.close()
except ConnectionRefusedError:
    print("conexion fallida")
