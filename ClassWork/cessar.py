txt = "For example !  3.2"

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symb = [',', '.', '-', '?', '!', '(', ')', ' ']

str_1 = ""

step = 3

for i in txt:
    if i in num:
        str_1 += str(i)

    elif i in symb:
        str_1 += str(i)

    elif ord(i) + step > ord("z"):
        str_1 += chr(ord(i) + step - 26)

    else:
        str_1 += chr(ord(i) + step)

print(str_1)
