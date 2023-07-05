class Queue1:

# QUEUE FIFO 





    def __init__(self,qe):
        self.qe=qe


    def push(self,qe):
        queue.append(qe)
        print(queue)

    def pp(self,queue):
        queue.pop(0)
        print(queue)

    def top(self,queue):
        t=queue[0]
        print(t)

print("Let's implement Queue Here...!")
print("REMEMBER QUEUE --> FIFO ")
  

queue=[25,15]
print(queue)

v=Queue1(queue)
print("PUSH")
v.push(23)
print("POP")
v.pp(queue)
print("TOP")
v.top(queue)