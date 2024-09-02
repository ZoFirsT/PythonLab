scores = []
while True:
    score = input()
    if score == 'q':
        break
    score = int(score)
    if score < 0 or score > 100:
        continue
    scores.append(score)

if len(scores) == 0:
    print("No scores entered.")
else:
    average = sum(scores) / len(scores)
    average = round(average, 2)

    if average >= 50:
        print(f"{average} Satisfactory")
    else:
        print(f"{average} Unsatisfactory")