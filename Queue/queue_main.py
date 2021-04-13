import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


data_queue = queue.Queue()
result_queue = queue.Queue()
QueueManager.register('data_queue', callable=lambda: data_queue)
QueueManager.register('result_queue', callable=lambda: result_queue)
m = QueueManager(address=('', 12345), authkey='abracadabra'.encode("utf8"))
s = m.get_server()
s.serve_forever()


