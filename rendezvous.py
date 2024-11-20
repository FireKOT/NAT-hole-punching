import socket


port = 1313

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("0.0.0.0", port))

addr1 = None
addr2 = None

while True:
    
    _, addr = serverSocket.recvfrom(port)

    if (addr1 == None):

        print("1 resv")

        addr1 = addr

    else:

        print("2 resv")

        addr2 = addr

        ip1, p1 = addr1
        ip2, p2 = addr2

        serverSocket.sendto(f"{ip2} {p2}".encode(), addr1)
        serverSocket.sendto(f"{ip1} {p1}".encode(), addr2)

        break