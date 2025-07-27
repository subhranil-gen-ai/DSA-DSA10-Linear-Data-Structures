def reverse_string_using_stack(s):
    stack = []

 
    for char in s:
        stack.append(char)

    reversed_str = ""

    
    while stack:
        reversed_str += stack.pop()

    return reversed_str


s = "hello"
print(reverse_string_using_stack(s))
