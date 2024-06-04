import sys

def solve():
  return

def main():
  # Taking input as string and splitting into list of integers
  # For example, if input is "1 2 3 4 5", it'll be split into [1, 2, 3, 4, 5]
  # For taking multiple integers as input, you can use map(int, input().split())
  nums = list(map(int, input().split()))

  # Taking single integer input
  n = int(input())

  # Taking input as list of strings
  strings = input().split()

  # Taking input as string
  s = input()

  # Taking input as a single string separated by a delimiter
  # For example, if input is "a,b,c,d,e", it'll be split into ['a', 'b', 'c', 'd', 'e']
  string_list = input().split(',')

  # Taking input with multiple lines
  n = int(input())
  for _ in range(n):
      s = input()

  # Taking input from standard input
  for line in sys.stdin:
      line = line.strip()
      # Process the line

  # Your logic here
  solve()

if __name__ == "__main__":
	main()
