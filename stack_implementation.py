stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(f"Stack after push: {stack}")
stack.pop()
print(f"Stack after pop: {stack}")
print(f"Top of Stack: {stack[-1]}")
if len(stack)==0:
  print("Stack is empty")
else:
  print("Stack is not empty")
