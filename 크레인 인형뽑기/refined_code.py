def solution(board, moves):
  answer = 0
  pocket = [0] #0을 추가하면, 끝에 두개 확인할 때, 조건 추가 필요없음

  for move in moves:
    for i in range(len(board)):
      if board[i][move-1] != 0:
        pocket.append(board[i][move-1])
        board[i][move-1] = 0
      
        if pocket[-1] == pocket[-2]:
          pocket.pop(-1)
          pocket.pop(-1)
          answer += 2
        break

  return answer
  
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))