class Stack:
#
#  Stack ADT has three methods: is_empty, push and pop.
#
   def __init__(self):
      self.stack = []
      self.top = 0

   def is_empty(self):
      return self.top == 0

   def push(self, item):
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]

stack = Stack()
stack.push('a') # s = [a]
stack.push('e') # s = [e, a]
stack.push('i') # s = [i, e, a]
l = stack.pop() # s = [e, a], l = "i"
m = stack.pop() # s = [a], m = "e"
n = stack.pop() # s = [], n = "a"
stack.push(l) # s = [i]
stack.push(l) # s = [i, i]
stack.push(m) # s = [e, i, i]
m = stack.pop() # s = [i, i], m = "e"
while not stack.is_empty():
   print(stack.pop(), end='')