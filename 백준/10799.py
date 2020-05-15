def solution(arrangement):
    answer = 0
    stack = []
    last = 0
    for i in arrangement:  #flag를 사용하거나, enumerate로 표시하기
        if i == '(':
            stack.append('(')
            last = 0
        else:
            if last == 0:
                stack.pop()
                answer += len(stack)

            else:
                stack.pop()
                answer += 1
            last = 1
    return answer

import sys
input = sys.stdin.readline
s = str(input().strip()) #입력으로 주어지는 문자열은 앞 뒤로 공백이 있다! => 공백처리!!!
print(solution(s))