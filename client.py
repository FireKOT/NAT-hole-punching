import argparse
import socket
import threading


def receiveMessages (sock):

    while True:

        try:

            message, addr = sock.recvfrom(1024)

            if message:

                print(f"{addr}: {message.decode()}")

        except KeyboardInterrupt:

            break
        


def sendMessages (sock, peerAddr):

    while True:

        message = input()
        sock.sendto(message.encode(), peerAddr)


def getPeerAddr (sock, rendezvousAddr):

    sock.sendto("".encode(), rendezvousAddr)

    data, _ = sock.recvfrom(1024)
    ip, port = data.split()

    print("Connection established")

    return (ip, int(port))


parser = argparse.ArgumentParser()
parser.add_argument("rendezvous", type = str)
parser.add_argument("-port", type = int, default = 1313)

args = parser.parse_args()


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", args.port))


peerAddr = getPeerAddr(sock, (args.rendezvous, 1313))


receiveThread = threading.Thread(target = receiveMessages, args = (sock,))
sendThread = threading.Thread(target = sendMessages, args = (sock, peerAddr))

receiveThread.start()
sendThread.start()

receiveThread.join()
sendThread.join()

sock.close()
