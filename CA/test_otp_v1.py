#author: Kunal Raju Hulke
#prn : 2030331245020
from otpgeneratorV1 import Send_OTP
from otpgeneratorV1 import Generate_Otp
import unittest

class TestOtp(unittest.TestCase):
    def test_1(self):
        email = "hulke1102002@gmail.com" #for validating email
        if "@gmail.com" in email:
            print("Validate Email🥳🎉👍😊")
        else:
            print("Invalid Email🥵😥")

if __name__ ==  '__main':
        unittest.main()