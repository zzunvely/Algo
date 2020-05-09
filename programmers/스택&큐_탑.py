#프로그래머스>코딩테스트 연습> 스택/큐>탑

def solution(heights):
    answer = [0] * len(heights)
    while len(heights)!=0 :
        element=heights.pop()
        for i in range(len(heights)-1, -1, -1) :
            if heights[i] > element :
                answer[len(heights)]=i+1
                break
    return answer
