hours_worked = int(input())

if hours_worked <= 40:
    compensation = hours_worked * 50
else:
    extra_hours = hours_worked - 40
    compensation = (40 * 50) + (extra_hours * 75)

print(compensation)