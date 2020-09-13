#drawing a bow tie

n = int(input('Enter a number to draw stars in bow tie '))

for i in range(n):
  string = '*' * (i + 1)
  string += ' ' * (2 * (n - i - 1))
  string += '*' * (i + 1)
  print(string)
for i in range(n-1):
  string = "*" * (n - i - 1)
  string += " " * (2 * (i + 1))
  string += "*" * (n - i - 1)
  print(string)