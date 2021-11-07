import pandas as pd
import matplotlib.pyplot as plt


data_flights = pd.read_csv("flights.csv")


flights = data_flights.CARGO.value_counts()
prices = data_flights.groupby("CARGO").PRICE.sum()
weights = data_flights.groupby("CARGO").WEIGHT.sum()


res_data = pd.DataFrame({'CARGO': flights, 'PRICE': prices, 'WEIGHT': weights}, index=data_flights.CARGO.unique())
print(res_data)

res_data.plot(kind="pie", subplots=True, figsize=(30,8))
plt.show()
