def solution(board, moves):
    answer = 0
    pocket = []
    for move in moves:#크레인 픽업 한개씩 출력
      j = 0
      while j < len(board):
        if board[j][move-1] != 0:
          temp = board[j][move-1]
          board[j][move-1] = 0
          if len(pocket) >= 1 and temp == pocket[-1]:
            del pocket[-1]
            answer +=2
          else:
            pocket.append(temp)
          break
        j+=1

    return answer
          


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))

