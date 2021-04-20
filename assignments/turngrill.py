def rotate(key, n, d):
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            aux = key[i][j];
            if d == 0: #Anticlockwise rotation
                key[i][j] = key[j][n - i - 1]
                key[j][n - i - 1] = key[n - i - 1][n - j - 1]
                key[n - i - 1][n - j - 1] = key[n - j - 1][i]
                key[n - j - 1][i] = aux
            else: #clockwise rotation
                key[i][j] = key[n - j - 1][i]
                key[n - j - 1][i] = key[n - i - 1][n - j - 1]
                key[n - i - 1][n - j - 1] = key[j][n - i - 1]
                key[j][n - i - 1] = aux
    return key
def encrypt(key, text, a, n, d):
    k = 0
    for rot in range(4):
        for i in range(n):
            for j in range(n):
                if key[i][j] == 1:
                    a[i][j] = text[k]
                    k = k + 1
        key = rotate(key, n, d)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = "")
    print()
def decrypt(key, text, a, n, d):
    for i in range(len(text)):
        a[i//n][i % n] = text[i]
    k = 0
    for rot in range(4):
        for i in range(n):
            for j in range(n):
                if key[i][j] == 1:
                    print(a[i][j], end = "")
        key = rotate(key, n, d)
    print()
def __main__():
    n = int(input("Enter the matrix size: "))
    d = int(input("Enter the direction (1 clockwise, 0 anticlockwise): "))
    m = int(input("Enter the amount of holes in the grille: "))
    print("Enter the row and the column of each hole in the matrix, take into account that (0, 0) is the top left corner: ")
    key = []
    a = []
    for i in range(n):
        aux = [0] * n
        aux2 = ['A'] * n
        key.append(aux)
        a.append(aux2)
    for i in range(m):
        print("Point: ", i + 1)
        r = int(input())
        c = int(input())
        key[r][c] = 1
    p = int(input("Enter the 1 for encrypting and 0 for decrypting: "))
    text = input("Enter the text: ")
    text = text.replace(" ", "")
    text = text.upper()
    while len(text) < n * n:
        text = text + 'X'
    if p == 1:
        encrypt(key, text, a, n, d)
    else:
        decrypt(key, text, a, n, d)
__main__()
