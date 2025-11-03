class Solution:
  def countPoints(self, rings: str) -> int:
    ring_map = {}
    for i in range(0, len(rings), 2):
      color = rings[i]
      rod = rings[i + 1]
      if rod not in ring_map:
        ring_map[rod] = set()
      ring_map[rod].add(color)

    count = sum(1 for colors in ring_map.values() if len(colors) == 3)
    return count