from socket import socket, AF_INET, SOCK_DGRAM
from time import time, ctime, sleep


# For leader
def send_heart_beat(cluster):
    port = 43278  # an arbitrary UDP port
    BEATWAIT = 10  # number of seconds between heartbeats
    heartbeat_socket = socket(AF_INET, SOCK_DGRAM)

    while 1:
        neighbors = [neighbors for neighbors in cluster.get_neighbors() if neighbors.get('state') != 'Leader']
        for neighbor in range(len(neighbors)):
            heartbeat_socket.sendto(str.encode(str(cluster.get_neighbors())), (neighbor.get('host'), port))
        if __debug__:
            print(f"Time: {ctime(time())}")
        sleep(BEATWAIT)