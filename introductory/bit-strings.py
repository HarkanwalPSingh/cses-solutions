import sys

def main():
  n = int(input())

  MODULO = 1_000_000_007
  base = 2

  # Impractical
  # result = 2**n % MODULO

  result = 1
  while n > 0:
    if (n % 2) == 1:
      result = (result * base) % MODULO
    n = n >> 1 # same as n // 2 but faster
    base = (base * base) % MODULO

  print(result)

if __name__ == "__main__":
	main()
