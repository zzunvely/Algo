#프로그래머스 > 스택&큐 > 프린터
def solution(priorities, location):
    answer = len(priorities)
    array = []
    for i in range(len(priorities)):
        array.append(i)

    while location in array:
        paper = priorities.pop(0)
        idx_paper = array.pop(0)
        isMax =  False
        for i in range(len(priorities)):
            if paper < priorities[i]:
                isMax = True
                break
        if isMax:
            priorities.append(paper)
            array.append(idx_paper)

    return answer - len(array)
