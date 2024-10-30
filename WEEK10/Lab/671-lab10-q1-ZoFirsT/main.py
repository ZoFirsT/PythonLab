def Name_Grade(name, grade):
    student = {'name': name}
    if grade == 'a':
        student['GRADE'] = grade
    else:
        student['grade'] = grade
    return student


name = input()
grade = input().lower()

print(Name_Grade(name, grade))
