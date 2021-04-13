from datetime import datetime
from multiprocessing.managers import BaseManager
from time import sleep

SLAVE_NODES_NUMBER = 7
OUTPUT_FILENAME = "../Data/out.txt"


def read(filename):
    f = open(filename, "r")
    nr = int(f.readline())
    nc = int(f.readline())

    A = [[0] * nc for x in range(nr)]
    r = 0
    c = 0
    for i in range(0, nr * nc):
        A[r][c] = float(f.readline())
        c += 1
        if c == nc:
            c = 0
            r += 1

    return A


def write_result(r, filename):
    file = open(filename, "w")

    for i in range(len(r)):
        for j in range(len(r[0])):
            file.write(f'{r[i][j]}, ')
        file.write(f'\n')
    pass


class QueueManager(BaseManager):
    pass


sleep(1)
start = datetime.now()

QueueManager.register('data_queue')
QueueManager.register('result_queue')
m = QueueManager(address=('queue', 12345), authkey='abracadabra'.encode("utf8"))
m.connect()
data_queue = m.data_queue()
result_queue = m.result_queue()

print("Reading bigA.dat")
big_a = read("../Data/bigA.dat")
print("Reading bigX.dat")
big_x = read("../Data/bigX.dat")

print("Pushing data_chunks into queue.")
for i in range(len(big_a)):
    for j in range(len(big_x[0])):
        data2 = []
        for k in range(len(big_x)):
            data2.append(big_x[k][j])

        data_chunk = {"row": i, "column": j, "data1": big_a[i], "data2": data2}
        data_queue.put(data_chunk)

results_num = 0
result = [[0.0] * len(big_x[0]) for i in range(len(big_a))]

print("Collecting result data from queue.")
while results_num != len(big_a) * len(big_x[0]):
    result_chunk = result_queue.get()

    result[result_chunk["row"]][result_chunk["column"]] = result_chunk["result"]
    results_num += 1

for i in range(SLAVE_NODES_NUMBER * 2):
    terminate_chunk = {"row": -1, "column": -1, "data1": None, "data2": None}
    data_queue.put(terminate_chunk)

print("Writing result into output file.")
write_result(result, OUTPUT_FILENAME)

end = datetime.now()
delta = end - start
print(f"Execution time in seconds: {delta.total_seconds()}")
