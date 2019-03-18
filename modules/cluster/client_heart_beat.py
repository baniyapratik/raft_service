from socket import socket, AF_INET, SOCK_DGRAM
from time import time, ctime, sleep
from raft_service.modules.cluster.cluster import Cluster


def send_heart_beat():
    port = 43278  # an arbitrary UDP port
    BEATWAIT = 10  # number of seconds between heartbeats
    cluster = Cluster()
    neighbors = cluster.get_neighbors()

    for node in neighbors:
        if node.state == 'Leader':
            leader = node
    heartbeat_socket = socket(AF_INET, SOCK_DGRAM)
    if leader:
        print(f"leader node is {leader}")
        serverIP = '127.0.0.1'
    else:
        serverIP = leader.host
    print("PyHeartBeat client sending to IP %s , port %d"%(serverIP, port))
    while 1:
        heartbeat_socket.sendto(str.encode('Thump!'), (serverIP, port))
        if __debug__:
            print(f"Time: {ctime(time())}")
        sleep(BEATWAIT)