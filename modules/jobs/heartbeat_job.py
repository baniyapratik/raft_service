from queue import Queue
from threading import Thread
from raft_service.modules.cluster.client_heart_beat import send_heart_beat

# Global variable
queue = Queue()


# Helper Functions
def heartbeat_consumer():
    print("consumer waiting")
    cluster = queue.get()
    send_heart_beat(cluster)
    print("consumer out")


# Leader is suppose to send the heartbeat
def start_sending_hearbeat(cluster):
    print('Producer putting')
    thread = Thread(target=heartbeat_consumer)
    thread.start()
    print('Starting to send the heartbeat')
    queue.put(cluster)  # Runs before get() above
    thread.join()
    print('Stopped sendng heart beat')


