#question 1
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example:
original_price = 1000.0
discount = 20.0
final_price = calculate_discount(original_price, discount)
print(f"The final price is: {final_price}")
#question 2
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    
    final_price = calculate_discount(original_price, discount_percent)

    if discount_percent >= 20:
        print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: {original_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for the price and discount percentage.")
