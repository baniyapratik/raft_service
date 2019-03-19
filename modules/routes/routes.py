import requests
from flask import Blueprint, request
from .schemas import NeighborSchema
from raft_service.modules.cluster.cluster import Cluster
from raft_service.modules.jobs import heartbeat_job
from raft_service.modules.cluster.node import Node
from raft_service.ext.api import APIResponse

mod = Blueprint('gateway', __name__, url_prefix='/api/raft')
# TODO read from file
cluster = Cluster()


@mod.route('/test', methods=['GET'], strict_slashes=False)
def test_api():
    return APIResponse()


@mod.route('/initiate', methods=['POST'], strict_slashes=False)
def initiate():
    data = NeighborSchema(strict=True)
    data = data.load(request.get_json()).data
    host = data['host']
    port = data['port']
    index = cluster.neighbors.__len__() +1
    node = Node(host, port, index)
    node.setState('Leader')
    cluster.add_node(node)
    # Initiate the leader heartbeat
    heartbeat_job.send_heart_beat(cluster)
    return APIResponse(data={"Leader Initiated"}, status=200)


@mod.route('/neighbor', methods=['POST'], strict_slashes=False)
def add_neighbor():
    data = NeighborSchema(strict=True)
    data = data.load(request.get_json()).data
    host = data['host']
    port = data['port']
    # add node
    index = cluster.neighbors.__len__() + 1
    node = Node(host, port, index)
    node.setState('Follower')
    cluster.add_node(node)
    url = "http://"+host+":"+port+"/api/raft/update_neighbor"
    neighbors = cluster.get_neighbors()
    r = requests.post(url, data={neighbors})
    return APIResponse(data={"nodes": neighbors}, status=200)


@mod.route('/neighbor', methods=['DELETE'], strict_slashes=False)
def remove_neighbor():
    pass


@mod.route('/neighbor', methods=['GET'], strict_slashes=False)
def get_neighbors():
    neighbors = cluster.get_neighbors()
    return APIResponse(data=neighbors, status=200)


@mod.route('/update_neighbor', methods=['POST'], strict_slashes=False)
def update_upon_add():
    pass