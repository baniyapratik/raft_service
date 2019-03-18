from socket import socket, AF_INET, SOCK_DGRAM
from time import time, ctime, sleep


def send_heart_beat(cluster):
    port = 43278  # an arbitrary UDP port
    BEATWAIT = 10  # number of seconds between heartbeats
    neighbors = [neighbors for neighbors in cluster.get_neighbors() if neighbors.state != 'Leader']

    heartbeat_socket = socket(AF_INET, SOCK_DGRAM)

    for neighbor in range(len(neighbors)):
        print("Leader sending heartbeat to IP %s , port %d"%(neighbor.host, port))
    while 1:
        for neighbor in range(len(neighbors)):
            heartbeat_socket.sendto(str.encode('Thump!'), (neighbor.host, port))
        if __debug__:
            print(f"Time: {ctime(time())}")
        sleep(BEATWAIT)