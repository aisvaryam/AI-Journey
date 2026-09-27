recorded_speeds = [65, 82, 45, 90, 75, 110, 55, 81]

def find_speeders(speeds,speed_limit):
    speeders = []

    for speed in speeds:
        if speed > speed_limit:
           speeders.append(speed) 

    return speeders

result = find_speeders(recorded_speeds,80)
print(result)   
