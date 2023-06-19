# запись в  файл байтовых строк
from pathlib import Path

message = "Привет мир! Hello world"
# b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82 \xd0\xbc\xd0\xb8\xd1\x80! Hello world'
print(message.encode("utf-16"))  # используют китайцы
print(message.encode("cp1251"))  # кодирование windows OS

a = message.encode("cp1251")

print(a)
# print(a.decode("cp1251"))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xcf in position 0: invalid continuation byte
# print(a.decode("utf-8"))

folder = Path("Test")

with open(folder / "utf-8.txt", "wb") as f:
    f.write(message.encode("utf-8"))


with open(folder / "utf-16.txt", "wb") as f:
    f.write(message.encode("utf-16"))


with open(folder / "cp1251.txt", "wb") as f:
    f.write(message.encode("cp1251"))

with open(folder / "utf-8.txt", 'rb') as f:
    print(f.read().decode("utf-8"))
with open(folder / "utf-16.txt", 'rb') as f:
    print(f.read().decode("utf-16"))
with open(folder / "cp1251.txt", 'rb') as f:
    print(f.read().decode("cp1251"))
