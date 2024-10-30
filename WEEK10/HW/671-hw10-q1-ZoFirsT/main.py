n = int(input())
nums = [int(input()) for _ in range(n)]

# print(nums)

result = {}
# print(result)

for num in nums:
    result[num] = 'even' if num % 2 == 0 else 'odd'

print(result)