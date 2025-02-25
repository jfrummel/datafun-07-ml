from datetime import datetime

x = datetime.now()
y = datetime.now()

print("Year:", x.year)
print("Month:", x.month)
print("Day:", x.day)
print("Hour:", x.hour)
print("Minute:", x.minute)
print("Second:", x.second)
print("Microsecond:", x.microsecond)
print("Timezone:", x.tzinfo) #timezone information, often None

print("Year:", y.year)
print("Month:", y.month)
print("Day:", y.day)
print("Hour:", y.hour)
print("Minute:", y.minute)
print("Second:", y.second)
print("Microsecond:", y.microsecond)
print("Timezone:", y.tzinfo) #timezone information, often None

print("x < y:", x < y)
print("x <= y:", x <= y)
print("x > y:", x > y)
print("x >= y:", x >= y)
print("x == y:", x == y)
print("x != y:", x != y)

print(x -y)