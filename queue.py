class Queue:
    def __init__(self, capacity = 10):
        self.data = [0] * capacity
        self.front = 0
        self.back = 0

    def count(self):
        if self.back >= self.front:
            return self.back - self.front
        else:
            return self.back - self.front + len(self.data)

    def isempty(self):
        return self.front == self.back

    def enqueue(self, item):
        if self.count() < len(self.data) - 1:
            self.data[self.back] = item
            self.back = (self.back + 1) % len(self.data)
        else:
            print("Queue Full")

    def dequeue(self):
        if self.count() > 0:
           item = self.data[self.front]
           self.front = (self.front + 1) % len(self.data)
           return item
        else:
            return None

queue = Queue()
queue.enqueue('a') # q = [a]
queue.enqueue('e') # q = [a, e]
queue.enqueue('i') # q = [a, e, i]
l = queue.dequeue() # q = [e, i] l = "a"
m = queue.dequeue() # q = [i] m = "e"
n = queue.dequeue() # q = [] n = "i"
queue.enqueue(l) # q = [a]
queue.enqueue(l) # q = [a, a]
queue.enqueue(m) # q = [a, a, e]
m = queue.dequeue() # q = [a, e]
while not queue.isempty():
   print(queue.dequeue(), end='')