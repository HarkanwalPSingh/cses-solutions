import sys

def printResult(set):
  print(len(set))
  for value in set:
    print(value, end=' ')
  print()

def main():
  n = int(input())

  sum = (n*(n+1))//2

  if not sum % 2 == 0:
    print('NO')
    return

  targetSum = sum // 2
  set1 = []
  set2 = []
  currentSum = 0
  for i in range(n, 0, -1):
    if currentSum + i <= targetSum:
      set1.append(i)
      currentSum += i
    else:
      set2.append(i)

  print('YES')
  printResult(set1)
  printResult(set2)

if __name__ == "__main__":
	main()
