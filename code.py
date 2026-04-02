def encrypt_route_cipher(text, rows, cols):
    text = text.replace(" ", "").upper()

    # Fill matrix row-wise
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    
    k = 0
    for i in range(rows):
        for j in range(cols):
            if k < len(text):
                matrix[i][j] = text[k]
                k += 1
            else:
                matrix[i][j] = 'X'  # padding

    # Read column-wise
    cipher = ""
    for j in range(cols):
        for i in range(rows):
            cipher += matrix[i][j]

    return cipher


def decrypt_route_cipher(cipher, rows, cols):
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    # Fill column-wise
    k = 0
    for j in range(cols):
        for i in range(rows):
            matrix[i][j] = cipher[k]
            k += 1

    # Read row-wise
    text = ""
    for i in range(rows):
        for j in range(cols):
            text += matrix[i][j]

    return text


# Example
plaintext = "HELLO WORLD"
rows, cols = 2, 5

cipher = encrypt_route_cipher(plaintext, rows, cols)
print("Encrypted:", cipher)

decrypted = decrypt_route_cipher(cipher, rows, cols)
print("Decrypted:", decrypted)
