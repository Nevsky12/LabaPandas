import pandas as pd

Big_data, Umbrella_data = [], []
data = pd.read_csv("transactions.csv")
Re_data = data[data['STATUS'] == 'OK']
print("The three biggest sums: \n", Re_data.loc[Re_data['SUM'].nlargest(3).index])
print("Sum of Umbrella inc transactions: \n", Re_data.loc[Re_data['CONTRACTOR'] == 'Umbrella, Inc']['SUM'].sum())

