from flask import Blueprint, request
from .schemas import NeighborSchema
from raft_service.modules.cluster.cluster import Cluster
from raft_service.ext.api import APIResponse

mod = Blueprint('gateway', __name__, url_prefix='/api/raft')
# read from file
cluster = Cluster()


@mod.route('/test', methods=['GET'])
def test_api():
    return APIResponse()


@mod.route('/initiate', methods=['POST'])
def initiate():

    pass


@mod.route('/neighbor', methods=['POST'])
def add_neighbor():
    data = NeighborSchema(strict=True)
    data = data.load(request.get_json()).data
    host = data['host']
    port = data['port']

    pass


@mod.route('/neighbor', methods=['DELETE'])
def remove_neighbor():
    pass


@mod.route('/neighbor', methods=['GET'])
def get_neighbors():
    pass