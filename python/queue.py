class Queue:
    def __init__(self):
        self.items = []
        self.lis=[]
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def findmiddle(self):
        l=len(self.items)/2
        if l%2==0:
            l=l-1
        for i in range(0,l):
            a=self.items.pop()
            self.lis.append(a)
        return self.items[l]
        for i in self.lis:
            self.items.insert(0,i)





q = Queue()


q.enqueue(5)
q.enqueue(8)
q.enqueue(6)
q.enqueue(30)
q.enqueue(11)
q.enqueue(9)
q.dequeue()
q.enqueue(4)
q.enqueue(15)
print "items in Queue: ", q.items
print "middle element: ",q.findmiddle()
