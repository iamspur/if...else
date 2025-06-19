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