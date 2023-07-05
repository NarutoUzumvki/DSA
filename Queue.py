# class Queue:

# # QUEUE FIFO 
# # PEP --> Python Enhancement Protocol





#     def __init__(self,q):
#         self.q=q

#     def push(self,val):
#         self.q.append(val)
#         print(queue)

#     def pop_(self):
#         if len(self.q)>0:
#             r=queue.pop(0)
#             print(queue)
            
#         else:
#             ("Empty Queue..!")
   

        

#     def top(self):
#         t=queue[0]
#         print(t)

# print("Let's implement Queue Here...!")
# print("REMEMBER QUEUE --> FIFO ")
  

# queue=[25,15]
# print(queue)

# v=Queue(queue)
# print("PUSH")
# v.push(23)

# print("POP")
# v.pop_() 

# print("TOP")
# v.top()


# v2=Queue(queue)
# print("v2")
# print(queue)

# v2.push(7)
# v2.pop_()
# v2.top()



class Queue:

    def __init__(self,q):
        self.q = q
    
    def push_to_queue(self,val):
        print("Pushing an element to Queue!")
        print(val)
        b = self.q.append(val)
        return b

    def pop_from_queue(self):
        print("Popping an Element..!")
        v = self.q.pop(0)
        return v

    def top_of_queue(self):
        print("TOP of the Queue..!")

        i=self.q[0]
        return i



print("Let's try to implement Queue Here...!")
print(" Note : Queue --> FIFO ")



queue_lst=[2,58,45]

print("Initial Queue elements..!")
print(queue_lst)
    
a=Queue(queue_lst)

a.push_to_queue(11)
print (queue_lst)

a.pop_from_queue()
print(queue_lst)

i=a.top_of_queue()
print(i)






 





