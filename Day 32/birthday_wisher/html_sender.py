from jinja2 import Environment, FileSystemLoader
import smtplib
import datetime
import pandas
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

env = Environment(loader=FileSystemLoader(searchpath="Day 32/birthday_wisher/html_template"))
template = env.get_template("letter.html")

my_email = "fill in your email"
password = "fill in your password"
smtp_server = "smtp.gmail.com"
smtp_port = 587 

now = datetime.datetime.now()  
random_letter = random.randint(1, 3)

# open the birthdays csv file
data = pandas.read_csv("Day 32/birthday_wisher/birthdays.csv")
data = data.to_dict(orient="records")

# get the birthday person's name if today is their birthday
for person in data:
    if now.day == person["day"] and now.month == person["month"]:
        name = person["name"]
        email = person["email"]

        variables = {
            "name": name,
            "sender": "Ayumi",
        }

        # render the html template with the variables
        letter = template.render(variables)

        # send the email
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = email
        msg['Subject'] = 'Happy Birthday!!'
        
        # Attach the HTML content with UTF-8 encoding
        msg.attach(MIMEText(letter, 'html', 'utf-8'))

        with smtplib.SMTP(smtp_server, smtp_port) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=msg.as_string())