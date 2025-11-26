import pandas as pd
import numpy as np

# Set random seed
np.random.seed(42)

# Define data parameters
n_employees = 100
departments = ['Finance', 'R&D', 'HR', 'Marketing', 'Sales', 'IT', 'Operations']
regions = ['Africa', 'Europe', 'North America', 'Latin America', 'Asia', 'Australia']

# Generate data
data = {
    'employee_id': [f'EMP{i:03d}' for i in range(1, n_employees + 1)],
    'department': np.random.choice(departments, n_employees),
    'region': np.random.choice(regions, n_employees),
    'performance_score': np.round(np.random.uniform(60, 100, n_employees), 2),
    'years_experience': np.random.randint(1, 25, n_employees),
    'satisfaction_rating': np.round(np.random.uniform(3.0, 5.0, n_employees), 1)
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data.csv', index=False)
print("data.csv generated successfully.")
