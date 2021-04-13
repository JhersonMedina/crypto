from string import ascii_uppercase
def multiply (a, b):
    ans = []
    for i in range(2):
        v = []
        for j in range(2):
            x = 0
            for k in range(2):
                x = x + a[i][k] * b[k][j];
            v.append(x);
        ans.append(v)
    return ans
def encrypt(text, key):
    while len(text) % 4 != 0:
        text = text + 'x'
    text = text.replace(' ', '')
    text = text.upper()
    ans = "" 
    for i in range(0, len(text), 4):
        c1 = [ord(text[i]) - ord('A'), ord(text[i + 1]) - ord('A')]
        c2 = [ord(text[i + 2]) - ord('A'), ord(text[i + 3]) - ord('A')]
        a = multiply([c1, c2], key)
        for x in range(2):
            for y in range(2):
                ans = ans + ascii_uppercase[a[x][y] % 26]
    return ans
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = egcd(b%a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
def decrypt(text, key):
    det = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    adj = [[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]
    g, x, y = egcd(det, 26)
    if (g != 1):
        print("Invalid input")
        quit()
    for i in range(2):
        for j in range(2):
            adj[i][j] = (adj[i][j] * x % 26 + 26) % 26 
    return encrypt(text, adj)
def __main__():
    text = input("Enter the text: ")
    print('Enter the key one number at a time, fromt top left to bottom right: ')
    key = []
    for i in range(2):
        x = []
        for j in range(2):
            x.append(int(input()))
            x[-1] = x[-1] % 26
        key.append(x)
    par = int(input('Enter 1 for encrypting, 0 for decrypting: '))
    if par == 1:
        print(encrypt(text, key))
    else:
        print(decrypt(text, key))
__main__()

