from raft_service.modules.cluster.client_heart_beat import send_heart_beat


class Leader:

    @staticmethod
    def send_heart_beat(self):
        send_heart_beat()