class Demo1:

# Stack LIFO
# Queue FIFO

    def __init__(self,se ):
         self.se=se

  
         

    
        
    def psh(self,se):
        stack.append(se)
        # print(l)


    def pp(self,stack):
        stack.pop()
        print(stack)

   

    def top(self,stack):
        i=stack[-1]
        print(i)


    




print("Let's implement Stack here...!")    
print(" REMEMBER STACK --> LIFO ")


stack=[]



y=Demo1(stack)
y.psh(33)

x=Demo1(stack)
x.psh(51)
x.psh(33)
x.psh(91)
x.psh(77)
print(stack)

print("POP")
x.pp(stack)

 
 
print("TOP")
x.top(stack)


 



 


   