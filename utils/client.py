
import socket
import sys
import struct

class Client:
    def __init__(self,multicast_address,port,message):
        print("[i] init ...")
        self.message = message
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #sock.bind((multicast_address, port))
        self.sock.bind(("", 5007))
        mreq = struct.pack("4sl", socket.inet_aton(multicast_address), socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        print("[i] start multicast lestening ...")
    def run(self):
        try:
            while 1:
                data, addr = self.sock.recvfrom(1024)
                print("[i] signal received from server")
                print("[i] send message to server")
                self.sock.sendto(bytes(self.message,'utf-8'),addr)
        except KeyboardInterrupt:
            print('[d] finish Executing ... ')
            sys.exit("[d] exit code")
