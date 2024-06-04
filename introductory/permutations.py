# TODO Recursion depth issue, create iterative solution
import sys

def main():
  n = int(input())
  result = []
  chosen = [False]*(n+1)
  isFound = False

  def generate(permutation):
    nonlocal isFound
    if isFound:
      return
    if len(permutation) > 1:
      if abs(permutation[-1] - permutation[-2]) == 1:
        return
    if len(permutation) == n:
      isFound = True
      for value in permutation:
        print(value, end=' ')
      return

    for i in range(1, n + 1):
      if chosen[i]: continue
      chosen[i] = True
      permutation.append(i)
      generate(permutation)
      chosen[i] = False
      permutation.pop()

  generate([])
  if not isFound:
    print("NO SOLUTION")

if __name__ == "__main__":
  main()
