```
โจทย์แบบฝึกหัดนี้เอามาจาก markpruet เพื่อใช้ฝึกฝนเขียนโปรแกรม
1.
รับค่าคะแนน เป็นเลขจำนวนเต็ม แล้วทำการเขียนโปรแกรมเพื่อคำนวณเกรด
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

2.
รับจำนวนเต็มบวกหนึ่งจำนวน แล้วหาว่าจำนวนนั้นมากกว่า 31 หรือไม่
n = int(input("Enter a number: "))
if n > 31:
    print("yes")
else:
    print("no")

3.
รับจำนวนเต็มบวกหนึ่งจำนวน แล้วหาว่าจำนวนนั้นน้อยกว่า 90 หรือไม่
n = int(input("Enter a number: "))
if n < 90:
    print("yes")
else:
    print("no")

4.
รับจำนวนเต็ม 3 จำนวน แล้วหาว่าจำนวนที่มากที่สุดมากกว่าจำนวนที่น้อยที่สุดอยู่เท่าไหร่ 
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

5.
ร้านขายเครื่องใช้ไฟฟ้าแห่งหนึ่ง นำเครื่องใช้ไฟฟ้าสามชนิดมาลดราคา ดังนี้
TV ราคา 6000 บาท 
DVD player ราคา 1500 บาท 
Audio System ราคา 3000 บาท 
ร้านค้ามอบส่วนลดพิเศษ 20% ให้กับลูกค้าที่มียอดซื้ออย่างน้อย 24,000 บาท 
จงเขียนโปรแกรมเพื่อรับจำนวนสินค้าแต่ละชนิดที่ลูกค้าจะซื้อ (เป็นจำนวนเต็มบวกหรือศูนย์) แล้ว
 คำนวณยอดซื้อ และแสดง ยอดซื้อรวม (total price) ส่วนลด (discount) ถ้ามี และ ราคาที่ต้องชำระ 
(payment) โดยราคาแสดงด้วยทศนิยม 2 ตำแหน่ง 
tv_price = 6000
dvd_price = 1500
audio_price = 3000
tv_qty = int(input("How many TVs: "))
dvd_qty = int(input("How many DVD players: "))
audio_qty = int(input("How many Audio System: "))
total_price = (tv_price * tv_qty) + (dvd_price * dvd_qty) + (audio_price * audio_qty)
if total_price >= 24000:
    pay = total_price * 0.8
else:
    pay = total_price
print(f"Total price is {total_price:.2f} baht")
if total_price > pay:
    discount = total_price - pay
    print(f"You've got a discount of {discount:.2f} baht")
print(f"Your payment is {pay:.2f} baht")
