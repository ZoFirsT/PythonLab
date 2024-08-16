minutes = int(input())

hours = minutes // 60
minutes = minutes % 60

print(f"{hours:01d}:{minutes:01d}")