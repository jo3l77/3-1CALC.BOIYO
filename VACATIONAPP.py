#Vacations Cost

#functions and parameters example


def hotel_cost(days):
   userInput= int(input("How many days do you plan to stay?"))
   return (90*days)

def plane_ride_cost(city):
    userInput= input("Enter which city you want to travel to: ")
    if city == "Charlotte":
        return(185)
    elif city=="Tampa":
        return(220)
    elif city=="Pittsburgh":
        return(175)

def rental_car_cost(days):
    cost=40*days
    if days>7:
        cost = cost-40
    elif days>=3 and days<7:
        cost=cost-20
    return cost


def trip_cost(days,city,spending_money):
    return hotel_cost(days)+rental_car_cost(days)+plane_ride_cost(city)+spending_money

print(trip_cost(6,"Tampa",2000))
