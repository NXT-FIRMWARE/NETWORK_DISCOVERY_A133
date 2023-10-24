import socket
import sys
import struct
import netifaces
import json

class Client:
    def __init__(self,multicast_address,port,message):
        print("[i] init ...")
        data = {
           "hostname" : socket.gethostname(),
           "wifi_mac" : netifaces.ifaddresses('wlan0')[netifaces.AF_LINK][0]['addr'],
           "ethernet_mac" : netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr'],
            "wifi_ip" : (netifaces.ifaddresses('wlan0')[netifaces.AF_INET][0]['addr'],
        }
        self.message = json.dumps(data)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        mreq = struct.pack("4sl", socket.inet_aton(multicast_address), socket.INADDR_ANY)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
        #self.sock.bind((multicast_address, 5555))
        self.sock.bind(("", 5555))
        print("[i] start multicast lestening ...")
    def run(self):
        try:
            while 1:
                data, addr = self.sock.recvfrom(1024)
                print("[i] signal received from server")
                print("[i] send message to server")
                self.sock.sendto(bytes(self.message,"utf-8"),addr)
        except KeyboardInterrupt:
            print('[d] finish Executing ... ')
            sys.exit("[d] exit code")
