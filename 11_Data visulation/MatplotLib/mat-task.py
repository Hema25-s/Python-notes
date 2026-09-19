import pandas as pd

data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"],
    "Sales": [12000, 15000, 17000, 16000, 18000, 20000, 21000, 19000, 22000, 24000],
    "Profit": [2000, 3000, 3500, 3200, 4000, 4500, 4800, 4200, 5000, 5500],
    "Expenses": [10000, 12000, 13500, 12800, 14000, 15500, 16200, 14800, 17000, 18500],
    "Category": ["A","A","B","B","A","C","C","B","A","C"],
    "Region": ["South","North","East","West","South","East","West","North","South","East"],
    "Customers": [120, 150, 180, 160, 200, 220, 240, 210, 260, 300]
}

df = pd.DataFrame(data)
#line char task
import matplotlib.pyplot as plt
'''
x=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
y=[12000, 15000, 17000, 16000, 18000, 20000, 21000, 19000, 22000, 24000]
z=[2000, 3000, 3500, 3200, 4000, 4500, 4800, 4200, 5000, 5500]
a=[10000, 12000, 13500, 12800, 14000, 15500, 16200, 14800, 17000, 18500]
plt.plot(x,y, color='red', marker='*', mfc='black', ms=10 )
plt.plot(x,z , linestyle='--',linewidth=20)
plt.plot(x,a )
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
'''


x=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
y=[12000, 15000, 17000, 16000, 18000, 20000, 21000, 19000, 22000, 24000]
z=["A","A","B","B","A","C","C","B","A","C"]
a=[10000, 12000, 13500, 12800, 14000, 15500, 16200, 14800, 17000, 18500]
Region=["South","North","East","West","South","East","West","North","South","East"]
z=[2000, 3000, 3500, 3200, 4000, 4500, 4800, 4200, 5000, 5500]
Customers=[120, 150, 180, 160, 200, 220, 240, 210, 260, 300]
'''
plt.bar(z,Region)
for i in range(len(Region)):
    plt.text(z[i],Region[i],Region[i])
# plt.bar(x,y,linewidth=5,edgecolor='black')
# plt.bar(x,a )    
plt.show()
'''
# plt.hist(y,bins=2,color='red',edgecolor='yellow')
plt.show()
plt.scatter(y,z , color='black', s=Customers)
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 5. 

plt.plot(df["Month"], df["Sales"], color="red", alpha=0.5)
plt.grid()
plt.show()


# 8.

a = df.groupby("Category")["Sales"].mean()

plt.bar(a.index, a.values)
plt.show()


# 10. 

plt.bar(df["Month"], df["Sales"], label="Sales")
plt.bar(df["Month"], df["Expenses"],
        bottom=df["Sales"], label="Expenses")

plt.legend()
plt.show()


# 12. 

bars = plt.bar(df["Month"], df["Sales"])

for bar in bars:
    plt.text(bar.get_x(), bar.get_height(),
             str(bar.get_height()))

plt.show()




# 16.

cum = np.cumsum(df["Profit"])

plt.plot(df["Month"], cum)
plt.show()

