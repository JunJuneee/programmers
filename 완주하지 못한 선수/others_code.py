import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

#colletion 모듈을 처음 봤다. 카운터를 쓰면 개수를 새 주고, 뺄수도 있으니 신기하다.