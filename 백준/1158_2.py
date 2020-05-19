#런타임에러나는 이유 못찾음
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
line = [i for i in range(1, a+1)]
final = []
num = 0
for _ in range(a):
    num += (b-1)
    if num > len(line):
        num = num % len(line)
    target = line.pop(num)
    final.append(target)
print("<"+", ".join(map(str, final))+">")