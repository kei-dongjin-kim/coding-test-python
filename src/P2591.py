class Solution:
  def distMoney(self, money: int, children: int) -> int:
    # Each child must receive at least 1 dollar
    money -= children

    # If there isn't enough money
    if money < 0:
      return -1
    
    count = 0

    # Distribute money so that as many children as possible get 8 dollar
    while money >= 7 and children > 0:
      money -= 7
      children -= 1
      count += 1

    # If there is leftover money but no children left, one 8 dollar child must give some back
    if children == 0 and money > 0:
      count -= 1
    
    # Special case: if one child left and exactly 3 dollar remaining -> violates condition
    if children == 1 and money == 3:
      count -= 1
    
    return count
  