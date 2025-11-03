class Solution:
  def isWinner(self, player1, player2):
    length = len(player1)
    sum1 = sum2 = 0
    p1 = p2 = 0 # Bonus counter

    for i in range(length):
      # Player 1 sorting logic
      if p1 > 0:
        sum1 += player1[i] * 2
        p1 -= 1
      else:
        sum1 += player1[i]
      if player1[i] == 10:
        p1 = 2
      
      # Player 2 sorting logic
      if p2 > 0:
        sum2 += player2[i] * 2
        p2 -= 1
      else:
        sum2 += player2[i]
      if player2[i] == 10:
        p2 = 2

    # Compare final score
    if sum1 == sum2:
      return 0
    return 1 if sum1 > sum2 else 2