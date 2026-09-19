#                     SEABORN
''''
Advance visual module that can be worked with matplotlib,
Extend version of matplotlib
Charts can be visuled without summarize the data
xlables, ylables will be set automatically.

Needs to be installed using following command

pip install seaborn


EX:
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='smoking_history', y='heart_disease')
plt.show()

'''
'''
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

#sns.barplot(data=data, x='heart_disease', y='smoking_history',  hue='smoking_history', legend=True, gap=0.50, orient='h')

#sns.lineplot(data=data, x='smoking_history', y='heart_disease',size='heart_disease')
#sns.scatterplot(data=data, x='blood_glucose_level', y='HbA1c_level', hue='smoking_history')



bmi, hbA1c, blood_gluc  -> heart_disease -> highset, low, total category

plt.show()
'''

#                       HEATMAP
'''

Used to visual the correlations matrix values with colors of box

WHAT IS CORRELATION:

Process of seeing the relationship between all numerical columns, that relationship
are called correlation relationship.

Types of correaltion:

1. Positive correlation -  When two numerical values are increased in same manner that are considered as positive correltion.
                           EX:  sales ^   profit ^                          

2. Negative correlation - When x is increase and y is decrease.
                          EX: sales ^  profit >


For both analysis gives positive and negative values, pandas as built in function to find
relationship between all numerical values. it retursn correlation matrix that with positive
and negative value.


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('employee.csv')

numerical_columns=data.select_dtypes(include='int64')

correlation_matrix = numerical_columns.corr()

# annot=True shows the numerical values inside the box
# 
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linecolor='black', linewidths=0.50)
plt.show()

'''


#                 PAIRPLOT
'''
It is combination scatter chart that takes all numerical data
on the dataset and creates scatter chart for all the
numerical columns.


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('employee.csv')

sns.pairplot(data=data, hue='Performance')
plt.show()


EX2:

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('employee.csv')

sns.pairplot(data=data, hue='Performance', x_vars='Salary',y_vars='Age')
plt.show()



'''

#              BOXPLOT
'''
Used to see the numerical value distribution of each numerical column on the dataset

It has following report

min, 25%, 50%(mean), 75%, max

This chart contains line for each values

This chart are used to find the outlier data,

             WHAT IS OUTLIER

A value which is not in a specific range

EX: Salary = [100,200,300,3453456456,250,300]
    3453456456  - outlier point


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('employee.csv')

sns.boxplot(data=data, x='Performance', y='Salary', hue='Performance', legend=True)
plt.grid()
plt.show()
'''


#   correlation values for all numerical data 
# blood_glucose_level distribution amoung dia yes no
# HbA1c_level for age category with boxplot