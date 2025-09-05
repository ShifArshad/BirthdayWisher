import smtplib
import random
import datetime as dt
import pandas

##################### Extra Hard Starting Project ######################
PLACEHOLDER = "[NAME]"
MY_EMAIL = ""
PASSWORD = ""

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
date_tuple = (dt.datetime.now().month, dt.datetime.now().day)

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv

if date_tuple in birthday_dict:
    birthday_person = birthday_dict[date_tuple]
    letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file=letter) as letter1:
        content = letter1.read()
        content = content.replace(PLACEHOLDER, birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday_person["email"],
                                msg=f"Subject:HAPPY BIRTHDAY\n\n{content}")

















# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
