class Node:
    isAlive = True

    def __init__(self, host, port, nodeId):
        self.host = host
        self.port = port
        self.state = None
        self.nodeId = nodeId

    def getHost(self):
        return self.host

    def setHost(self, host):
        self.host = host

    def setState(self, state):
        self.state = state

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