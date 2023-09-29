import datetime
import random
import smtplib

# hqdg mblp kpps zicn

my_email = "fill in your email"
password = "fill in your password"
smtp_server = "smtp.gmail.com"
smtp_port = 587 

now = datetime.datetime.now()  

def send_quotes(): 
    # open the quotes file
    with open("Day 32/quotes_sender/quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
        print(quote)

    # send the email
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="brianmaysebastian@gmail.com" , msg=f"Subject:Random Quotes\n\n{quote}")


if now.weekday() == 4:
    send_quotes()   

