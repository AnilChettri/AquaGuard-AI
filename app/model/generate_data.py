# app/model/generate_data.py
import random
import pandas as pd

def generate_data(samples=1000):
    data = []
    for _ in range(samples):
        pH = round(random.uniform(5, 9), 2)
        temp = round(random.uniform(10, 35), 2)
        turbidity = round(random.uniform(0, 50), 2)
        label = 'Clean' if 6.5 <= pH <= 8.5 and turbidity < 5 else 'Contaminated'
        data.append([pH, temp, turbidity, label])
    
    df = pd.DataFrame(data, columns=['pH', 'Temperature', 'Turbidity', 'Label'])
    return df

if __name__ == "__main__":
    df = generate_data()
    df.to_csv('water_quality_data.csv', index=False)
    print("Data generated and saved as water_quality_data.csv")
