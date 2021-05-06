import pyaes
import base64
import os

def __main__(): 
    #Reading image
    with open("dogg.jpg", "rb")as image:
        f = image.read()
        data = f
    #AES encryption
    iv = "InitializationVe"
    secLevel = input("Enter security level:1. 128 bits, 2. 192 bits, 3-other. 256 bits\n")
    if (secLevel == "1"):
        inputKey = os.urandom(16)
    elif (secLevel == "2"):
        inputKey = os.urandom(24)
    else:
        inputKey = os.urandom(32)
    mode = input("choose operation mode: 1.CTR, 2-other.OFB\n")
    if (mode == "1"):
        k = pyaes.AESModeOfOperationCTR(inputKey)
    else:
        k = pyaes.AESModeOfOperationOFB(inputKey, iv=iv)
    d = k.encrypt(data)
    #Base 64 Encode
    encoded = base64.b64encode(d).decode('utf-8')
    print(encoded)
    pic = open("image.txt", "w")
    pic.write(encoded)
    pic.close()

    pic = open("image.txt", "r")
    encryptedImage = base64.b64decode(pic.read())
    pic.close()

    if (mode == "1"):
        k = pyaes.AESModeOfOperationCTR(inputKey)
    else:
        k = pyaes.AESModeOfOperationOFB(inputKey, iv=iv)

    decryptedImage = k.decrypt(encryptedImage)

    pic = open("decryptedDogg.jpg", "wb")
    pic.write(decryptedImage)
    pic.close()
__main__()
