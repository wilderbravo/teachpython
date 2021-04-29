from collections import namedtuple
Station = namedtuple("Station", "id, city, state, lat, long")
denver = Station(44, "Denver", "CO", 40, 105)
print(denver)
print(denver.state)

print(denver[1])
