# Author:- Kunal Raju Hulke
# Prn:-2030331245020
import random
import smtplib
# importing data from filew
# file = open("data.txt", "r")

# By using file handling we can access/import the data from another file

Sender_email = "hulke1102002@gmail.com"
Sender_pass = "ccriexgmhuvybrfi"

def Send_OTP(Otp):
    # Getting mail_id from user that whom user wana send otp
    recevicer_mail = input("Enter Recevicers-Email id: ")
    if ("@gmail.com" in recevicer_mail):
        message = "Your OTP is " + Otp
        server.sendmail(Sender_email, recevicer_mail,"Subject:OTP \n" + message)
        print("Congratulation!! 🥳Your OTP Generates Successfully🥳")
    else:
        print("You entered an Invalid Email!!!!🥵🥵")

def Generate_Otp():
    print("Press 1 for only Numeric OTP.")
    print("Press 2 for Both.")
    User_input = int(input("Enter: "))

    # if user wants only numeric otp then if will run
    if (User_input == 1):
        length_of_otp = int(input("Enter the length of OTP: "))
        Otp = ""
        for i in range(length_of_otp):
            Random_NO = random.randint(0, 9)
            Otp = Otp + str(Random_NO)
        Send_OTP(Otp)
    # if user wants both numeric and char then else part will run
    else:
        length_of_otp = int(input("Enter the length of OTP: "))
        Otp = ""
        if (length_of_otp % 2 == 0):
            for i in range(int(length_of_otp / 2)):
                Random_no = random.randint(0, 9)
                Random_char = random.randint(97, 123)
                convert_NtC = chr(Random_char)
                Otp = Otp + str(Random_no) + convert_NtC
            Send_OTP(Otp)
        else:
            for i in range((int(length_of_otp / 2))):
                Random_no = random.randint(0, 9)
                Random_char = random.randint(97, 123)
                convert_NtC = chr(Random_char)
                Otp = Otp + str(Random_no) + convert_NtC
            Otp = Otp + chr(random.randint(97, 123))
            Send_OTP(Otp)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# By using server.login function we can login to that particular login
server.login(Sender_email, Sender_pass)
Generate_Otp()
server.close()