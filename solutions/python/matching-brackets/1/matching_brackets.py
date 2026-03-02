

left_tokens = ["[", "{", "("]
right_tokens = ["]", "}", ")"]

def is_paired(input_string):
    stack = []
    for ch in list(input_string):
       if ch in  left_tokens:
           stack.append(left_tokens.index(ch))
       if ch in right_tokens:
           if not stack:
               return False
           if stack.pop() != right_tokens.index(ch):
               return False
    return len(stack) == 0           
