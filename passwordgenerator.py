import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
in_let=int(input("enter the num of letters"))
in_num=int(input("enter the num of numbers"))
in_symbols=int(input("enter the num of symbols"))
password=[]

for i in range(1,in_let+1):
    password+=random.choice(letters)
for i in range(1,in_num+1):
    password+=random.choice(numbers)
for i in range(1,in_symbols+1):
    password+=random.choice(symbols)
random.shuffle(password)

passw =""
for x in password:
    passw+=x
print(passw)