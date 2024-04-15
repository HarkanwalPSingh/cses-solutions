import sys

def main():

  n = int(input())
  nums = list(map(int, input().split()))

  result = 0
  for i in range(1, n):
    if nums[i] < nums[i-1]:
      diff = nums[i-1] - nums[i]
      result += diff
      nums[i] += diff

  print(result)

if __name__ == "__main__":
  main()
