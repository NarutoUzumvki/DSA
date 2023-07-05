# class Demo1:

# # Stack LIFO
# # Queue FIFO

#     def __init__(self,se ):
#          self.se=se

  
         

    
        
#     def psh(self,se):
#         stack.append(se)
#         # print(l)


#     def pp(self,stack):
#         stack.pop()
#         print(stack)

   

#     def top(self,stack):
#         i=stack[-1]
#         print(i)


    




# print("Let's implement Stack here...!")    
# print(" REMEMBER STACK --> LIFO ")


# stack=[]



# y=Demo1(stack)
# y.psh(33)

# x=Demo1(stack)
# x.psh(51)
# x.psh(33)
# x.psh(91)
# x.psh(77)
# print(stack)

# print("POP")
# x.pp(stack)

 
 
# print("TOP")
# x.top(stack)


 



 
class Stack:

   
    def __init__(self,s):
        self.s = s

    def push_to_stack(self,val):
        f = self.s.append(val)
        print("Pushing an Element!" )
        print(val)
        return f
         

    def pop_from_stack(self):

        if len(self.s)>0:
            print("Poping an Element!")
            
            m = self.s.pop()
            
        else:
            print("Empty Stack..!")

        return m

    def top_of_Stack(self):

        print("Top Of The Stack..!")

        if len(self.s)>0:
            
            n = self.s[-1]
            return n
        else:
            print("Empty Stack..!")

        
print("Let's try to implement Stack Here...!")
print(" Note : Stack --> LIFO ")


stack_lst = [ 12,1]

print("Initial Stack elements..!")
print(stack_lst)

d = Stack(stack_lst)
d.push_to_stack(51)
print(stack_lst)
d.pop_from_stack()
print(stack_lst)
j=d.top_of_Stack()
print(j)
 

 



   