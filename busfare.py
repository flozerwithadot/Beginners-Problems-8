stop = int(input("what stop are you at? "))
go = int(input("what stop do you want to go to? "))
fare = 5 + (go - stop) * 2.50
total = round(fare, 2)
print(f"the fare from stop {stop} to stop {go} is ${total}")
