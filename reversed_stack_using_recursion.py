def insert_at_bottom(stack,item):
  if len(stack)==0:
    stack.append(item)
  else:
    top=stack.pop()
    insert_at_bottom(stack,item)
    stack.append(top)
def reversed_stack(stack):
  if len(stack)==0:
     return
  top=stack.pop()
  reversed_stack(stack)
  insert_at_bottom(stack,top)
stack=[10,20,30]
print(f"Original Stack: {stack}")
reversed_stack(stack)
print(f"Reversed Stack: {stack}")
