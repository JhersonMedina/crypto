#Getting the alphabet to ease things up
from string import ascii_uppercase
def endecrypt(text, k, par):
    add = 1 if par == 1 else -1
    ans = ''
    for c in text:
        i = ord(c)
        less = ord('A')
        ans += ascii_uppercase[(i - less + add * k) % 26]
    return ans
def __main__ ():
    text = input('Enter the text: ')
    k = int(input('Enter K parameter: '))
    par = int(input('Enter 1 for encrypting, 0 for decrypting: '))
    text = text.replace(' ', '')
    text = text.upper()
    print(endecrypt(text, k, par))
__main__()

