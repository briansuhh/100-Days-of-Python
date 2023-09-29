import smtplib
import datetime
import pandas
import random

my_email = "fill in your email"
password = "fill in your password"
smtp_server = "smtp.gmail.com"
smtp_port = 587 

now = datetime.datetime.now()  
random_letter = random.randint(1,3)

# open the birthdays csv file
data = pandas.read_csv("Day 32/birthday_wisher/birthdays.csv")
data = data.to_dict(orient="records")

# get the birthday person's name if today is their birthday
for person in data:
    if now.day == person["day"] and now.month == person["month"]:
        name = person["name"]
        email = person["email"]

        # open the letter_templates file and replace the name with the birthday person's name
        with open(f"Day 32/birthday_wisher/letter_templates/letter_{random_letter}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", name)

        # send the email
        with smtplib.SMTP(smtp_server, smtp_port) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday!!\n\n{letter}")

            