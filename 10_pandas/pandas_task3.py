'''
import pandas as pd

while True:

    try:
        file_name = input("Enter the CSV file : ")
        df = pd.read_csv(file_name)
        print("\nFile loaded successfully!")
        print(df)

    except Exception as e:
        print("Error:", e)
        print("Please enter a valid CSV file.\n")
        continue

    while True:
        print("\n========== DATA CLEANING MENU ==========")
        print("1. Check Null Values")
        print("->Filling null values")
        print(" a)Fill Null Values using ffill")
        print(" b)Fill Null Values using bfill")
        print(" c)Fill Null Values using fillna")
        print("->Removing null values")
        print("2.duplicate value checking")
        print("3. duplicate value removing")
        print("4. save clean file")
        print("5.changing data type")
        print("6.column merging")
        print("7.data selection")
        print("8.Exit....................")
        print("******************************************")

        try:
            choice = int(input("Enter your choice (1-8): "))

        except ValueError:
            print("Please enter a number from 1 to 8.")
            continue

        if choice == 1:
            print("\nNull values in each column:")
            print(df.isnull().sum())

        elif choice == 2:
            df = df.ffill()
            print("\nNull values filled using forward fill (ffill).")

        elif choice == 3:
            df = df.bfill()
            print("\nNull values filled using backward fill (bfill).")

        elif choice == 4:
            df = df.fillna(df)
            print("\nNull values filled using fillna.")

        elif choice == 5:
            total_duplicate_values=df.duplicated().sum()
            if total_duplicate_values>0:print("\nTotal duplicate values",total_duplicate_values)
            else:print("no duplicate values found")
      

        elif choice == 6:
            df = df.drop_duplicates()

            print("\nDuplicate rows removed:")

        elif choice == 7:
            df.to_csv('Cleaned_data.csv', index=False)
            print('Data cleaned...')

        
        elif choice == 8:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

    break

#1.null value handling options
# user press 1 a) filling null values b) removing null value a)1.ffill 2. bfill 3. fillna (choose the numerical and text column which has null values.NUMBERS-Fill mean values,TEXT-fill the word which is more occuried)
#2.duplicate value checking 3. duplicate value removing 4. save clean file 5.changing data type -give all the columns in what data type,user said which column should change and what data type need to change 
#6.column merging-show all the columns in data frame \ Get which 2 columns need to combine and combined column should be a new column in data frame
#7.data selection-user need to give starting and ending ROWS & COLUMNS export as new csv file 




df=pd.read_csv("pattern.csv")
print(df)
print("*********************************************")
print(df.info())
print("*********************************************")
print(df.shape)
print("*********************************************")
print(df.columns)
print("*********************************************")




import pandas as pd

while True:

    try:
        file_name = input("Enter the CSV file : ")
        df = pd.read_csv(file_name)
        print("\nFile loaded successfully!")
        print(df)

    except Exception as e:
        print("Error:", e)
        print("Please enter a valid CSV file.\n")
        continue

    while True:
        print("\n========== DATA CLEANING MENU ==========")
        print("1. Check Null Values")
        print("->Filling null values")
        print(" a)Fill Null Values using ffill")
        print(" b)Fill Null Values using bfill")
        print(" c)Fill Null Values using fillna")
        print("->Removing null values")
        print("2.duplicate value checking")
        print("3. duplicate value removing")
        print("4. save clean file")
        print("5.changing data type")
        print("6.column merging")
        print("7.data selection")
        print("8.Exit....................")
        print("******************************************")
        try:
            choice = int(input("Enter your choice (1-8): "))
        
        except ValueError:
            print("Please enter a number from 1 to 8.")
            continue

        if choice == 1:

            print("\nNull values in each column:")
            print(df.isnull().sum())

            print("\n a) Filling null values")
            print(" b) Removing null values")

            option = input("Choose a or b: ").lower()

            if option == "a":

                print("\nFilling methods:")
                print("1. ffill")
                print("2. bfill")
                print("3. fillna")

                method = int(input("Choose method (1-3): "))

                if method == 1:
                    df = df.ffill()
                    print("\nNull values filled using ffill.")

                elif method == 2:
                    df = df.bfill()
                    print("\nNull values filled using bfill.")

                elif method == 3:
                           numerical_data=df.select_dtypes(include=['int64','float64'])
                           numerical_columns = numerical_data.columns.to_list()

                
                           if numerical_data.isnull().sum().sum() > 0:
                               for column in numerical_columns:
                                   df[column] = df[column].fillna(int(numerical_data[column].mean()))
                                   print("Filled with numbers")
        
                           text_data=df.select_dtypes(exclude=['int64','float64'])
                           text_columns = text_data.columns.to_list() 
                               
                           if text_data.isnull().sum().sum()>0:
                                for column in text_columns:
                                    highest_occured_value = df[column].value_counts().sort_values(ascending=False).index[0]
                                    df[column]=df[column].fillna(highest_occured_value)

                else:
                    print("Invalid method.")

            elif option == "b":

                print("\n1. Remove rows with null values")
                print("2. Remove columns with null values")

                remove_choice = int(input("Choose (1-2): "))

                if remove_choice == 1:
                    df = df.dropna()
                    print("\nRows containing null values removed.")

                elif remove_choice == 2:
                    df = df.dropna(axis=1)
                    print("\nColumns containing null values removed.")

                else:
                    print("Invalid choice.")

            else:
                print("Invalid option.")

        elif choice == 2:

            total_duplicate_values = df.duplicated().sum()

            if total_duplicate_values > 0:
                print("\nTotal duplicate rows:", total_duplicate_values)
            else:
                print("\nNo duplicate values found.")

        elif choice == 3:

            total_duplicate_values = df.duplicated().sum()

            if total_duplicate_values > 0:
                df = df.drop_duplicates()
                print("\nDuplicate rows removed.")
            else:
                print("\nNo duplicate rows found.")

        elif choice == 4:

            output_file = input("Enter output CSV file name: ")

            if not output_file.endswith(".csv"):
                output_file = output_file + ".csv"

            df.to_csv(output_file, index=False)

            print("\nClean file saved successfully as", output_file)

        elif choice == 5:

            print("\nColumns and their current data types:")
            print(df.dtypes)

            column = input("\nEnter the column name to change: ")

            if column in df.columns:

                print("\n data types:")
                print("1. int")
                print("2. float")
                print("3. str")
                print("4. bool")

                dtype_choice = int(input("Choose data type (1-4): "))

                try:

                    if dtype_choice == 1:
                        df[column] = df[column].astype(int)

                    elif dtype_choice == 2:
                        df[column] = df[column].astype(float)

                    elif dtype_choice == 3:
                        df[column] = df[column].astype(str)

                    elif dtype_choice == 4:
                        df[column] = df[column].astype(bool)

                    else:
                        print("Invalid data type.")
                        continue

                    print("\nData type changed successfully.")
                    print(df.dtypes)

                except Exception as e:
                    print("Error while changing data type:", e)

            else:
                print("Column not found.")

        elif choice == 6:

            print("\nColumns in the DataFrame:")
            for column in df.columns:
                print(column)

            column1 = input("\nEnter first column: ")
            column2 = input("Enter second column: ")

            if column1 in df.columns and column2 in df.columns:

                new_column = input("Enter new column name: ")

                df[new_column] = (df[column1].astype(str)  +df[column2].astype(str))

                print("\nColumns merged successfully.")
                print(df)

            else:
                print("One or both columns not found.")

        elif choice == 7:
            print("Number of rows:",df.shape[0])
            print("\nAvailable columns:")
            columns=df.columns
            for i in range(len(columns)):
                print(i, ":", columns[i])

            try:
                start_row = int(input("\nEnter starting row: "))
                end_row = int(input("Enter ending row: "))

                start_col = int(input("Enter starting column number: "))
                end_col = int(input("Enter ending column number: "))

                selected_data = df.iloc[start_row:end_row + 1,start_col:end_col + 1]

                print("\nSelected Data:")
                print(selected_data)

                output_file = input("\nEnter CSV file name to export selected data: ")

                if not output_file.endswith(".csv"):
                    output_file = output_file + ".csv"

                selected_data.to_csv(output_file, index=False)

                print("\nSelected data exported successfully as",output_file)

            except Exception as e:
                print("Error:", e)

       
        elif choice == 8:

            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice. Please enter 1 to 8.")

    break


'''






import pandas as pd
employees = pd.DataFrame({
    "EmpID": [1, 2, 3, 4, 5],
    "Name": ["Asha", "Balu", "Chitra", "Deepak", "Eshan"],
    "Department": ["HR", "IT", "HR", "Finance", "IT"],
    "Salary": [50000, 60000, 55000, 70000, 65000]
})

departments = pd.DataFrame({
    "Department": ["HR", "IT", "Finance", "Admin"],
    "Location": ["Chennai", "Bangalore", "Mumbai", "Delhi"]
})

attendance = pd.DataFrame({
    "EmpID": [1, 2, 3, 4, 5],
    "DaysPresent": [20, 22, 18, 25, 24]
})

bonus = pd.DataFrame({
    "EmpID": [1, 3, 4],
    "Bonus": [5000, 4000, 6000]
})
'''
summ_data = employees.groupby('Department')['Salary'].sum()
print(summ_data)
print("**************************************************")
avg=employees.groupby('Department')['Salary'].mean()
print(avg)
print("*************************************************")
count_emp=employees.groupby('Department').count()
print(count_emp)
print("************************************************")
min_sal=employees.groupby('Department')['Salary'].min()
print(min_sal)
print("***********************************************")
max_sal=employees.groupby('Department')['Salary'].max()
print(max_sal)
print("***********************************************")
agg_sal=employees.groupby('Department')['Salary'].agg(func=['sum','mean','count'])
print(agg_sal)
print("************************************************")
list_sal=employees.groupby('Department')['Salary'].apply(list)
print(list_sal)
print("************************************************")
sal_var=employees.groupby('Department')['Salary'].var()
print(sal_var)
print("************************************************")
standard=employees.groupby('Department')['Salary'].std()
print(standard)
print("**********************************************)
def find_salary(Salary):
    if Salary>=60000:
        return 'High'
    else:
        return 'Low'
employees["Salarygroup"]=employees['Salary'].apply(find_salary)  

sal_group=employees.groupby('Salarygroup').sum()

'''
'''
result=pd.merge(employees,departments, on="Department",how="inner")
print(result)
print("********************************************************")
left=pd.merge(employees,departments,how='left')
print(left)
print("********************************************************")
right=pd.merge(departments,employees,how='right')
print(right)
print("********************************************************")
att=pd.merge(employees,attendance,on='EmpID')
print(att)
print("********************************************************")
bon=pd.merge(employees,bonus, how='inner')
print(bon)
print("********************************************************")
bon=pd.merge(employees,bonus, how='inner')
print(bon)
print("********************************************************")
bonu=pd.merge(employees,bonus,how='left')
print(bonu)
print("****************************************************")
multiple_merge=pd.merge(employees,attendance)
mul=pd.merge(multiple_merge,bonus)
print(mul)
print("***********************************************")
ren = employees.rename(columns={"Department": "DeptName"})
print(ren)
print("************************************************")
empid=pd.merge(attendance,bonus, on='EmpID', how='outer')
print(empid)
print("************************************************")
# suffix=pd.merge(employees,departments.add_suffix(departments))
# print(suffix)
'''
'''
employees_index = employees.set_index("EmpID")
attendance_index = attendance.set_index("EmpID")
bonus_index = bonus.set_index("EmpID")


j1=employees_index.join(attendance_index)
print(j1)
print("**************************************************")
j2=employees_index.join(bonus_index,how='left')
print(j2)
print("**************************************************")
j3=employees_index.join(bonus_index,how='outer')
print(j3)
print("**************************************************")
j4=employees_index.join(attendance_index)
print(j4.join(bonus_index,how='outer'))
print("**************************************************")
# joined_data = employees.join(attendance, how='left')
# print(joined_data)


'''

# departments = departments.add_suffix('00L')
# employees = employees.add_suffix('00L')


# suffix=pd.merge(employees,departments, on='Department00L')
# print(suffix)

'''
row_wise=pd.concat([employees,employees])
print(row_wise.reset_index())
print("***************************************************")
side=pd.concat([employees,bonus],axis=1)
print(side.reset_index())
print("****************************************************")
mismatch=pd.concat([attendance,bonus])
print(mismatch)
print("***************************************************")
three=pd.concat([employees,departments])
print(pd.concat([three,bonus],axis=0).reset_index())
'''


# 1. Ask user to select
#    1. for row wise combine
#    2. for column wise combine

#    if 1:
#    Ask user how many dataframe want to merge

#    run for loop for use entered time to get
#    all csv file names.
   
#    read each csv file, and show how many common columns are exists on both(use set)
#    dataframe, if no common column exist ask user to upload data only with common
#    column

#    If common column exists check wherethere it is eligible for row wise append or not.
#    If eligible do row wise append, else not eligible
'''
import pandas as pd

dfs = []

all_common_columns = ''

common_column_count = {}

no_of_files = 2

#  fetch_all_columns -> returns all columns in str format
# check_common_column -> returns the common columns in dict format

for i in range(no_of_files):
    dfs.append(pd.read_csv(input(f'Enter file {i}: ')))

for k in range(no_of_files):
    columns = dfs[k].columns.to_list()

    all_common_columns += ' '.join(columns)

for j in range(no_of_files):
    columns = dfs[k].columns.to_list()

    for z in columns:
        if all_common_columns.count(z) > 1:
            common_column_count[z] = all_common_columns.count(z)


# for key,value in common_column_count.items():
#     print(f'COLUMN {key}: {value}')
    
if len(common_column_count.items())>2:
    result=pd.concat(dfs,axis=0)
    print("===========================================================================================")
    print("Row wise merged")
    print(result)
else:
    result=pd.concat(dfs,axis=1)
    print("============================================================================================")
    print("Column wise merged")
    print(result)

    
'''

# concated_data = pd.concat(dfs)

# concated_data.to_csv('output.csv')

# try:
#         file_name = input("Enter the CSV file : ")
#         df = pd.read_csv(file_name)
#         print("\nFile loaded successfully!")
#         print(df)

# except Exception as e:
#         print("Error:", e)
#         print("Please enter a valid CSV file.\n")
        

# while True:
#         print("================DATA MERGING================")
#         print("\n 1. for row wise combine")
#         print("\n 2. for column wise combine")
#         print("\n 3.exit..................")

#         try:
#                     choice = int(input("Enter your choice (1-3): "))
        
#         except ValueError:
#                     print("Please enter a number from 1 to 3.")
#                     continue

#         if choice == 1:

#          n = int(input("How many CSV files? "))
#         df2 = []
#         for i in range(n):
#               file_name = input(f"Enter CSV file{i+1}: ")
#               df = pd.read_csv(file_name)
#               df2.append(df)
#               common = True
#               for column in df2[0].columns:
#                     for df in df2[1:]:
#                           if column not in df.columns:
#                                 common = False
#                                 if common == False:
#                                       print("No common columns.")
#                                       print("Please upload files with common columns.")
#                                 else:
#                                        same = True
#                                        for df in df2:
#                                         if list(df.columns) != list(df2[0].columns):
#                                                same = False
#                                                if same == True:
#                                                       result = pd.concat(df2)
#                                                       print("\nRow wise combine successful!")
#                                                       print(result)
#                                         else:
#                                                print("Row wise combine is not possible.")
#                                                print("All CSV files should have same columns.")



        
'''




import pandas as pd

dfs = []
while True:
    for i in range(2):
     file = input(f"Enter file {i}: ")
     dfs.append(pd.read_csv(file))

    def fetch_all_columns(dfs):
     columns = ""
     for df in dfs:
        columns += " ".join(df.columns)
     return columns

    print(type(fetch_all_columns(dfs)))

    def check_common_column(dfs):
        columns = fetch_all_columns(dfs)
        common_columns = {}
        for df in dfs:
          for col in df.columns:
             if columns.count(col) > 1:
                common_columns[col] = columns.count(col)
        return common_columns

    print(type(check_common_column(dfs)))
   
    if len() > 2:
     result = pd.concat(dfs)
     print("==========================================================================================================================")
     print("Row wise merged")
     print(result)
    else:
     result = pd.concat(dfs, axis=1)
     print("==========================================================================================================================")
     print("Column wise merged")
     print(result)


'''

  
  

import pandas as pd

while True:

    dfs = []

    n = int(input("How many files do you want to merge: "))

    for i in range(n):
        file = input(f"Enter file {i + 1}: ")
        df = pd.read_csv(file)
        dfs.append(df)

 
    common_columns = set(dfs[0].columns)

    for df in dfs[1:]:
        common_columns = common_columns & set(df.columns)

    print("\nCommon columns:")
    print(common_columns)

   
    choice = input("\n1. Row-wise\n2. Column-wise\nEnter choice: ")

    if choice == "1":
        result = pd.concat(dfs)
        print("\nRow-wise merged:")
        print(result)

    elif choice == "2":
        result = pd.concat(dfs, axis=1)
        print("\nColumn-wise merged:")
        print(result)

    else:
        print("Invalid choice!")

