#프로그래머스>코딩테스트 연습> 스택/큐>쇠막대기

def solution(arrangement):
    answer = 0
    last=0 #레이저와 막대 구분을 위한 bit 0='(', 1=')'
    s=Stack()
    for x in arrangement :
        if x=='(':
            s.push('(')
            last=0
        else:
            if last==0 :
                s.pop()
                answer+=s.size() #레이저
            else :
                s.pop()
                answer+=1
            last=1
    return answer

class Stack:
    def __init__(self):
            self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)