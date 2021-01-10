#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

import hmac
import hashlib
import os
import bcrypt 
import binascii
class passwordTester:

    @staticmethod
    def hash_password(password_string):
        #hashed_password = bcrypt.hashpw(password_string, bcrypt.gensalt())
        hashed_password = hashlib.pbkdf2_hmac('sha256',password_string,b'salt',10000,dklen=None)
        print(binascii.hexlify(hashed_password))
        return hashed_password


    @staticmethod
    def hash_check(cleartext_password, hashed_password):
        if bcrypt.checkpw(cleartext_password, hashed_password):
            print("Yes")
            return True
        else:
            print("No")  
            return False  

