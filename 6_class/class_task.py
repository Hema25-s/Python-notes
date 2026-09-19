
'''
#task1
class Hotel:
    hotel_name = ''
    location = ''
    check_in_time = ''

    def __init__(self, hotel_name, location, check_in_time):
        self.hotel_name = hotel_name
        self.location = location
        self.check_in_time = check_in_time

    def display_hotel_details(self, room_no):

        if room_no == 101:
            room_type = "Deluxe Room"
        else:
            room_type = "Standard Room"

        details = f"""
Hotel name: {self.hotel_name}
Location: {self.location}
Check-in time: {self.check_in_time}
Room type: {room_type}
"""

        return details


class Guest(Hotel):
    guest_name = ''
    age = 0

    def __init__(self, hotel_name, location, check_in_time, guest_name, age):
        super().__init__(hotel_name, location, check_in_time)
        self.guest_name = guest_name
        self.age = age

    def display_guest_details(self, room_no):

        hotel_details = self.display_hotel_details(room_no)

        guest_details = f"""
Guest name: {self.guest_name}
Age: {self.age}
"""

        return  guest_details

hotel1=Hotel("Taj Hotel", "Chennai", "14:00")
print(hotel1.display_hotel_details(101))    


guest = Guest("Taj Hotel", "Chennai", "14:00", "Hema", 25)

print(guest.display_guest_details(101))










#task2


class Bus:
    from_location = ''
    to_location = ''
    departure_time = ''

    def __init__(self, from_location, to_location, departure_time):
        self.from_location = from_location
        self.to_location = to_location
        self.departure_time = departure_time

    def display_bus_details(self, bus_no):

        if bus_no == 101:
            bus_type = "AC Sleeper"
        else:
            bus_type = "Non-AC Seater"

        details = f"""
Bus type: {bus_type}
From: {self.from_location}
To: {self.to_location}
Departure time: {self.departure_time}
"""

        return details


class Passenger(Bus):

    passenger_name = ''
    age = 0

    def __init__(self, from_location, to_location, departure_time,
                 passenger_name, age):

        super().__init__(from_location, to_location, departure_time)

        self.passenger_name = passenger_name
        self.age = age

    def display_passenger_details(self, bus_no):

        self.display_bus_details(bus_no)

        passenger_details = f"""
Passenger name: {self.passenger_name}
Age: {self.age}
"""

        return  passenger_details


bus1=Bus("Erode","Chennai","22:00" )    
print(bus1.display_bus_details(101))

passenger = Passenger("Erode", "Chennai","22:00", "Ravi", 30)

print(passenger.display_passenger_details(102))





#task3





class Movie:
    movie_name = ''
    theatre_name = ''
    show_time = ''

    def __init__(self, movie_name, theatre_name, show_time):
        self.movie_name = movie_name
        self.theatre_name = theatre_name
        self.show_time = show_time

    def display_movie_details(self,age):

        if age >= 18:
            status = "Allowed for movie"
        else:
            status = "Not allowed for movie"

        details = f"""
Movie name: {self.movie_name}
Theatre name: {self.theatre_name}
Show time: {self.show_time}
Status: {status}
"""

        return details


class Customer(Movie):

    customer_name = ''
    age = 0

    def __init__(self, movie_name, theatre_name, show_time,
                 customer_name, age):

        super().__init__(movie_name, theatre_name, show_time)

        self.customer_name = customer_name
        self.age = age

    def display_customer_details(self):

         self.display_movie_details(self.age)

         customer_details = f"""
Customer name: {self.customer_name}
Age: {self.age}
"""

         return  customer_details

movie1=Movie("Leo","PVR Cinemas","18:30")   
print(movie1.display_movie_details(19))


customer = Customer( "Leo", "PVR Cinemas","18:30","Karthik",20)

print(customer.display_customer_details())




#task4


class Flight:
    from_location = ''
    to_location = ''
    departure_time = ''

    def __init__(self, from_location, to_location, departure_time):
        self.from_location = from_location
        self.to_location = to_location
        self.departure_time = departure_time

    def display_flight_details(self, flight_no):

        if flight_no == 101:
            flight_type = "Domestic Flight"
        else:
            flight_type = "International Flight"

        details = f"""
Flight type: {flight_type}
From: {self.from_location}
To: {self.to_location}
Departure time: {self.departure_time}
"""

        return details


class Passenger(Flight):

    passenger_name = ''
    age = 0

    def __init__(self, from_location, to_location, departure_time,
                 passenger_name, age):

        super().__init__(from_location, to_location, departure_time)

        self.passenger_name = passenger_name
        self.age = age

    def display_passenger_details(self, flight_no):

        self.display_flight_details(flight_no)

        passenger_details = f"""
Passenger name: {self.passenger_name}
Age: {self.age}
"""

        return   passenger_details
    
flight=Flight("Chennai","Delhi", "09:30")
print(flight.display_flight_details(101))

passenger = Passenger("Chennai","Delhi", "09:30", "Priya", 2)

print(passenger.display_passenger_details(101))



#task5
class Restaurant:
    restaurant_name = ''
    location = ''
    opening_time = ''

    def __init__(self, restaurant_name, location, opening_time):
        self.restaurant_name = restaurant_name
        self.location = location
        self.opening_time = opening_time

    def display_restaurant_details(self):

        if self.opening_time == "12:00":
            meal = "Lunch"
        else:
            meal = "Dinner"

        details = f"""
Restaurant name: {self.restaurant_name}
Location: {self.location}
Opening time: {self.opening_time}
Meal: {meal}
"""

        return details


class Customer(Restaurant):

    customer_name = ''
    age = 0

    def __init__(self, restaurant_name, location, opening_time,
                 customer_name, age):

        super().__init__(restaurant_name, location, opening_time)

        self.customer_name = customer_name
        self.age = age

    def display_customer_details(self):

        restaurant_details = self.display_restaurant_details()

        customer_details = f"""
Customer name: {self.customer_name}
Age: {self.age}
"""

        return restaurant_details + customer_details


customer = Customer("Anjappar","Erode","12:00","Suresh",35)

print(customer.display_customer_details())
'''

#task6



class School:
    school_name='' 
    class_name=''
    school_timming=''
    def __init__(self,school_name,class_name,school_timming):
        self.school_name=school_name
        self.class_name=class_name
        self.school_timming=school_timming

    def display_school_detail(self):

        school_details=f"""
school name={self.school_name}
class name={self.class_name}
school timming={self.school_timming}

"""


        return school_details

class Student(School):
    student_name='' 
    age=0
    def __init__(self, school_name, class_name, school_timming,student_name,age):
        super().__init__(school_name, class_name, school_timming)  
        self.student_name=student_name
        self.age=age
        
    def display_student_detail(self):
            self.display_school_detail()

            if self.age>=15:
                     student_type = "Senior Student"
            else:
                student_type = "Junior student"

            student_details=f"""

            Student_name={self.student_name}
            Age={self.age}
            Student_type={self.student_name}

     """   

      
            return student_details      
          
    