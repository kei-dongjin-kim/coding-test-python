class Solution:
  def checkString(self, s: str) -> bool:
    flag = False
    
    for c in s:
      if flag:
        if c == 'a':
          return False
      else:
        if c == 'b':
          flag = True
      
    return True
