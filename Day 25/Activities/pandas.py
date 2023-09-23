import pandas

# there are two types of data structures in pandas: series and data frame
# a data table is a data frame
# a single column is a series

data = pandas.read_csv("Day 25/Activities/weather_data.csv")
print(data["temp"]) # series
print(data) # data frame

# convert data frame to dictionary
data_dict = data.to_dict()
print(data_dict)

# convert series to list
temp_list = data["temp"].to_list()
print(temp_list)

# average temperature
average = data["temp"].max()
print(average)

# get data in columns
print(data["condition"]) # data["column_name"]
print(data.condition) # data.column_name

# get data in rows
print(data[data.temp == 12]) # data[data.column_name == "value"]

# get data where the temperature is at maximum
print(data[data.temp == data.temp.max()])
print(data[data.day == "Monday"])

# get the day where the temperature is at maximum
monday = data[data.day == "Monday"]
print(monday.condition)

# get the temperature of Monday in fahrenheit
monday = data[data.day == "Monday"]
print(monday.temp * 9/5 + 32)  # convert to fahrenheit