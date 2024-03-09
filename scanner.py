import sys
import socket
from datetime import datetime

#Define target
if len(sys.argv) == 4:
	target = socket.gethostbyname(sys.argv[1]) # translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip> <port range>")
	print("example: python3 scanner.py 192.168.1.1 21 80")

#Banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(int(sys.argv[2]), int(sys.argv[3])):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is  open!".format(port))
        s.close

except KeyboardInterrupt:
	print("\n Exiting...")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolve")

except socket.error:
	print("Could not connect to server.")
	sys.exit()