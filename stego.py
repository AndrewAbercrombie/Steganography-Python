import base64
import os

image = input("Image Path: ")
os.system('cls')
image_b64 = ""
with open(image, "rb") as image_file:
    image_b64 = str(base64.b64encode(image_file.read()))

user_input = input("Encrypt/Decrypt: ")
os.system('cls')

if user_input.lower() == "e" or user_input.lower() == "encrypt":
    secret_msg = input("Enter Secret Message: ")
    os.system('cls')
    space_index = [i for i, ltr in enumerate(secret_msg) if ltr == " "] 
    secret_msg = secret_msg.replace(" ", "")

    key_list = []
    for i in secret_msg:
        key_list.append(image_b64.index(i))

    for i in space_index:
        key_list.insert(i, -1)

    keyStr = ""
    for key in key_list:
        keyStr += str(key) + " "

    key = base64.b64encode(keyStr.encode('utf-8')).decode('utf-8') 

    print("Secret Key: " + key)
elif user_input.lower() == "d" or user_input.lower() == "decrypt":
    key = input("Enter Key: ")
    os.system('cls')

    keyStr = base64.b64decode(key).decode('utf-8')
    key_list = keyStr.split()
    key_list = [int(x) if x != " " else " " for x in key_list]

    secret_msg = ""
    for key in key_list:
        if key == " ":
            secret_msg += " "
        elif key == -1:
            secret_msg += " " 
        else:
            secret_msg += image_b64[key]

    print("Decrypted Secret Message: " + secret_msg)