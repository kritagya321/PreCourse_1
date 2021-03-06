class myStack:
     def __init__(self):
          self.stack = []
         
     def isEmpty(self):
          if self.stack:
               return True
          return False
         
     def push(self, item):
           self.stack.append(item)
         
     def pop(self):
          return self.stack.pop()       
        
     def peek(self):
          if self.size ==0:
               return None
          return self.size[-1]
        
     def size(self):
          return len(self.stack)
         
     def show(self):
          return self.stack
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
