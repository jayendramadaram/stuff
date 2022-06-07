from email import message
from cryptography.fernet import Fernet
key = "https://www.youtube.com/watch?v=NUYvbT6vTPs"
print(key)
# input()
fernet = Fernet(key)


message = """"""

message1 = """"""

method = int(input("mama array method enti ra : "))
if method == 1:
    encMessage = fernet.encrypt(message.encode())
    print("original string: ", message)
    print(encMessage)
elif method == 2:
    decMessage = fernet.decrypt(message1).decode()
    print(decMessage)
