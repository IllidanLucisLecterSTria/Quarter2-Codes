def calculate_delivery_fee(distance_km, php_per_km):
    delivery_fee = distance_km * php_per_km
    return delivery_fee
distance = float(input("Enter distance in kilometers: "))
php_per_km = float(input("Enter rate per kilometer (₱): "))
fee = calculate_delivery_fee(distance, php_per_km)
print(f"Total Delivery Fee: ₱{fee:.2f}")