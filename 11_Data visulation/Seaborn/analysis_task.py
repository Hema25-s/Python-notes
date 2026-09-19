# 1

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='gender', y='BMI')

plt.show()


# 2

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='gender', y='blood_glucose_level')

plt.show()


# 3

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='gender', y='HbA1c_level')

plt.show()


# 4

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='gender', y='diabetes',hue='diabetes', legend=True)

plt.show()


# 5

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='diabetes', y='BMI')

plt.show()


# 6

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='diabetes', y='HbA1c_level')

plt.show()


# 7

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='diabetes', y='blood_glucose_level')

plt.show()


# 8

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='smoking_history', y='diabetes',hue='diabetes', legend=True)

plt.show()


# 9

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='smoking_history',y='blood_glucose_level')

plt.show()


# 10

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='smoking_history', y='BMI')

plt.show()


# 11

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.barplot(data=data, x='smoking_history',y='HbA1c_level')

plt.show()


# 12

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')
data['age_group'] = pd.cut(data['age'],bins=[0, 18, 35, 50, 65, 80],labels=['0-18', '19-35', '36-50', '51-65', '66-80'])
sns.barplot(data=data, x='age_group',y='blood_glucose_level')

plt.show()


# 13

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

data['age_group'] = pd.cut(data['age'],bins=[0, 18, 35, 50, 65, 80],labels=['0-18', '19-35', '36-50', '51-65', '66-80'])
sns.barplot(data=data, x='age_group', y='diabetes',hue='diabetes', legend=True)
plt.show()


# 14

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

data['age_group'] = pd.cut(data['age'],bins=[0, 18, 35, 50, 65, 80],labels=['0-18', '19-35', '36-50', '51-65', '66-80'])
sns.barplot(data=data, x='age_group', y='diabetes')
plt.show()


# 15

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.boxplot(data=data, x='diabetes', y='BMI',hue='diabetes', legend=True)

plt.grid()
plt.show()


# 16

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.boxplot(data=data, x='diabetes', y='HbA1c_level',hue='diabetes', legend=True)

plt.grid()
plt.show()


# 17

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.boxplot(data=data, x='diabetes',y='blood_glucose_level',hue='diabetes', legend=True)

plt.grid()
plt.show()


# 18

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

data['age_group'] = pd.cut(data['age'],bins=[0, 18, 35, 50, 65, 80],labels=['0-18', '19-35', '36-50', '51-65', '66-80'])
sns.boxplot(data=data, x='age_group',y='HbA1c_level',hue='age_group', legend=True)

plt.grid()
plt.show()


# 19

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

data['age_group'] = pd.cut(data['age'],bins=[0, 18, 35, 50, 65, 80],labels=['0-18', '19-35', '36-50', '51-65', '66-80'])
sns.boxplot(data=data, x='age_group',y='blood_glucose_level',hue='age_group', legend=True)

plt.grid()
plt.show()


# 20

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.boxplot(data=data, x='smoking_history',y='BMI',hue='smoking_history', legend=True)

plt.grid()
plt.show()


# 21

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')
sns.scatterplot(data=data,x='BMI',y='blood_glucose_level',hue='diabetes')
plt.show()


# 22

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.scatterplot(data=data,x='HbA1c_level',y='blood_glucose_level', hue='diabetes')

plt.show()


# 23

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.scatterplot(data=data,x='age',y='HbA1c_level',hue='diabetes')

plt.show()


# 24

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')
numerical_columns = data.select_dtypes(include='int64')
correlation_matrix = numerical_columns.corr()

sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',linecolor='black',linewidths=0.50)
plt.show()


# 25

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

sns.pairplot(
    data=data,
    vars=['age','BMI','HbA1c_level','blood_glucose_level','hypertension','diabetes'])

plt.show()