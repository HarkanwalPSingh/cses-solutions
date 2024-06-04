import sys
"""
1's boundary -> 1 to 1 order: 1 -> 1
2's boundary -> 2 to 4 order: 4 -> 2
3's boundary -> 5 to 9 order: 5 -> 9
4's boundary -> 10 to 16 order: 16 -> 10
5's boundary -> 17 to 25

Even the order is reverse
Boundary varies from max(x, y) - 1 square to max(x, y) square

2,3 => 5 to 9, if x < y calculate from RIGHT
3,2 => 5 to 9, if x > y calculate from LEFT
"""

def main():
  n = int(input())

  def solve(x, y):
    big = y
    if x > y:
      big = x

    LEFT_BOUNDARY = (big-1)**2 + 1
    RIGHT_BOUNDARY = (big)**2

    modBig = big % 2 == 0

    # print(f"Boundaries: {LEFT_BOUNDARY} {RIGHT_BOUNDARY}")
    if x < y:
      print(LEFT_BOUNDARY + x - 1) if modBig else print(RIGHT_BOUNDARY - x + 1)
    else:
      print(RIGHT_BOUNDARY - y + 1) if modBig else print(LEFT_BOUNDARY + y - 1)

  inputs = []
  for _ in range(n):
    x, y = map(int, input().split())
    inputs.append((x, y))

  for value in inputs:
    solve(value[0], value[1])

if __name__ == "__main__":
  main()
