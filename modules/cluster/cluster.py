from raft_service.modules.cluster.node import Node

class Cluster:
    neighbors = []

    def add_node(self, node):
        self.neighbors.append(node)
        return self.node_json(node)

    def add_neighbor(self, host, port):
        node = Node(host, port)
        self.neighbors.append(node)

    def remove_neighbor(self, nodeId):
        for neighbor in self.neighbors:
            if neighbor.nodeId == nodeId:
                self.neighbors.remove(neighbor)
                break
        return self.neighbors

    def get_neighbors(self):
        my_neighbors = [self.node_json(neighbor) for neighbor in self.neighbors]
        return my_neighbors

    def node_json(self, node):
        return {
            "node_id": node.nodeId,
            "host": node.host,
            "port": node.port,
            "state": node.state
        }


