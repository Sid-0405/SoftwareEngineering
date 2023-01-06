import datetime
import pandas as pd
import smtplib
import os

os.chdir(r"D:\python practise\LAB")


def sendEmail(to, sub, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587);
    server.starttls()
    server.login('hulke1102002@gmail.com', "tyfqxwmnvxlakudg");
    server.sendmail("hulke1102002@gmail.com", to, f"Subject: {sub}\n\n{msg}");
    server.quit();


if __name__ == "__main__":

    df = pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    year = datetime.datetime.now().strftime("%Y")
    # Excel Data
    birthday="06/01"

    if today == birthday:
        print('hulke1102002@gmail.com')
        sendEmail('hulke1102002@gmail.com', "Happy Birthday", 'Wish you a very happy birthday bhaava 🥳🎉🎊🎊')

