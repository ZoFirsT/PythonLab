x = float(input())
y = float(input())

if x != 0 and y != 0:
    if x > 0 and y > 0:
        quadrant = "Q1"
    elif x < 0 and y > 0:
        quadrant = "Q2"
    elif x < 0 and y < 0:
        quadrant = "Q3"
    else:
        quadrant = "Q4"
    print(quadrant)
else:
    print("Undetermined quadrant")