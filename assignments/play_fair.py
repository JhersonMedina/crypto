#Getting the alphabet to ease things up
from string import ascii_uppercase
def build(text): #Builds the key matrix using text
    key = [[]]
    done = set() #characters that were already added to the matrix
    for i in text:
        if i == 'J':
            i = 'I'
        if i not in done:
            key[-1].append(i)
            done.add(i)
            if len(key[-1]) == 5:
                key.append([])
    for i in ascii_uppercase:
        if i == 'J':
            i = 'I'
        if i not in done:
            key[-1].append(i)
            done.add(i)
            if len(key[-1]) == 5:
                key.append([])
    key.pop(-1)
    return key
def find(key, c):
    for i in range(0, len(key)):
        for j in range(0, len(key[i])):
            if (key[i][j] == c):
                return [i, j]
    return [-1, -1] #Never gets here
def endecrypt(text, key, par):
    add = 1 if par == 1 else -1
    ans = ''
    for i in range(1, len(text), 2):
        row1, col1 = find(key, text[i])
        row2, col2 = find(key, text[i - 1])
        if (row1 == row2):
            ans += key[row1][(col1 + add + 5) % 5] + key[row2][(col2 + add + 5) % 5]
        elif (col1 == col2):
            ans += key[(row1 + add + 5) % 5][col1] + key[(row2 + add + 5) % 5][col2]
        else:
            ans += key[row1][col2] + key[row2][col1]
    return ans
def __main__ ():
    keyText = input('Enter the key: ')
    text = input('Enter text: ') 
    par = int(input('Enter 1 for encrypting, 0 for decrypting: '))
    keyText = keyText.upper()
    keyText = keyText.replace(' ', '')
    key = build(keyText)
    text = text.upper()
    text = text.replace(' ', '')
    text = text.replace('J', 'I')
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            text = text[0:i] + ('X' if text[i] != 'Y' else 'X') + text[i]
    if (len(text) % 2 == 1):
        text += ('X' if text[-1] != 'Y' else 'X')
    for i in key:
        print(i)
    print(text)
    print(endecrypt(text, key, par))
__main__()

