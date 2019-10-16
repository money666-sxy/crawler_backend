from queue import Queue


class DBQueue(object):
    def __init__(self, maxsize):
        self.cq = Queue(maxsize=maxsize)

    def __contains__(self, item):
        pass

    def isEmpty(self):
        return self.cq.empty()

    def isFull(self):
        return self.cq.full()

    def put(self, article_item):
        self.cq.put(article_item)

    def get(self):
        return self.cq.get()
