# Continue 

favourite_sports = ["running", "swimming", "biking", "triathlon"]
for index, sport in enumerate(favourite_sports):
    if index % 2 != 0:
        continue
    print(sport)