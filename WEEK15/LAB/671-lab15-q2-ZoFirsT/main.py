import pandas as pd

df = pd.read_csv('data.csv')

# ดึงข้อมูลประเภทของชั้นผู้โดยสาร (Pclass)
passenger_classes = df['Pclass'].unique()
print(passenger_classes)

# # Filter passengers over 40 years old
over_40 = df[df['Age'] > 40]
print(over_40)

class_male_counts = over_40[over_40['Sex'] == 'male']['Pclass'].value_counts().sort_index().to_dict()
print(class_male_counts)

class_female_counts = over_40[over_40['Sex'] == 'female']['Pclass'].value_counts().sort_index().to_dict()
print(class_female_counts)

print("male (age>40)")
for pclass, count in class_male_counts.items():
    print(f"Pclass {pclass}: {count}")

print("female (age>40)")
for pclass, count in class_female_counts.items():
    print(f"Pclass {pclass}: {count}")
