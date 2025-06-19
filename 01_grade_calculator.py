n = int(input("กรอกคะแนน: "))
if n >= 80:
    result = "ได้เกรด A"
elif n >= 70:
    result = "ได้เกรด B"
elif n >= 60:
    result = "ได้เกรด C"
elif n >= 50:
    result = "ได้เกรด D"
else:
    result = "ได้เกรด F"
print(result)