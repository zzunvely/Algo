#출력은 잘되는데, 시간오류
import sys
input = sys.stdin.readline()
a, b = map(int, input.split())
line = []
final = []
for i in range(a):
    line.append(int(i+1))
for _ in range(a):
    for i in range(b-1):
        tmp = line.pop(0)
        line.append(tmp)
    target = line.pop(0)
    final.append(target)

print("<", end="")
for i in range(len(final)-1):
    print(final[i], end=", ")
print(final[-1], end="")
print(">", end="")