class Node:
    isAlive = True
    nodeId = 0

    def __init__(self, host, port):
        global nodeId
        self.host = host
        self.port = port
        self.nodeId = ++nodeId

    def getHost(self):
        return self.host

    def setHost(self, host):
        self.host = host

    def getPort(self):
        return self.port

    def setPort(self, port):
        self.port = port

    def getNodeId(self):
        return self.nodeId

    def setNodeId(self, nodeId):
        self.nodeId = nodeId

    def getHostAndPort(self):
        return {"host": self.host, "port": self.port}