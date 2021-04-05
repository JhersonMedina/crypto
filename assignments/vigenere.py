#Getting the alphabet to ease things up
from string import ascii_uppercase
def __main__ ():
    key = input('Enter the key: ')
    key = key.replace(' ', '')
    key = key.upper()
    t = int(input('Enter T parameter: '))
    text = input('Enter the text: ')
    text = text.replace(' ', '')
    text = text.upper()
    while len(text) % t != 0:
        text = text + 'X'
    par = int(input('Enter 1 for encrypting, 0 for decrypting: '))
    add = 1 if par == 1 else -1
    i = 0
    j = 0
    while i < len(text):
        less = ord('A')
        a = ord(text[i])
        b = ord(key[j])
        print(ascii_uppercase[((a - less) + add * (b - less) + 26) % 26], end = "")
        if i % t == t - 1:
            print(" ", end = "")
        i += 1
        j = (j + 1) % len(key)
    print("")
__main__()

