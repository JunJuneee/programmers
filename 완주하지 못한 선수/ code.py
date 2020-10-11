def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    
    for par in participant:
        dic[hash(par)] = par
        temp += int(hash(par))
    for com in completion:
        temp -= int(hash(com))
    return dic[temp]