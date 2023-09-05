
#Author: FARHAT OUSSAMA
#Date  : 09/05/2023

from dotenv import load_dotenv
from utils.client import Client
import os

load_dotenv() 

MCAST_GRP = os.getenv('MULTICAST_ADDRESS')
MCAST_PORT = os.getenv('PORT')
MESSAGE = os.getenv('PROJECT')


if __name__ == '__main__':
    print("[d] start network discovery client ...")
    discoveryClient = Client(MCAST_GRP,MCAST_PORT,MESSAGE)
    discoveryClient.run()
    