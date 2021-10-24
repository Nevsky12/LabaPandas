import pandas as pd
import matplotlib.pyplot as plt

data_prices, data_weights, data_number, orgs = [], [], [], []
data = pd.read_csv("flights.csv")
names = dict(((i, [0, 0, 0]) for i in data["CARGO"].values))
for cell in data.to_numpy():
    names.update(
        {cell[1]: [names.get(cell[1])[0] + 1, cell[2] + names.get(cell[1])[1], cell[3] + names.get(cell[1])[2]]})
print(pd.DataFrame(names,index=["Number of flights", "Sum-price", "Sum-weight"]))

xs = range(len(names.keys()))
for a in names.keys():
    orgs.append(a)
data_Y = names.values()
for el in data_Y:
    data_prices.append(el[1])
    data_number.append(el[0])
    data_weights.append(el[2])

plt.title("Prices of all flights")
plt.bar(orgs, data_prices,
        width=0.2, color=['red','blue','green'], alpha=0.7,
        zorder=2)
plt.show()
plt.clf()
plt.title("Weights of all flights")
plt.bar(orgs, data_weights,
        width=0.2, color=['red','blue','green'], alpha=0.7, label=[orgs[0],orgs[1],orgs[2]],
        zorder=2)
plt.show()
plt.clf()
plt.title("Numbers of flights")
plt.bar(orgs, data_number,
        width=0.2, color=['red','blue','green'], alpha=0.7, label=[orgs[0],orgs[1],orgs[2]],
        zorder=2)
plt.show()
