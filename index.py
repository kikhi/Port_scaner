import socket

ip = input("Insert ip direction: ")

for puerto in range(1, 65535):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout()

    result = sock.connect_ex(ip, puerto)

    if result == 0:
        print("Puerto Abierto: " + str(puerto))
        sock.close()
    else:
        print("Puerto Cerrado: " + str(puerto))