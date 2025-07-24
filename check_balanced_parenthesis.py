def check_balanced_parenthesis(expr):
  matching={")":"(","}":"{","]":"["}
  stack=[]
  for char in expr:
    if char in '({[':
      stack.append(char)
    elif char in ')}]':
      if not stack or stack[-1]!=matching[char]:
        return False
      stack.pop()
  return len(stack)==0
expr="{[()()]}"
print(check_balanced_parenthesis(expr))
