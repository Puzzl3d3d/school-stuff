import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(hostname, ip)

