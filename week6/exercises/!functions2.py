# Write the function that calculates average velocidad based on the 
# distance and time. Use it by implementing a programme, that will 
# calculate average run velocidad, average biking velocidad and
# average car velocidad

def avg_speed(distance, time):
    return distance/time

print(f"Velocidad is equal to {avg_speed(5, 2)}km/h")



def run_avg_speed(vehicle_name):
    distance = float(input(f"How many km have you travelled by {vehicle_name}"))
    time = float(input(f"How much time did you spend on it"))
    average_speed = avg_speed(distance, time)
    print(f"Your average velocidad by {vehicle_name} is {average_speed}km/h")

run_avg_speed("car")

