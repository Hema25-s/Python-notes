#               PANDAS
'''
it is a module used for data collection, cleaning, summarize, visualize the data in proper
manner.

it also needs to be installed by the following command

pip install pandas -. run this on ternimal

Before using pandas we need to import the file or module
'''

#              SERIES
'''
Series is a datastucture that used to store single column for a table.

It also have index that starts from 0 left that can be visible to the
each element


EXAMPLE FOR CREATING SERIES:

import pandas as pd

names = pd.Series(['A','B','C','D'])

print(names)


                       SERIES OPERATIONS

import pandas as pd

names = pd.Series(['A','B','C','D'])

print(names)
print(names[0])

print(names[1:])
print(names[::-1])

names[1] = '100'
print(names)


EX2:

import pandas as pd

names = pd.Series(['A','B','C','D'])

names =names.tolist()
print(names[-2])

                          MATH FUNCTIONS

import pandas as pd

salary = pd.Series([1,2,2,3,4])

total = salary.sum()  # min, max, mean, median
print(total)


                     AGGREGATION FUNCTIONS

used to take single report of all math functions


import pandas as pd

salary = pd.Series([1,2,2,3,4])

total = salary.aggregate(func=['mean','sum','max'])
print(total)

OUTPUT:
mean     2.4
sum     12.0
max      4.0
dtype: float64


                   OTHER FUNCTIONS

import pandas as pd

salary = pd.Series([234,56,5,64,6,45,45,45])

print(salary.dtype)
print(salary.shape)
print(salary.astype('str'))
print(salary.between(40,60))  # gives boolean value

#condition = salary.between(40,60)
condition = salary.ge(50)
result = salary[condition]
print(result)

salary.gt(50)
'''

#                      DATAFRAME
'''
A data structure like series that helps to store data in table format

It can be created using dictionary data structure and list

And it can be created from series


EXAMPLE FOR CREATION:

import pandas as pd

data = {
    'Name': ['A','B','C','D'],
    'Age':[24,34,54,34],
    'Salary':[3423,535,45,45]
}

df = pd.DataFrame(data)
print(df)

print(df['Age'])  # gives it as a series


             EXTRACT ONLY NEEDED DATA EXAMPLES

import pandas as pd

data = {
    'Name': pd.Series(['A','B','C','D']),
    'Age':[24,34,54,34],
    'Salary':[3423,535,45,45]
}

df = pd.DataFrame(data, columns=['Name','Age'])
print(df)

OUTPUT:
 Name  Age
0    A   24
1    B   34
2    C   54
3    D   34



               DATA FRAME OPERATIONS

import pandas as pd

data = {
    'Name': ['A','B','C','D'],
    'Age':[24,34,54,34],
    'Salary':[3423,535,45,45]
}

df = pd.DataFrame(data)
print(df['Name'].head(2))
print(df['Name'].tail(2))


OUTPUT:
0    A
1    B
Name: Name, dtype: str
2    C
3    D
Name: Name, dtype: str
'''

#                 CSV FILE DATA COLLECTION
'''
read_csv() is the function that are in pandas module used to collect
csv data as dataframe.

All the series and dataframe function can be applied here also.

             EXAMPLE FOR READ CSV:

import pandas as pd
df = pd.read_csv('data.csv')
print(df)

OUTPUT:
 EmployeeID  FirstName   LastName  Gender  Age  ...                      JobTitle       City  Salary    HireDate PerformanceRating
0         1001       John        Doe    Male   29  ...             Software Engineer    Chennai   85000  2022-01-15                 4
1         1002       Jane      Smith  Female   34  ...             Marketing Manager     Mumbai   72000  2021-08-10                 5
2         1003    Michael      Brown    Male   31  ...               Sales Executive  Bangalore   65000  2023-03-20                 3
3         1004      Emily      Davis  Female   28  .


      EX2:

import pandas as pd
df = pd.read_csv('data.csv')
print(df.columns)

OUTPUT:
Index(['EmployeeID', 'FirstName', 'LastName', 'Gender', 'Age', 'Department',
       'JobTitle', 'City', 'Salary', 'HireDate', 'PerformanceRating'],
      dtype='str')


     EX3:

import pandas as pd
df = pd.read_csv('data.csv')
print(df.columns.tolist())


     EX4:

import pandas as pd
df = pd.read_csv('data.csv')

print(df['Department'])
print(df['Department'].tolist())

print(df['Department'][7])

 
     EX5:

import pandas as pd
df = pd.read_csv('data.csv')

print(df.head())
print(df.tail())


                  DATA SELECTION WITH LOC, ILOC

Loc - label based location used to take particular part of data using label index
      Doesn't take n-1 data
 
ILoc - index based location used to take particular part of data using numeric index
       it take n-1 data

SYNTAX:

loc[start_row_index:end_row_index , start_col_index:end_col_index]



EXAMPLE FOR LOC:

import pandas as pd
df = pd.read_csv('data.csv')

df1 = df.loc[35:40, 'Gender':'JobTitle']
print(df1)


EXA<PLE FOR ILOC:

import pandas as pd
df = pd.read_csv('data.csv')

df1 = df.iloc[35:40, 3:6]
print(df1)

                  MULTIPLE COLUMN SELECTION

import pandas as pd
df = pd.read_csv('data.csv')

df1 = df[['Gender','JobTitle','Department']]

print(df1)


OUTPUT:
  Gender                      JobTitle   Department
0     Male             Software Engineer  Engineering
1   Female             Marketing Manager    Marketing
2     Male               Sales Executive        Sales
3   Female                 HR Specialist           HR
4     Male             Financial Analyst      Finance
5   Female               DevOps Engineer  Engineering
6     Male              Customer Support      Support
7   Female                   QA Engineer  Engineering
8     Male                    Accountant      Finance
9   Female                Content Writer    Marketing
10    Male           Engineering Manager  Engineering
11  Female                 Sales Manager        Sales
12    Male               Finance Manager      Finance
13  Female                     Recruiter           HR
14    Male          System Administrator           IT
15  Female                SEO Specialist    Marketing
16    Male                 Data Engineer  Engineering
17  Female             Account Executive        Sales
18    Male             Technical Support      Support
19  Female             Senior Accountant      Finance
20    Male             Backend Developer  Engineering
21  Female          Social Media Manager    Marketing
22    Male              Regional Manager        Sales
23  Female                    HR Manager           HR
24    Male              Network Engineer           IT
25  Female            Frontend Developer  Engineering


           EX2 FOR MULTI COLUMN SELECTION

import pandas as pd
df = pd.read_csv('data.csv')

df1 = df[['Gender','JobTitle','Department']]

print(df1.head())
'''


#                DATA FILTERING
'''

FILTERING EX1:

import pandas as pd

df = pd.read_csv('data.csv')
print(df.columns)

condition = df['Gender'] == 'Male' # gives the boolean value

#print(condition)

male_data = df[condition] # reterives the data that statisfies the condition
#print(male_data['Gender'])
print(male_data[['FirstName','Gender']].head())
print('Whole data size: ', df.shape)
print('Conditiona applied data size:',male_data.shape)


EX2:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.iloc[-1:-11:-1])


           MULTIPLE CONDITIONS

Can be give by bitwsie operators

&, |, ~


EX1:


import pandas as pd

df = pd.read_csv('data.csv')
condition = (df['Salary'] > df['Salary'].mean()) & (df['Gender'] == 'Male')

filter_data = df[condition].head()
print( df['Salary'].mean())
print(filter_data[['Salary','Gender']])


EX2:

import pandas as pd 

df = pd.read_csv('data.csv')
print(df['Department'].unique())

condition = (df['Department'] == 'HR') | (df['Department'] == 'Sales')

filter_data = df[condition].head()
print(filter_data[['Department']])


EX3:


import pandas as pd

df = pd.read_csv('data.csv')
print(df['Department'].unique())

condition = ~(df['Department'] == 'HR')

filter_data = df[condition].head()
print(filter_data[['Department']])


                 FILTERING CONDITION WITH STRING FUNCTIONS


import pandas as pd

df = pd.read_csv('data.csv')

condition = (df['FirstName'].str.startswith('J')) & (df['FirstName'].str.endswith('n')) 

fil_data = df[condition]

print(fil_data.head())

EX2:

import pandas as pd

df = pd.read_csv('data.csv')

condition = (df['FirstName'].str.find('a') != -1)

print(condition)

fil_data = df[condition]

print(fil_data.head())


EX3:

import pandas as pd

df = pd.read_csv('data.csv')

condition = (df['FirstName'].str.contains('a'))

print(condition)

fil_data = df[condition]

print(fil_data.head())

 
EX4:



import pandas as pd


df = pd.read_csv('data.csv')

def find_no_of_letter_on_text(txt):
    return len(txt)

# apply function used to apply some custom function to the each
# and every text value on the first name column
df['first_name_len'] = df['FirstName'].apply(find_no_of_letter_on_text)


condition = df['first_name_len'] > 5
fil_data = df[condition]

print(fil_data['FirstName'])


import pandas as pd

df = pd.read_csv('data.csv')

#                CREATE
# Adding new column
#f['Incremented_Salary'] = df['Salary'] + 100

#             DELETE
# removing old column, gives new dataframe that removes the
# column
# df2 = df.drop('Salary', axis=1)

# print(df2['Salary'])

#         UPDATE
print('Salary before increment')
print(df['Salary'])


df['Salary'] = df['Salary']+100
print('Salary After Increment')

print(df['Salary'])
'''


#               DATA CLEANING  & DATA PREPROCESSING
'''

                    DATA CLEANING

It is a process of filling empty value and removing duplicate values

                   WHAT IS NULL VALUE

A empty cell in any data structure, all kind of structure, unstructure,
semi structure data will have null values

                   DATA PREPROCESSING
                   
Changing one data type to another data, Adding, Removing, Updating
columns in the dataframe
Filter record on a dataframe


                   FILLING VALUE ONLY SPECIFIC COLUMN

import pandas as pd

df = pd.read_csv('data.csv')

print(df.isnull().sum())

#df['FirstName'] = df['FirstName'].ffill()

df[['Gender','JobTitle']] = df[['Gender','JobTitle']].ffill()

print(df.isnull().sum())

'''

#           HANDLING DUPLICATE VALUES HANDLING
'''
import pandas as pd

df = pd.read_csv('data.csv')

# con=(df.duplicated()) # gives boolean result
# fil=df[con]
# print(fil)

# print(df.duplicated().sum())

# print(df['JobTitle'].duplicated().sum())
# colums=df.columns.to_list()
# for i in colums:
#     print(i,df[i].duplicated().sum())
# print(df[['JobTitle','Gender']].duplicated().sum())


# df2=df.drop_duplicates()
# print(df2.duplicated().sum())
# df.drop_duplicates(inplace=True)
# df.ffill(inplace=True)
# df.to_csv('Cleaned_data.csv', index=False)
# print('Data cleaned...')


'''

#        AUTOMATION APPLICATION OVERVIEW
'''

create infinite while loop with the following options

   i). Ask user to enter file with try and except
   ii). else -> Ask user to following numbers

         1. For Null Value checking
         2. For Null value fill with ffill, 3.... bfill, 4.... fillna
         5. For Check duplicate values
         6. Drop duplicate values 
         7. For Save the cleaned file
         8. For exit


Use while, int, input, break
   
'''


#       STRING VALUE HANDLING AND DATE TIME HANDLING PROGRAM
'''            
import pandas as pd

df = pd.read_csv('data.csv')

df['HireDate'] = pd.to_datetime(df['HireDate'])
print(df.info())

categorical_data = df.select_dtypes(include=['str'])


#df['FirstName'] = df['FirstName'].str.lower()

#print(categorical_data.columns)
#print(df['HireDate'].dt.month)

#print(df)


num_data = df.select_dtypes(exclude=['str','datetime64']).astype('float64')

num_columns = num_data.columns.to_list()

df[num_columns] =  num_data.astype('float')

print(df.info())
'''


#                 REGEX - Regular expression
'''
It is process a making patterns using collection of symbols
to filter a string

It can created from string that denotes r infront of it.

EX: r''


SYMBOLS:
1. ^  - startswith
2. $ - endswith
3. .  - any single character
4. [a-zA-Z]  - macths small and cap  a to z
5. \d - matches no
6. {no_of_occurence} - {10}
7. +  - one or more char
8. * - zero or more char


EX:


import pandas as pd

df = pd.read_csv('data.csv')

pattern = r'^J.*'

condition= df['FirstName'].str.contains(pat=pattern)

fil_data = df[condition]

print(fil_data)


EX2:


import pandas as pd

df = pd.read_csv('data.csv')

pattern = r'^J.*n$'

condition= df['FirstName'].str.contains(pat=pattern)

fil_data = df[condition]

print(fil_data)


EX3:
import pandas as pd

df = pd.read_csv('data.csv')

pattern = r'^Jo{2}.n$'

condition= df['FirstName'].str.contains(pat=pattern)

fil_data = df[condition]

print(fil_data)




EX4:


import pandas as pd

df = pd.read_csv('data.csv')

pattern = r'^J.\d{3}.*n$'

condition= df['FirstName'].str.contains(pat=pattern)

fil_data = df[condition]

print(fil_data)


EX5:
import pandas as pd

df = pd.read_csv('data.csv')

df['FirstName'] = df['FirstName'].str.lower()

pattern = r'^[a-z]'

condition= df['FirstName'].str.contains(pat=pattern)

fil_data = df[condition]

print(fil_data)
'''



#                GROUP BY
'''
Used to summarize the data

SYNTAX:

df_name.groupby('categorical_col')['numerical_col'].aggregation_operation()

Aggregation function: sum, min, max, count, mean


SYNTAX_2:

df_name.groupby(['categorical_col_1','categorical_col_2'])['numerical_col'].aggregation_operation()


SYNTAX_3:

df_name.groupby(['categorical_col_1')[['numerical_col_1','numerical_col_2']].aggregation_operation()


SYNTAX_4:

df_name.groupby(['categorical_col_1','categorical_col_2'])[['numerical_col_1','numerical_col_2']].aggregation_operation()

'''

#import pandas as pd

#df = pd.read_csv('pattern.csv')

#df = df.ffill()
#df = df.bfill()

#df = df[~(df['Salary'].str.contains('invalid'))]

#df['Salary'] = df['Salary'].astype('int64')

#summ_data = df.groupby('Department')['Salary'].sum()

#summ_data = df.groupby(['Department','Age'])['Salary'].min()


# summ_data = df.groupby(['Department','Age'])['Salary'].agg(func=['min','mean','sum'])

# print(summ_data)




#nedd age catorgy column teen age,young , older get all age people get how much salary
'''
import pandas as pd

df = pd.read_csv('employee.csv')
def find_age_category(age):
    if age>=18 and age<=20:
        return "Teen"
    elif age>=21 and age<=40:
        return"Young"
    else:
        return"Older"

df = df[~(df['Salary'].str.contains('invalid'))]
df['Salary'] = df['Salary'].astype('int64')
df['Age_category']=df['Age'].apply(find_age_category)
condition=df.groupby(['Age_category','Department'])['Salary'].sum()
print(condition)



'''

#                      MERGE, JOIN, CONCAT
'''
Merging - Process of combining two dataframe with common columns,
          Atleast one common column are value should exists on both
          dataframe.

          SYNTAX:
          pd.merge(left_df,right_df, on='common_column', how='merge type')


          TYPES OF MERGE:

          1. inner  - Combines common values on both dataframe
          2. right -  All values from right and matched from left
          3. left  - All values from left and matched from right
          4. outter - Gives all values from both dataframe


EX:

import pandas as pd

data = {
    "emp_id": [101, 102, 103, 104, 105, 106],
    "name": ["Arun", "Bala", "Chitra", "Divya", "Ezhil",'Fiz'],
    "dept_id": [1, 2, 1, 3, 2, 5],
    "salary": [30000, 35000, 32000, 40000, 36000,34554]
}

employees = pd.DataFrame(data)

departments = pd.DataFrame({
    "dept_id": [1, 2, 3, 4],
    "department": ["IT", "HR", "Finance", "Marketing"]
})

result = pd.merge(employees, departments, on="dept_id", how='right')
print(result)



                     JOIN

Used to merge two dataframe using common index

SYNTAX:

left_df_name.join(right_df_name, how='join_type')



EX:

import pandas as pd

data = {
    "emp_id": [101, 102, 103, 104, 105, 106],
    "name": ["Arun", "Bala", "Chitra", "Divya", "Ezhil",'Fiz'],
    "dept_id": [1, 2, 1, 3, 2, 5],
    "salary": [30000, 35000, 32000, 40000, 36000,34554]
}

employees = pd.DataFrame(data).set_index('dept_id')

departments = pd.DataFrame({
    "dept_id": [1, 2, 3, 4],
    "department": ["IT", "HR", "Finance", "Marketing"]
}).set_index('dept_id')


joined_data = employees.join(departments, how='left')
print(joined_data)



                       CONCAT

used to combine rows and columns between multiple dataframe

SYNTAX:

pd.concat([df1,df2,df3......dfn])


For more than two common columns - row added
For only the common column with axis =1 - column added


EX FOR ROW APPEND:

import pandas as pd

data = {
    "emp_id": [101, 102, 103, 104, 105, 106],
    "name": ["Arun", "Bala", "Chitra", "Divya", "Ezhil",'Fiz'],
    "dept_id": [1, 2, 1, 3, 2, 5],
    "salary": [30000, 35000, 32000, 40000, 36000,34554]
}

employees = pd.DataFrame(data)


data2 = {
    "emp_id": [107, 108, 109, 110, 111, 112],
    "name": ["Arun", "Bala", "Chitra", "Divya", "Ezhil",'Fiz'],
    "dept_id": [1, 2, 1, 3, 2, 5],
    "salary": [30000, 35000, 32000, 40000, 36000,34554]
}

employees2 = pd.DataFrame(data2)

whole_data = pd.concat([employees, employees2])
print(whole_data.reset_index())




EXAMPLE FOR COLUMN WISE COMBINE:



import pandas as pd

data = {
    "emp_id": [101, 102, 103, 104, 105, 106],
    "name": ["Arun", "Bala", "Chitra", "Divya", "Ezhil",'Fiz'],
    "dept_id": [1, 2, 1, 3, 2, 5],
    "salary": [30000, 35000, 32000, 40000, 36000,34554]
}

employees = pd.DataFrame(data)

departments = pd.DataFrame({
    "dept_id": [1, 2, 3, 4],
    "department": ["IT", "HR", "Finance", "Marketing"]
})

whole_data = pd.concat([employees, departments], axis=1)
print(whole_data.ffill())

'''


#                   MERGE AUTOMATION PROJECT
''''
1. Ask user to select
   1. for row wise combine
   2. for column wise combine

   if 1:
   Ask user how many dataframe want to merge

   run for loop for use entered time to get
   all csv file names.
   
   read each csv file, and show how many common columns are exists on both
   dataframe, if no common column exist ask user to upload data only with common
   column

   If common column exists check wherethere it is eligible for row wise append or not.
   If eligible do row wise append, else not eligible


   
'''


#age category wise count  heart dis only take the count of 1 , smoking people who have heart dis check
#check which gender have more heart disease

# import pandas as pd

# df = pd.read_csv('diabetes.csv')


# print(df['gender'].value_counts().sort_values(ascending=False).index[0])

# def find_age_category(age):
#     if age >= 18 and age <= 20:
#         return "Teen"
#     elif age >= 21 and age <= 40:
#         return "Young"
#     else:
#         return "Older"


# df['Age_category'] = df['age'].apply(find_age_category)


# print("\nAge Category-wise Heart Disease Count")

# age_count = df[df['heart_disease'] == 1]

# print(age_count['Age_category'].value_counts())


# print("\nSmoking People with Heart Disease")

# smoking_people = df[(df['heart_disease'] == 1) &(df['smoking_history'] == 'current')]

# print(smoking_people.shape)

# print("\nGender-wise Heart Disease Count")

# gender_count = df[df['heart_disease'] == 1]

# print(gender_count['gender'].value_counts())


# # if gender_count['Male'] > gender_count['Female']:
# #     print("\nMale has more Heart Disease")
# # else:
# #     print("\nFemale has more Heart Disease")  