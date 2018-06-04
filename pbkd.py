import hashlib, binascii, datetime
salt = ‘{:%H:%M:%S}’.format(datetime.datetime.now())
password = raw_input(“Enter your password: ”)
pbkd = hashlib.pbkdf2_hmac(“sha256”,password,salt,1)
pbkd = binascii.hexlify(pbkd)
print(“Your derived key is: ”,pbkd)
