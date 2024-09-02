def factorial(x):
  if x == 0 or x == 1:
    return 1
  else:
    result = 1
    for i in range(2, x+1):
      result *= i
    return result

x = int(input())

result = factorial(x)
output_string = f"{x}"
for i in range(x-1, 0, -1):
    output_string += f"*{i}"
output_string += f"={result}"

print(output_string)