import csv
with open("Work/Python/Weather.csv", "r") as file:
    data = list(csv.reader(file))

print(data)

city = input("Enter a city name: ")

for row in data[1:]:
    print(row)
    if row[1] == city:
        print(row[2])