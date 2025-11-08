class Solution:
  def canMakeSquare(self, grid):
    # check all 2x2 sub-squares in the 3x3 grid
    for i in range(2):
      for j in range(2):
        # count how many 'B' cells appear in this 2x2 block
        b = 0

        # iterate through the 2x2 block
        for r in range(i, i + 2):
          for c in range(j, j + 2):
            if grid[r][c] == 'B':
              b += 1

        # if number of 'B' in the block is 0, 1, 3 or 4 => possible
        if b in (0, 1, 3, 4):
          return True
    
    return False