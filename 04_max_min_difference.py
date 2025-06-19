n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
if n1 > n2 and n1 > n3:
    max = n1
elif n2 > n1 and n2 > n3:
    max = n2
else:
    max = n3

if n1 < n2 and n1 < n3:
    min = n1
elif n2 < n1 and n2 < n3:
    min = n2
else:
    min = n3
print(f"มากกว่า: {max - min}")