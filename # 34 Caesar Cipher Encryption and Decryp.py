# 34 Caesar Cipher Encryption and Decryption

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("\nEncrypted Message:", encrypted)
print("Decrypted Message:", decrypted)