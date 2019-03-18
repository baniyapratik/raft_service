from raft_service.modules.cluster.node import Node

class Cluster:
    neighbors = []

    def add_neighbor(self, host, port):
        node = Node(host, port)
        self.neighbors.append(node)

    def remove_neighbor(self, nodeId):
        for neighbor in self.neighbors:
            if neighbor.nodeId == nodeId:
                self.neighbors.remove(neighbor)
                break

    def get_neighbors(self):
        my_neighbors = [neighbor for neighbor in self.neighbors]
        return my_neighbors



