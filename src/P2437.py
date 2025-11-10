class Solution:
  def countTime(self, time: str) -> int:
    res = 1

    # Hour first digit
    if time[0] == '?':
      if time[1] in ['0', '1', '2', '3']:
        res *= 3
      else:
        res *= 2
    
    # Hour second digit
    if time[1] == '?':
      if time[0] == '2':
        res *= 4
      elif time[0] == '?':
        res *= 12
      else:
        res *= 10
    
    # Minute first digit
    if time[3] == '?':
      res *= 6
    
    # Minute second digit
    if time[4] == '?':
      res *= 10
    
    return res