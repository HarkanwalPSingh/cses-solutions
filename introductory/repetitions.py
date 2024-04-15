import sys

def main():

  s = input()
  l, r = 0, 0
  window = 1
  while r < len(s):
    if s[r] != s[l]:
      window = max(window, r - l)
      l = r
    r += 1

  window = max(window, r - l)
  print(window)

if __name__ == "__main__":
  main()
