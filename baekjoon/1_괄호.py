## 풀이 1
count = int(input())
for _ in range(count):
    stack, input_string = [], input()

    for i in input_string:
        if i == '(':
            stack.append(i)
        elif (len(stack) != 0) and i == ')':
            stack.pop()
        else:
            stack.append(i)
            break
    
    print('YES' if len(stack) == 0 else 'NO')
    
## 풀이 2
# count = int(input())
# for _ in range(count):
#     stack, input_string = [], input()

#     for i in input_string:
#         if i == '(':
#             stack.append(i)
#         elif i == ')':
#             if len(stack) == 0:
#                 stack.append(i)
#                 break
#             else:
#                 stack.pop()
        
#     if len(stack) == 0:
#         print("YES")
#     else:
#         print("NO")