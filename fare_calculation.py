def cal_fare(trips):
    base_fare = 50
    result = ""
    trip_number = 1  
    for trip in trips:
        distance_fare = trip * 10 + base_fare
        result += f"Trip {trip_number}: ${distance_fare}\n"
        trip_number += 1  
    return result.strip()  

trips = [5, 10, 3]  # Distances in km
print(cal_fare(trips))
