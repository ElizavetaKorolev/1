text = input("Введите строку: ")
while True:
    k_input = input("Введите сдвиг (целое число): ")
    if k_input.lstrip('-').isdigit():
        k = int(k_input)
        break
    else:
        print("Ошибка! Пожалуйста, введите целое число.")
result = ""
for char in text:
    if char.isalpha() and char.isascii():
        start = ord('A') if char.isupper() else ord('a')
        shifted = start + (ord(char) - start + k) % 26
        result += chr(shifted)
    else:
        result += char
print("Зашифрованный текст:", result)