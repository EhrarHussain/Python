import queue
import threading


class Thread(threading.Thread):

    def __init__(self, num, queue):
        threading.Thread.__init__(self)
        self.num = num
        self.queue = queue

    def run(self):
        return_value = "value: " + str(self.num)
        self.queue.put(return_value)
        self.queue.task_done()


def q():
    myqueue = queue.Queue()

    # start threads
    for i in range(5):
        t1 = Thread(i, myqueue)
        t1.daemon = True
        t1.start()

    # wait for threads to finish
    myqueue.join()

    # get values from threads
    while not myqueue.empty():
        print(myqueue.get())


q()
