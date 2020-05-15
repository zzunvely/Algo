import sys
input = sys.stdin.readline
stack1 = str(input().strip())
stack1 = list(stack1)
stack2 = []
n = int(input().strip())
for i in range(n):
    tmp = list(map(str, input().strip().split()))
    if tmp[0] == 'L':
        if len(stack1) !=0 :
            t = stack1.pop()
            stack2.append(t)
    elif tmp[0] == 'D':
        if len(stack2) !=0:
            t = stack2.pop()
            stack1.append(t)
    elif tmp[0] == 'B':
        if len(stack1) !=0:
            stack1.pop()
    elif tmp[0] == 'P':
        stack1.append(tmp[1])
final = "".join(stack1)
stack2.reverse()
final += "".join(stack2)
print(final)