# TODO completely wrong answer
import sys

def solve(n):
  result = []
  if n == 1:
    result.append((1,3))
  elif n == 2:
    result.append((1,2))
    result.append((1,3))
    result.append((2,3))
  elif n > 2:
    result.append((1,2))
    result.append((1,3))
    result.append((2,3))
    for i in range(n-2):
      result.append((1,2))
      result.append((3,2))
      result.append((2,3))

  return result

def main():
  n = int(input())
  result = solve(n)

  print(len(result))
  for stackA, stackB in result:
    print(stackA, stackB)

if __name__ == "__main__":
	main()
