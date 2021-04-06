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

#this tells what file to read. because i do not have excel it didnt work however this is how it looks
quote = pandas.read_csv("squirrel.csv")

#this isolates and counts the number of each color
grey_squirrels = len(quote[quote["primary fur color"] == "grey"])
red_squirrels = len(quote[quote["primary fur color"] == "cinnamon"])
black_squirrels = len(quote[quote["primary fur color"] == "black"])

#this displays them for us
print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)


data_dict = {
    "fur color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]

}

#turn to data frame(write new csv file)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")






