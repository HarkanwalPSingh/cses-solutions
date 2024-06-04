import sys

def solve(n):
  # gray_code = i ^ (i >> 1) => i XOR (i bitwise right shift)
  result = []
  for i in range(2**n):
    grayCode = i ^ (i >> 1)
    binaryRepr = format(grayCode, f'0{n}b')
    result.append(binaryRepr)

  return result

def main():
  n = int(input())

  for val in solve(n):
    print(val)


if __name__ == "__main__":
	main()
