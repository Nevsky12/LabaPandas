import pandas as pd
import matplotlib.pyplot as plt

ejudge = pd.read_html("results_ejudge.html")[0]
excel = pd.read_excel("students_info.xlsx")

data = pd.merge(excel, ejudge, how="left", right_on="User", left_on="login")
GF_ave = [data[data["group_faculty"] == i]['Solved'].mean() for i in data["group_faculty"].unique()]
GO_ave = [data[data["group_out"] == i]['Solved'].mean() for i in data["group_out"].unique()]

plt.title("Average number of solved tasks for faculty groups")
plt.bar([i for i in data["group_faculty"].unique()], GF_ave,
        width=0.2, color=['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'black'], alpha=0.7,
        zorder=2)
plt.show()
plt.clf()
plt.title("Average number of solved tasks for informatics groups")
plt.bar([i for i in data["group_out"].unique()], GO_ave,
        width=0.2, color=['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'black'], alpha=0.7,
        zorder=2)
plt.show()

for gr_faculty in data["group_faculty"][(data["G"] > 0) | (data['H'] > 0)]:
    print(gr_faculty, end="  ")
print(" ")
for i in range(len(data["group_faculty"][(data["G"] > 0) | (data['H'] > 0)])):
    print("|", end="  ")
print(" ")
for gr_info in data["group_out"][(data["G"] > 0) | (data['H'] > 0)]:
    print(gr_info, end=" ")

bool_checker = pd.notnull(data["login"])
data = data[bool_checker].fillna(0) # corrected data
print(data)