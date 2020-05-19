import sys
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, num):
        self.queue.append(num)

    def pop(self):
        return self.queue.pop(0) if len(self.queue) != 0 else -1

    def size(self):
        return len(self.queue)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def front(self):
        return self.queue[0] if self.size() != 0 else -1

    def back(self):
        return self.queue[-1] if self.size() != 0 else -1

num = int(input())
queue = Queue()
for _ in range(num):
    tokens = input().split()
    if tokens[0] == "push":
        queue.push(tokens[1])
    elif tokens[0] == "pop":
        print(queue.pop())
    elif tokens[0] == "size":
        print(queue.size())
    elif tokens[0] == "empty":
        print(queue.empty())
    elif tokens[0] == "front":
        print(queue.front())
    elif tokens[0] == "back":
        print(queue.back())
    else:
        print("it's not acceptable operator")