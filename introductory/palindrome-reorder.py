import sys
from collections import Counter

def solve(s):
  counter = Counter(s)
  oddCount = 0
  oddItem = ''
  numOddItems = 0
  for item, count in counter.items():
    if count % 2 != 0:
      numOddItems += 1
      oddCount = count
      oddItem = item
    if numOddItems > 1:
      return "NO SOLUTION"

  leftString = ''
  for item, count in counter.items():
    if item != oddItem:
      leftString += item*(count//2)

  rightString = leftString[::-1]
  palindrome = leftString + oddItem*oddCount + rightString

  return palindrome

def main():
  s = input()
  print(solve(s))

if __name__ == "__main__":
	main()
