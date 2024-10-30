n = int(input())
directory = {}
directory['key_list'] = []
directory['value_list'] = []

for i in range(n):
    key = str(input())
    value = float(input())
    directory['key_list'].append(key)
    directory['value_list'].append(value)   

# print(directory)

# print(directory['key_list'][1])

result = {}

for i in range(len(directory['key_list'])):
    key = directory['key_list'][i]
    value = directory['value_list'][i]
    result[key] = value

# พิมพ์ผลลัพธ์
print(result)




# sum value all in directory
sum_value_list = sum(directory['value_list'])
print(f"{sum_value_list:.1f}")
