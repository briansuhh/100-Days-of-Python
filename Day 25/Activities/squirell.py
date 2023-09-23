import pandas

data = pandas.read_csv("Day 25/Activities/squirrel_data.csv")

# grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrel, red_squirrel, black_squirrel]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("Day 25/squirrel_count.csv")


# Another way to do it is to use the value_counts() method, but it will not be in a dictionary format
fur_color = data["Primary Fur Color"].value_counts()

grey_squirrel = fur_color["Gray"]
red_squirrel = fur_color["Cinnamon"]
black_squirrel = fur_color["Black"]

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel, red_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Day 25/Activities/squirrel_count.csv")



