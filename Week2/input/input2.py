distance_input = input("Ile km przeszedłeś w tym miesiącu")
distance = int(distance_input)
days_go_around = 40075/distance
weeks_go_around  = days_go_around / 7
print("W takim tempie okrążenie ziemi zajmie Ci: ", weeks_go_around, "tygodni")