from multiprocessing.managers import BaseManager
from time import sleep


class QueueManager(BaseManager):
    pass


sleep(1)
QueueManager.register('data_queue')
QueueManager.register('result_queue')
m = QueueManager(address=('queue', 12345), authkey='abracadabra'.encode("utf8"))
m.connect()
data_queue = m.data_queue()
result_queue = m.result_queue()

data_chunk = data_queue.get()
while data_chunk["row"] != -1:
    result = 0.0
    for i in range(len(data_chunk["data1"])):
        result += data_chunk["data1"][i] * data_chunk["data2"][i]

    result_chunk = {"row": data_chunk["row"], "column": data_chunk["column"], "result": result}
    result_queue.put(result_chunk)

    data_chunk = data_queue.get()
