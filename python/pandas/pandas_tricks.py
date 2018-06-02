import pandas as pd

# Create Panda Dataframe from a list of tuples
contacts = [('Satyabrat', 'Kumar', 34, 'satyabratsingh@gmail.com'),
            ('Ravi', 'Singh', 30, 'ravisingh@gmail.com'),
            ('Sudhansu', 'Singh', 28, 'satyabratsingh@ssudhansu.com')]
labels = ['first_name', 'last_name', 'age', 'email']
df = pd.DataFrame.from_records(contacts, columns=labels)
print df

# Create a Panda data frame from a list of dictionaries
families = [{'first_name': 'Satyabrat', 'last_name': 'Kumar', 'Age': 34, 'email': 'satyabratsingh@gmail.com'},
         {'first_name': 'Ravi', 'last_name': 'Singh', 'Age': 30, 'email': 'ravisingh@gmail.com'},
         {'first_name': 'Sudhansu', 'last_name': 'Shekhar Singh', 'Age': 28, 'email': 'ssudhansu@gmail.com' }]

df = pd.DataFrame(families)
print df

anotherDf = pd.DataFrame.from_dict(families)
print anotherDf
