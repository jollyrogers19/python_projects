import datetime as dt
import pandas
import random
import smtplib

my_mail="yourmail@gmail.com"
password="xxxxxxxxxxxx"

now=dt.datetime.now()
today = (now.month, now.day)

data=pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person=birthdays_dict[today]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail,password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=birthday_person["email"],
            msg=f"Happy Birthday!!\n\n{contents}")







