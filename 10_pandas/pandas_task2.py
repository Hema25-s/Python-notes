'''
                                    #taskkkk
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
print(df.isnull())
print("************************************************************************")
print(df.isnull().sum())
print("************************************************************************")
print(df.ffill())
print("************************************************************************")
print(df.bfill())
print("************************************************************************")
print(df.dropna())
print("************************************************************************")
print(df.fillna(0).head())
print("************************************************************************")
print(df.bfill(inplace=True).head())
print("************************************************************************")
print(df.ffill(inplace=True).tail())
print("************************************************************************")


#task1

import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition =  (df['Gender'] == 'Male')

filter_data = df[condition]
print(filter_data[['FirstName','Gender']])


#task2
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition =  (df['Gender'] == 'Female')

filter_data = df[condition]
print(filter_data[['FirstName','LastName','Gender']])



#task3
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition=df['Age']>40
print(condition)
filter_data=df[condition]
print(filter_data[['FirstName','Age','RoomType']])


#task4
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
print(df.iloc[-1:-11:-1])



#task5
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
average=df['RoomRate'].mean()
print(average)
print("************************************************************")
condition=df['RoomRate']>average
print(condition)
print("##########################################################")
filter_data=df[condition]
print(filter_data[['FirstName','Gender','RoomRate']])


#task6
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition=(df['Department']=='Sales')|(df['Department']=='HR')
Filter_data=df[condition]
print(Filter_data[['FirstName','Department']])



#task7
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition=~(df['Department']=='HR')
Filter_data=df[condition]
print(Filter_data[['FirstName','Department']])


#task8
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition=(df['Nights']>4)&(df['RoomType']=='Suite')
filter_data=df[condition]
print(filter_data[['FirstName','RoomType','Nights']])



#task9
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition=(df['Department']=='Sales')&(df['BookingStatus']=='Confirmed')
filter_data=df[condition]
print(filter_data[['BookingID','FirstName','Department','BookingStatus']])






#task10
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition=(df['BookingStatus']=='Cancelled')|(df['BookingStatus']=='Checked Out')
filter_data=df[condition]
print(filter_data[['BookingID','FirstName','Department','BookingStatus']])



#task11
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition=(df['FirstName'].str.startswith('J'))
filter_data=df[condition]
print(filter_data[['FirstName','LastName']])


#task12
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition=(df['FirstName'].str.endswith('n'))
filter_data=df[condition]
print(filter_data[['FirstName','LastName']])

#task13&14
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition=(df['FirstName'].str.contains('a'))&(df['FirstName'].str.contains('el'))
filter_data=df[condition]
print(filter_data[['FirstName','LastName']])




#task15
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
condition=(df['FirstName'].str.find('a')!=-1)
filter_data=df[condition]
print(filter_data[['FirstName','LastName']])



#task17
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
def find_name_lenght(name):
    return len(name)


df['first_name_len']=df['FirstName'].apply(find_name_lenght)
condition=df['first_name_len']>6
filter_data=df[condition]
print(filter_data[['FirstName','first_name_len']])




#task18
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
df['totalroomcost']=df['Nights']*df['RoomRate']
condition = df['totalroomcost']>0
filter_data = df[condition]
print(filter_data[['FirstName','Nights','RoomRate','totalroomcost']])


#task19
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
df['totalroomcost']=df['Nights']*df['RoomRate']
condition = df['totalroomcost']>50000
filter_data = df[condition]
print(filter_data[['BookingID','FirstName','Nights','RoomRate','totalroomcost']])



#task19&20
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
df['totalroomcost']=df['Nights']*df['RoomRate']
condition = (df['totalroomcost']>50000)&(df['BookingStatus']=='Confirmed')
filter_data = df[condition]
print(filter_data[['BookingID','FirstName','BookingStatus','totalroomcost']])




#task21
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
print("Before room rate increment")
print(df['RoomRate'])
print("After room rate increment")
df['RoomRate'] = df['RoomRate'] + 500
print(df['RoomRate'])


#task22
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
df2 = df.drop('PaymentMethod', axis=1)
print(df2)

'''
#task23
import pandas as pd
df=pd.read_csv('hotel_bookings.csv')
df['totalroomcost']=df['Nights']*df['RoomRate']
con = (df['totalroomcost']>50000)&(df['BookingStatus']=='Confirmed')
fil_data = df[con]
condition=(df['Gender']=='Male')&(df['Department']=='Sales')|(df['Department']=='Finance')&(df['Nights']>3)&(df['FirstName'].str.contains('a'))&(df['RoomRate']>30000)
filter_data=df[condition]
print(filter_data[['BookingID','FirstName','Gender','Department','Nights','totalroomcost','BookingStatus']])

print("*******************************************************")
df2=(df['Department']=='Finance')&(df['Gender']=='Male')&(df['Nights']>3)
fil=df[df2]
#print(fil[['Department','Gender','Nights']])












