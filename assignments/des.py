from pyDes import *
import base64
def __main__():
    #Reading image
    with open ("dogg.jpg", "rb") as image:
        f= image.read()
        b = bytes(f)
    key = ""
    while len(key) != 8:
        key = input("Enter the 8 character key: ")
        key = key.replace(" ", "")
        key.upper()
    #Des encrytption
    data = b  
    k = des(key, CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(data)
    #Base 64 Encode
    text = d
    print("DES encrypted text: ", text)
    base64_bytes = base64.b64encode(text)
    print(f"Base 64 encrypted text: {base64_bytes}")
    #Base 64 Decode
    base64Text = base64_bytes.decode("ascii")
    byteString = base64.b64decode(base64Text)
    print(f"Decrypted text: {byteString}")
    pic = open("decryptedDogg.jpg", "wb")
    pic.write(k.decrypt(byteString))
    pic.close()
__main__()
