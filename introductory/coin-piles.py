import sys

def solve(nums):
  a, b = nums[0], nums[1]

  if (a + b) % 3 != 0 or (a > 2*b or b > 2*a):
    print('NO')
  else:
    print('YES')

def main():
  n = int(input())
  for _ in range(n):
      nums = list(map(int, input().split()))
      solve(nums)

if __name__ == "__main__":
	main()
