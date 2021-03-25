# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas


data = pandas.read_csv("weather_data.csv")
#this tells us what type of data is being stored
#print(type(data))
#this tells us to print the column labeled temp
#print(data["temp"])

#there are a lot of methods in pandas
#one that is very useful is to_dict. it converts your data to a pyton dictionary
data_to_dict = data.to_dict()
print(data_dict)

print(data["temp"].max())

#you can get data from column one of 2 ways. the attribute is case sensative
print(data["condition"]) #treated like key
print(data.condition)   #treated like an object

#filter data in rows
print(data[data.day == "monday"])

#find row with maximum
print(data[data.temp == data.temp.max()])

monday = data[data.day == "monday"]
monday_temp = int(monday.temp)
monday_temp_f = monday_tem * 1.8 + 32
print(monday_temp_f)

#create a data frame from scratch
data_dict = {
    "students": ["amy", "james", "angela"]
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("csv_data.csv")


