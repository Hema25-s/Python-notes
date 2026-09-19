#                            MATPLOTLIB
'''

It is a python module used to create and customize charts on python
It needs to be installed using following command
pip install matplotlib
'''

#               LINE CHART
'''
Used when we want analyze time related data, that changes over time


import matplotlib.pyplot as plt

x=['A','B','C','D','E']
y=[234234,3454,546456,5645,3455]

plt.figure(figsize=(7,7))
plt.title('Sample title')
plt.plot(x,y, color='red', marker='*', mfc='blue', ms=20)
plt.xlabel('Products')
plt.ylabel('Sales')
#plt.show()
plt.savefig('analysis.png')
print('Saved....')



EX2:

import matplotlib.pyplot as plt
import numpy as np

x=['A','B','C','D','E']
y=[234,34,54,564,345]
z= np.array(y)+100

plt.figure(figsize=(7,7))
plt.title('Sample title')
plt.plot(x,y, color='orange', marker='*', mfc='blue', ms=20)
plt.plot(x,z, color='blue', marker='*', mfc='yellow', ms=20)
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()


            LINE WTIH TEXT

import matplotlib.pyplot as plt
import numpy as np

x=['A','B','C','D','E']
y=[234,34,54,564,345]
z= np.array(y)+100

plt.figure(figsize=(7,7))
plt.title('Sample title')
plt.plot(x,y, color='orange', marker='*', mfc='blue', ms=20)

for i in range(len(y)):
    plt.text(x[i],y[i],y[i])
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()
'''

#                  BAR CHART
'''
Used to visual each categorie's frequency.


import matplotlib.pyplot as plt
import numpy as np

x=['A','B','C','D','E']
y=[234,34,54,564,345]
z= np.array(y)+100

plt.figure(figsize=(7,7))
plt.title('Sample title')
plt.bar(x,y, color='orange', edgecolor='black')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()


EX2:


import matplotlib.pyplot as plt
import numpy as np

x=['A','B','C','D','E']
y=[234,34,54,564,345]
z= np.array(y)+100

plt.figure(figsize=(7,7))
plt.title('Sample title')


plt.bar(x,y, color='orange', edgecolor='black')
for i in range(len(x)):
    plt.text(x[i],y[i],y[i])
plt.plot(x,z)
for i in range(len(x)):
    plt.text(x[i],z[i],z[i])


plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()
'''

#                   SCATTER
'''
Takes only two numerical value for x and y axis,
used to check the relationship between two numerical values


EX:

import matplotlib.pyplot as plt
import numpy as np

x=['A','B','C','D','E']
y=[234,34,54,564,345]
z= np.array(y)+100

plt.figure(figsize=(7,7))
plt.title('Sample title')


plt.scatter(y,z, c='blue')
plt.plot(y,z)

plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()

'''

#             HISTOGRAME
'''
Takes only one numerical value to see the distribution
of the each value.

EX:
height = [100,120,125,130,145,155]

100-130 -> 4
130-150 -> 3

In hist each bars are considers as bins, that can also be controled


EX:
import matplotlib.pyplot as plt
import numpy as np

height = [100,120,125,130,145,155]

plt.figure(figsize=(7,7))
plt.title('Sample title')


plt.hist(height, bins=2, color='pink', edgecolor='black')

plt.show()
'''

# plt.savefig('analysis.png')
# print('Saved....')


#         PIE AND DOUGHNUT
'''
import matplotlib.pyplot as plt
import numpy as np

height = [100,120,125,130,145,155]

plt.figure(figsize=(7,7))

x=['A','B','C','D','E']
y=[234,34,54,564,345]
plt.pie(x=y, labels=x, autopct='', 
        wedgeprops=dict(width=0.4))
plt.show()
'''

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('diabetes.csv')
condition = df['diabetes'] == 1

diabetes_patients = df[condition]

summary_data = diabetes_patients.groupby('smoking_history')['diabetes'].sum().sort_values(ascending=False)
print(summary_data)

x= summary_data.index.to_list()
y= summary_data.values.tolist()

plt.bar(x,y, color='pink')
plt.show()

