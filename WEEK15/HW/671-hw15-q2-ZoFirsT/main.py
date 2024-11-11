# YOUR CODE HERE
import pandas as pd

df = pd.read_csv('data.csv')
# print(df)

for port in df['Embarked'].unique():
    port_df = df[df['Embarked'] == port]
    
    sorted_df = port_df.sort_values(by=['Pclass', 'Fare'], ascending=[True, False])
    
    display_df = sorted_df[['Pclass', 'Fare', 'Embarked']]
    
    print(f"Embarked: {port}")
    
    print(display_df.head())
    
    print(display_df.tail())
