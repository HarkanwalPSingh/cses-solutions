import sys

def main():
  # would be governed by factors of 2 & 5, since 5 occurs less than 2 so its upper bounded by 5
  # trailing_zeros = n/5 + n/(5^2) + n/(5^3) + ...
  n = int(input())
  powerOfFive = 5
  result = 0
  while n >= powerOfFive:
    result += n // powerOfFive
    powerOfFive *= 5

  print(result)

if __name__ == "__main__":
	main()
